from datetime import datetime, timedelta
import traceback
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

reservation_date = dt.datetime.now()+timedelta(days=5)

reservation_rooms = ["370A", "370B", "381", "386", "176", "172"]

url = "https://ucf.libcal.com/reserve/generalstudyroom"


def main():
    print("Date Reserveing: " + reservation_date.strftime("%B %d, %Y"))

    driver1 = webdriver.Chrome()
    driver1.get(url)
    gotoday(driver1)
    ReserveEngine(driver1, datetime.strptime("8:00am", "%I:%M%p"), datetime.strptime("12:30pm", "%I:%M%p"))


    # <button class="fc-goToDate-button btn btn-default btn-sm" type="button" aria-label="Go To Date" data-original-title="" title=""><i class="fa fa-calendar" aria-class="hidden"></i> Go To Date</button>
    # driver.find_element("name", "fa fa-calendar").click()
    # driver.find_element("data-date", "1678665600000").click()
    # 7:00am Monday, May 1, 2023 - Room 370A - Available


def ReserveEngine(driver, start, finish):
    i=0
    while i < int(len(reservation_rooms)):
        if(checkavailable(driver, i, start, finish)):
            print("Reserving Room: " + reservation_rooms[i])
            # here 
            break
        else:
            print("Could not reserve: " + reservation_rooms[i])
            i += 1
            
    myTimes = ListAvailablesStrings(start,finish, reservation_rooms[0])
    try:
        for i in range(len(myTimes)):
            driver.find_element("xpath", "//a[@class='fc-timeline-event fc-h-event fc-event fc-event-start fc-event-end fc-event-future s-lc-eq-avail' and @aria-label='"+myTimes[i]+"']")
        return True
    except Exception:
        return False


    # driver.find_element("xpath", "//button[@id='submit_times']").click()
    # time.sleep(15)
    # login(driver,'NIDHERE','PASSWORD')
    # time.sleep(15)
    # driver.find_element("xpath", "//button[@class='btn btn-primary' and @name='continue']").click()
    # driver.find_element("xpath", "//input[@name='nick']").send_keys("RESERVATIONNAME")
    # a = driver.find_element("xpath", "//select[@name='q2613']")
    # dropselect =Select(a)
    # dropselect.select_by_visible_text("Undergraduate Student")
    # driver.find_element("xpath", "//input[@id='q2614']").send_keys("NID GOES HERE")
    # driver.find_element("xpath", "//button[@type='submit' and @id='btn-form-submit']").click()
    # time.sleep(10)


# WIP: #

def login(driver, username, password):
    username_field = driver.find_element("xpath", "//input[@id='userNameInput']")
    username_field.send_keys(username)
    password_field = driver.find_element("xpath", "//input[@id='passwordInput']")
    password_field.send_keys(password)
    sign_on_button = driver.find_element("xpath", "//span[@id='submitButton']")
    sign_on_button.click()
    time.sleep(5)
    print("tried ")



# Anag's work:      
    
def reserve(driver, start, finish):
    myTimes = ListAvailablesStrings(start,finish, reservation_rooms[0])
    try:
        for i in range(len(myTimes)):
            temp = driver.find_element("xpath", "//a[@class='fc-timeline-event fc-h-event fc-event fc-event-start fc-event-end fc-event-future s-lc-eq-avail' and @aria-label='"+myTimes[i]+"']")
        return True
    except Exception:
        return False

    # searches for room
    try:
        driver.execute_script("arguments[0].click();", temp)
        time.sleep(7)
        driver.find_element("xpath", "//button[@id='submit_times']").click()
        time.sleep(15)
        login(driver, 'nid', 'password')
        time.sleep(15)
        driver.find_element(
            "xpath", "//button[@class='btn btn-primary' and @name='continue']").click()
        driver.find_element(
            "xpath", "//input[@name='nick']").send_keys("Anagh")
        a = driver.find_element("xpath", "//select[@name='q2613']")
        dropselect = Select(a)
        dropselect.select_by_visible_text("Undergraduate Student")
        driver.find_element("xpath", "//input[@id='q2614']").send_keys("SID")
        driver.find_element(
            "xpath", "//button[@type='submit' and @id='btn-form-submit']").click()
        time.sleep(10)
    except NoSuchElementException:
        print("Run it again")
        # main()
        # driver.close()


# Helper Functions: #

def date_to_unix_timestamp(date):
    date_object = dt.datetime.strptime(
        date, '%Y-%m-%d').replace(tzinfo=pytz.timezone('GMT'))
    return (int(date_object.timestamp())) * 1000


def gotoday(driver):
    driver.find_element(
        "xpath", "//button[@class='fc-goToDate-button btn btn-default btn-sm' and @aria-label='Go To Date']").click()
    if (driver.find_element("xpath", "//th[@class='datepicker-switch'and @colspan='5']").text != reservation_date.strftime("%B %Y")):
        driver.find_element("xpath", "//th[@class='next']").click()
        print(driver.find_element("Going to: "+"xpath",
              "//th[@class='datepicker-switch'and @colspan='5']").text)
    driver.find_element("xpath", "//td[@data-date='" + str(date_to_unix_timestamp(reservation_date.strftime("%Y-%m-%d"))) + "']").click()
    time.sleep(1)

def getTimesInList(start, end):
    times = []
    while start <= end:
        times.append(start.strftime("%I:%M%p").lstrip('0').lower())
        start += timedelta(minutes=30)
    return times


def ListAvailablesStrings(start, end, roomToReseve):
    i = 0
    finals = []
    times = getTimesInList(start, end)
    while start <= end:
        finals.append(times[i]+" "+reservation_date.strftime("%A, %B %d, %Y")+" - Room "+roomToReseve+" - Available")
        start += timedelta(minutes=30)
        i = i + 1
    return finals

def checkavailable(driver, roomNum, start, finish):
    myTimes = ListAvailablesStrings(start,finish, reservation_rooms[roomNum])
    try:
        for i in range(len(myTimes)):
            driver.find_element("xpath", "//a[@class='fc-timeline-event fc-h-event fc-event fc-event-start fc-event-end fc-event-future s-lc-eq-avail' and @aria-label='"+myTimes[i]+"']")
        return True
    except Exception:
        return False


# Calling Main: #

main()
