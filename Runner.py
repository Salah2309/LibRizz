from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from datetime import timedelta
import datetime as dt
import calendar
import time
import pytz

# THINGS TO WORK ON
# AUTOMATE ROOM NUMBER ROTATION
# LOOP FOR RESRERVE FUNCTION TO MAKE MULTIPLE RESERVATION

reservation_date=dt.datetime.now()+timedelta(days=2)

url = "https://ucf.libcal.com/reserve/generalstudyroom"

def main():
    driver = webdriver.Chrome()
    #driver1 = webdriver.Chrome()
    driver.get(url)
    #driver1.get(url)
    gotoday(driver)
    #gotoday(driver1, reservation_date)
    reserve(driver, (reservation_date.strftime("%B %d, %Y")), 'aa','a', "b")
    #reserve(driver, (reservation_date.strftime("%B %d, %Y")), 'aa','a', "b")
   # reserve(driver, "370", "12","1")
    #<button class="fc-goToDate-button btn btn-default btn-sm" type="button" aria-label="Go To Date" data-original-title="" title=""><i class="fa fa-calendar" aria-class="hidden"></i> Go To Date</button>
    #driver.find_element("name", "fa fa-calendar").click()
    #driver.find_element("data-date", "1678665600000").click()
    driver.implicitly_wait(90)
    driver.implicitly_wait(90)
    time.sleep(8)
    time.sleep(15)
	
	
def date_to_unix_timestamp(date):
    date_object = dt.datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=pytz.timezone('GMT'))
    print((int(date_object.timestamp())) *1000)
    return (int(date_object.timestamp())) *1000


def checkavailable(room, start_time, end_time):
	

    return 0

def gotoday(driver):
	#setting time 0:0 in datetime 
	
	driver.find_element("xpath", "//button[@class='fc-goToDate-button btn btn-default btn-sm' and @aria-label='Go To Date']").click()
	if(driver.find_element("xpath","//th[@class='datepicker-switch'and @colspan='5']").text == reservation_date.strftime("%B %Y")):
		print("works")
	else:
		print("dontwork")
	
	
	driver.find_element("xpath", "//td[@data-date='"+ str(date_to_unix_timestamp(reservation_date.strftime("%Y-%m-%d"))) +"']").click();
	#time.sleep(3)
	driver.implicitly_wait(4)
	

def reserve(driver, day, room, start_time, end_time):
	#searches for room 
	temp = driver.find_element("xpath", "//td[@class='fc-timeline-lane fc-resource' and @data-resource-id='eid_150798']//a[@title='7:00am Wednesday, April 26, 2023 - Room 370A - Available']//div[@class='fc-event-title fc-sticky']")
	driver.execute_script("arguments[0].click();", temp)
	time.sleep(7)
	driver.find_element("xpath", "//button[@id='submit_times']").click()
	time.sleep(15)
	login(driver,'NIDHERE','PASSWORD')
	time.sleep(15)
	driver.find_element("xpath", "//button[@class='btn btn-primary' and @name='continue']").click()
	driver.find_element("xpath", "//input[@name='nick']").send_keys("RESERVATIONNAME")
	a = driver.find_element("xpath", "//select[@name='q2613']")
	dropselect =Select(a)
	dropselect.select_by_visible_text("Undergraduate Student")
	driver.find_element("xpath", "//input[@id='q2614']").send_keys("NID GOES HERE")
	driver.find_element("xpath", "//button[@type='submit' and @id='btn-form-submit']").click()
	time.sleep(10)
	
	
def login(driver, username, password):
 
        username_field = driver.find_element("xpath", "//input[@id='userNameInput']")
        username_field.send_keys(username)
        password_field = driver.find_element("xpath", "//input[@id='passwordInput']")
        password_field.send_keys(password)
        sign_on_button = driver.find_element("xpath", "//span[@id='submitButton']")
        sign_on_button.click()
        time.sleep(5)
        print("tried ")
   

main()
