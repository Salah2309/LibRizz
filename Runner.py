from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

url = "https://ucf.libcal.com/reserve/generalstudyroom"

def main():
    driver = webdriver.Chrome()
    driver.get(url)
    #time.sleep(10)
    time.sleep(2)
    driver.find_element("xpath", "//button[@class='fc-goToDate-button btn btn-default btn-sm' and @aria-label='Go To Date']").click()
    time.sleep(3)
    #<button class="fc-goToDate-button btn btn-default btn-sm" type="button" aria-label="Go To Date" data-original-title="" title=""><i class="fa fa-calendar" aria-class="hidden"></i> Go To Date</button>
    l.click()
    print(ran)
    #driver.find_element("name", "fa fa-calendar").click()
    #driver.find_element("data-date", "1678665600000").click()
    login(driver,'yourlogin','yourpassword')
	

def checkavailable(room, start_time, end_time):

    return 0


def reserve(room, start_time, end_time):

    return 0

def login(driver, username, password):
    try:
        username_field = driver.find_element_by_id("userNameInput")
        password_field = driver.find_element_by_id("passwordInput")
        sign_on_button = driver.find_element_by_id("submitButton")

        username_field.send_keys(username)
        password_field.send_keys(password)
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
