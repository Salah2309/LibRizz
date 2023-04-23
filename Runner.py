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
    driver = webdriver.Chrome()
    driver.get(url)
    driver = gotoday(driver,date_to_unix_timestamp('2023-04-18'))
    time.sleep(25)


def checkavailable(room, start_time, end_time):
	
    return 0


def gotoday(driver, day):
    driver.find_element("xpath","//button[@class='fc-goToDate-button btn btn-default btn-sm'and @aria-label='Go To Date']").click()
    driver.find_element("xpath","//td[@data-date='1682121600000']").click()
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

#CHATGPT SAID:
# def make_reservation():
#     username = "your_username"
#     password = "your_password"
#     capacity = "10"
#     time_slot = "12:00 PM - 1:00 PM"
#     driver = webdriver.Chrome()
#     driver.get(url)
#     username_field = driver.find_element_by_id("username")
#     username_field.send_keys(username)
#     password_field = driver.find_element_by_id("password")
#     password_field.send_keys(password)
#     login_button = driver.find_element_by_name("_eventId_proceed")
#     login_button.click()
#     capacity_field = driver.find_element_by_id("capacity")
#     capacity_field.send_keys(capacity)
#     time_slot_field = driver.find_element_by_id("s-lc-rm-time")
#     time_slot_field.send_keys(time_slot)
#     submit_button = driver.find_element_by_name("s-lc-rm-submit")
#     submit_button.click()
#     driver.quit()

# schedule.every().day.at("11:45").do(make_reservation)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
