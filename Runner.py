from datetime import datetime, timedelta
import traceback
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import datetime as dt
import calendar
import time
import pytz


reservation_date = dt.datetime.now()+timedelta(days=4)

reservation_rooms = ["370A", "370B", "381", "386", "176", "172"]

url = "https://ucf.libcal.com/reserve/generalstudyroom"




def main():
    print("Date Reserveing: " + reservation_date.strftime("%B %d, %Y"))

    driver1 = webdriver.Chrome()
    driver1.get(url)
    gotoday(driver1)
    ReserveEngine(driver1, datetime.strptime("9:00am", "%I:%M%p"), datetime.strptime("1:30pm", "%I:%M%p"))
    

#confirms availability and calls reserve fuction to reserve it. 

def ReserveEngine(driver, start, finish):
    i=0
    while True:
    	if(checkavailable(driver, i, start, finish)):
    		print("Reserving Room: " + reservation_rooms[i])
    		reserve(driver, i ,start, finish)
    		break
    	else:
    		print("Could not reserve: " + reservation_rooms[i])
    		i += 1


#Log In function 

def login(driver, username, password):
	print("Logging In")
	username_field = driver.find_element("xpath", "//input[@id='userNameInput']")
	username_field.send_keys(username)
	password_field = driver.find_element("xpath", "//input[@id='passwordInput']")
	password_field.send_keys(password)
	sign_on_button = driver.find_element("xpath", "//span[@id='submitButton']")
	sign_on_button.click()
	time.sleep(5)
	print("Logged In Sucessfully")



# Room reservation function
    
def reserve(driver, roomInt,start, finish):
	times = getTimesInList(start, finish)
	print(times[0]+" to "+times[len(times)-1]+" on "+reservation_date.strftime("%A, %B %d, %Y"))
	myTimes = ListAvailablesStrings(start,finish, reservation_rooms[roomInt])
	temp = driver.find_element("xpath", "//a[@class='fc-timeline-event fc-h-event fc-event fc-event-start fc-event-end fc-event-future s-lc-eq-avail' and @aria-label='"+myTimes[0]+"']")
	driver.execute_script("arguments[0].click();", temp)
	time.sleep(7)
	dropdown = driver.find_element("xpath","//select[@class='form-control input-sm b-end-date']")
	dropselect = Select(dropdown)
	dropselect.select_by_visible_text(times[len(times)-2]+" "+reservation_date.strftime("%A, %B %d, %Y"))
	time.sleep(6)
	driver.find_element("xpath", "//button[@id='submit_times']").click()
	time.sleep(4)
	login(driver, 'NID', 'Password')
	time.sleep(4)
	driver.find_element("xpath", "//button[@class='btn btn-primary' and @name='continue']").click()
	driver.find_element("xpath", "//input[@name='nick']").send_keys("Reservation Name")
	dropdown = driver.find_element("xpath", "//select[@name='q2613']")
	dropselect = Select(dropdown)
	dropselect.select_by_visible_text("Undergraduate Student")
	driver.find_element("xpath", "//input[@id='q2614']").send_keys("SID")
	driver.find_element("xpath", "//button[@type='submit' and @id='btn-form-submit']").click()
	time.sleep(6)
	print("Booked Room: " + reservation_rooms[roomInt])
	Exit(driver)
         
   

# Helper Functions: #

def date_to_unix_timestamp(date):
    date_object = dt.datetime.strptime(
        date, '%Y-%m-%d').replace(tzinfo=pytz.timezone('GMT'))
    return (int(date_object.timestamp())) * 1000


#changes current date to reservation date to list availability

def gotoday(driver):
    driver.find_element(
        "xpath", "//button[@class='fc-goToDate-button btn btn-default btn-sm' and @aria-label='Go To Date']").click()
    if (driver.find_element("xpath", "//th[@class='datepicker-switch'and @colspan='5']").text != reservation_date.strftime("%B %Y")):
        driver.find_element("xpath", "//th[@class='next']").click()
        print(driver.find_element("Going to: "+"xpath",
              "//th[@class='datepicker-switch'and @colspan='5']").text)
    driver.find_element("xpath", "//td[@data-date='" + str(date_to_unix_timestamp(reservation_date.strftime("%Y-%m-%d"))) + "']").click()
    time.sleep(1)


#creates list of all reservation time (every 30 mins)

def getTimesInList(start, end):
    times = []
    while start <= end:
        times.append(start.strftime("%I:%M%p").lstrip('0').lower())
        start += timedelta(minutes=30)
    return times
    

#Creates list of availablity strings

def ListAvailablesStrings(start, end, roomToReseve):
    i = 0
    finals = []
    times = getTimesInList(start, end)
    while start <= end:
        finals.append(times[i]+" "+reservation_date.strftime("%A, %B %d, %Y")+" - Room "+roomToReseve+" - Available")
        start += timedelta(minutes=30)
        i = i + 1
    return finals

#Checks for availability

def checkavailable(driver, roomNum, start, finish):
    myTimes = ListAvailablesStrings(start,finish, reservation_rooms[roomNum])
    try:
        for i in range(len(myTimes)):
            driver.find_element("xpath", "//a[@class='fc-timeline-event fc-h-event fc-event fc-event-start fc-event-end fc-event-future s-lc-eq-avail' and @aria-label='"+myTimes[i]+"']")
        return True
    except Exception:
        return False

def Exit(driver):
	print("Good Bye")
	driver.close()

# Calling Main: #

main()
