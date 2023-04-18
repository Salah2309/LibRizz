from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

url = "https://ucf.libcal.com/reserve/generalstudyroom"

def main():
    driver = webdriver.Chrome()
    driver.get(url)
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

# Github credentials
username = "Username"
password = "Password"

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver.exe")

# head to github login page
driver.get("https://ucf.libcal.com/reserve/generalstudyroom")
html = driver.page_source
time.sleep(3)
#selecting date
driver.find_element("class", "fc-goToDate-button btn btn-default btn-sm").click()
#driver.find_element("data-date", "1678665600000").click()
#driver.find_element("style", "top: 0px; left: 814px; right: -851px;").click()
#driver.find_element("name", "submit_times").click()
# find username/email field and send the username itself to the input field
#driver.find_element("name", "UserName").send_keys(username)
# find password input field and insert password as well
#driver.find_element("name", "Password").send_keys(password)
# click login button
#driver.find_element("id", "submitButton").click()

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
    

# close the driver
driver.close()