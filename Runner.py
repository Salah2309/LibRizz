from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from datetime import timedelta
import datetime as dt
import calendar
import time
import pytz

# THINGS TO WORK ON
# AUTOMATE ROOM NUMBER ROTATION
# LOOP FOR RESRERVE FUNCTION TO MAKE MULTIPLE RESERVATION

reservation_date=dt.datetime.now()+timedelta(days=6)
reservation_rooms = ["370A","370B","381","386","176","172"]
room_resource_id= ["eid_150798","eid_150789","eid_150811","eid_150812","eid_113208","eid_151291"]
start_time1 = ["9:00am","9:30am","10:00am","10:30am","11:00am","11:30am","12:00pm","12:30pm"]
#start_time2
#start_time3



url = "https://ucf.libcal.com/reserve/generalstudyroom"

def main():
	driver1 = webdriver.Chrome()
    #driver2 = webdriver.Chrome()
    #driver3 = webdriver.Chrome()

	driver1.get(url)
    #driver2.get(url)
    #driver3.get(url)
    
	gotoday(driver1)
    #gotoday(driver2)
    #gotoday(driver3)
	checkavailable(driver1, (timedateconvertor()))
	#check_exists_by_xpath(driver1)
	#reserve(driver1, timedateconvertor(), reservation_rooms[0],'a', "b")
	#reserve(driver1, (timedateconvertor()), reservation_rooms[0] ,'a', "b")


    #reserve(driver, "370", "12","1")
    #<button class="fc-goToDate-button btn btn-default btn-sm" type="button" aria-label="Go To Date" data-original-title="" title=""><i class="fa fa-calendar" aria-class="hidden"></i> Go To Date</button>
    #driver.find_element("name", "fa fa-calendar").click()
    #driver.find_element("data-date", "1678665600000").click()
	#time.sleep(15)
	
	
def date_to_unix_timestamp(date):
    date_object = dt.datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=pytz.timezone('GMT'))
    return (int(date_object.timestamp())) *1000

def gotoday(driver):
	driver.find_element("xpath", "//button[@class='fc-goToDate-button btn btn-default btn-sm' and @aria-label='Go To Date']").click()
	if(driver.find_element("xpath","//th[@class='datepicker-switch'and @colspan='5']").text != reservation_date.strftime("%B %Y")):
		driver.find_element("xpath","//th[@class='next']").click()
		print(driver.find_element("xpath","//th[@class='datepicker-switch'and @colspan='5']").text)	
	driver.find_element("xpath", "//td[@data-date='"+ str(date_to_unix_timestamp(reservation_date.strftime("%Y-%m-%d"))) +"']").click();
	

def timedateconvertor():
	if(int(reservation_date.strftime("%d"))<10):
		date = int(reservation_date.strftime("%d"))
		date = reservation_date.strftime("%A, %B ")+str(date)+reservation_date.strftime(", %Y")
		return date
	else:
		return reservation_date.strftime("%A, %B %d, %Y")
	

	
def checkavailable(driver, day):
	
	j =1
	counter = 0
	for i in start_time1:
		try:
			driver.find_element("xpath", f"//td[@class='fc-timeline-lane fc-resource' and @data-resource-id='"+room_resource_id[j]+"']//a[@title='"+i+" "+day+" - Room "+reservation_rooms[j]+" - Available""']//div[@class='fc-event-title fc-sticky']")
			counter+=1
			print("tried "+room_resource_id[j]+" at "+i+" "+day+" - Room "+reservation_rooms[j]+" - Available")
			#print(driver.find_element("xpath", f"//td[@class='fc-timeline-lane fc-resource' and @data-resource-id='"+room_resource_id[j]+"']").text)
		except:
			j+=1
			counter =0
			checkavailable(driver, day)
			print("not avil")
			#checkavailable(driver, day)
	if(counter>7):
		for i in start_time1:
			reserve(driver, (timedateconvertor()), reservation_rooms[j], room_resource_id[j] ,i)

def roomFinder(start_time, end_time):
	
    return 0

def reserve(driver, day, room, room_eid, start_time):
	#searches for room
	try:
		words = start_time+" "+day+" - Room "+room+" - Available"
		#temp = driver.find_element("xpath", "//td[@class='fc-timeline-lane fc-resource' and @data-resource-id='eid_150798']//a[@title='7:00am Tuesday, May 2, 2023 - Room 370A - Available']//div[@class='fc-event-title fc-sticky']")
		temp = driver.find_element("xpath", f"//td[@class='fc-timeline-lane fc-resource' and @data-resource-id='"+room_eid+"']//a[@title='"+words+"']//div[@class='fc-event-title fc-sticky']")
		driver.execute_script("arguments[0].click();", temp)
		time.sleep(7)
		driver.find_element("xpath", "//button[@id='submit_times']").click()
		time.sleep(15)
		login(driver,'nid','password')
		time.sleep(15)
		driver.find_element("xpath", "//button[@class='btn btn-primary' and @name='continue']").click()
		driver.find_element("xpath", "//input[@name='nick']").send_keys("Anagh")
		a = driver.find_element("xpath", "//select[@name='q2613']")
		dropselect =Select(a)
		dropselect.select_by_visible_text("Undergraduate Student")
		driver.find_element("xpath", "//input[@id='q2614']").send_keys("SID")
		driver.find_element("xpath", "//button[@type='submit' and @id='btn-form-submit']").click()
		time.sleep(10)
	except NoSuchElementException:
		print("Run it again")
		#main()
		#driver.close()
	
	
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
