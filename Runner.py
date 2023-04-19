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
    #time.sleep(10)
    #time.sleep(2)
    gotoday(driver, (dt.datetime.now()+timedelta(days=8)).strftime("%d"))
   # reserve(driver, "370", "12","1")
    #<button class="fc-goToDate-button btn btn-default btn-sm" type="button" aria-label="Go To Date" data-original-title="" title=""><i class="fa fa-calendar" aria-class="hidden"></i> Go To Date</button>
    #driver.find_element("name", "fa fa-calendar").click()
    #driver.find_element("data-date", "1678665600000").click()
    driver.implicitly_wait(90)
    driver.implicitly_wait(90)
    time.sleep(8)
    time.sleep(15)
	
def checkavailable(room, start_time, end_time):
	

    return 0

def gotoday(driver, day):

	driver.find_element("xpath", "//button[@class='fc-goToDate-button btn btn-default btn-sm' and @aria-label='Go To Date']").click()
	t=dt.datetime(2023, 4, 25, 0, 0, 0)
	dvalue = calendar.timegm(t.timetuple())*1000
	driver.find_element("xpath", "//td[@data-date='"+ str(dvalue) +"']").click();
	#time.sleep(3)
	driver.implicitly_wait(4)
	reserve(driver, "a",'a', "b")
	
	

def reserve(driver, room, start_time, end_time):
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
 
        username_field = driver.find_element("xpath", "//input[@id='userNameInput']")
        username_field.send_keys(username)
        password_field = driver.find_element("xpath", "//input[@id='passwordInput']")
        password_field.send_keys(password)
        sign_on_button = driver.find_element("xpath", "//span[@id='submitButton']")
        sign_on_button.click()
        time.sleep(5)
        print("tried ")
   

main()
