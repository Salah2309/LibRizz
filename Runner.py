import datetime
import pytz
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import datetime as dt
import calendar
import time
from datetime import timedelta

# THINGS TO WORK ON
# AUTOMATE ROOM NUMBER ROTATION
# LOOP FOR RESRERVE FUNCTION TO MAKE MULTIPLE RESERVATION

url = "https://ucf.libcal.com/reserve/generalstudyroom"

def main():
    driver1 = webdriver.Chrome()
    #driver2 = webdriver.Chrome()
    #driver3 = webdriver.Chrome()
    driver1.get(url)
    #driver2.get(url)
    #driver3.get(url)
    reservation_date = dt.datetime.now()+timedelta(days=8)
    driver1 = gotoday(driver1,(reservation_date.strftime("%Y-%m-%d")))
    time.sleep(25)

def checkavailable(room, start_time, end_time):
	
    return 0


def gotoday(driver, day):
    print(day)
    driver.find_element("xpath","//button[@class='fc-goToDate-button btn btn-default btn-sm'and @aria-label='Go To Date']").click()
    driver.find_element("xpath","//td[@data-date='"+str(date_to_unix_timestamp(day))+"']").click()
    return driver

def date_to_unix_timestamp(date_string):
    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d').replace(tzinfo=pytz.timezone('GMT'))
    return (int(date_object.timestamp())) *1000


def reserve(driver, day, room, start_time, end_time):
	#searches for room 
	temp = driver.find_element("xpath", "//td[@class='fc-timeline-lane fc-resource' and @data-resource-id='eid_150798']//a[@title='7:30am Tuesday, April 25, 2023 - Room 370A - Available']//div[@class='fc-event-title fc-sticky']")
	driver.execute_script("arguments[0].click();", temp)
	time.sleep(7)
	driver.find_element("xpath", "//button[@id='submit_times']").click()
	time.sleep(15)
	login(driver,'UCFNID','UCFPASSWORD')
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
    try:
        username_field = driver.find_element_by_id("userNameInput")
        password_field = driver.find_element_by_id("passwordInput")
        sign_on_button = driver.find_element_by_id("submitButton")

        time.sleep(20)
        
        username_field = driver.find_element("xpath", "//input[@id='userNameInput']")
        username_field.send_keys(username)
        password_field = driver.find_element("xpath", "//input[@id='passwordInput']")
        password_field.send_keys(password)
        sign_on_button = driver.find_element("xpath", "//span[@id='submitButton']")
        sign_on_button.click()
    except:
        print("Could Not Login!!!")

main()
