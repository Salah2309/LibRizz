import datetime as dt
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import pytz


# Custom Setters: #

# use "6:00am" format
# do not select more than 12 hours!
StartTime = "7:30am"
EndTime = "4:00pm"
daysTravel = 7
username1 = "NID"
password1 = "Password"
username2 = "NID"
password2 = "Password"
username3 = "NID"
password3 = "Password"

#
# https://ucf.libcal.com/reserve/generalstudyroom
# https://library.ucf.edu/maps/


# DO NOT CHANGE ANYTHING BELOW THIS LINE #

def main():
    print("\n\n--Date Reserveing: " + reservation_date.strftime("%B %d, %Y"))
    # Finds Empty Room:
    roomToBook = FoundOurRoom()
    if (roomToBook == ''):
        return
    # Books Room for Given Time
    driver1 = JobOpener('_Booking1', isVisible=True)
    driver2 = JobOpener('_Booking2', isVisible=False)
    driver3 = JobOpener('_Booking3', isVisible=False)
    reserveEngine(driver1, driver2, driver3, roomToBook)

    JobCloser(driver1, '_Booking1')
    JobCloser(driver2, '_Booking2')
    JobCloser(driver3, '_Booking3')


def reserveSelect(driver1, driver2, driver3, roomToBook):

    # login(driver, 'NID', 'Password')
    # time.sleep(4)
    # driver.find_element(
    #     "xpath", "//button[@class='btn btn-primary' and @name='continue']").click()
    # driver.find_element(
    #     "xpath", "//input[@name='nick']").send_keys("Reservation Name")
    # dropdown = driver.find_element("xpath", "//select[@name='q2613']")
    # dropselect = Select(dropdown)
    # dropselect.select_by_visible_text("Undergraduate Student")
    # driver.find_element("xpath", "//input[@id='q2614']").send_keys("SID")
    # driver.find_element(
    #     "xpath", "//button[@type='submit' and @id='btn-form-submit']").click()
    # time.sleep(6)
    # print("--Booked Room: " + roomToBook)
    # JobCloser(driver,1)
    pass

# Helper Functions: #

# Time Converter:


def date_to_unix_timestamp(date):
    date_object = dt.datetime.strptime(
        date, '%Y-%m-%d').replace(tzinfo=pytz.timezone('GMT'))
    return (int(date_object.timestamp())) * 1000


# changes current date to reservation date to list availability

def gotoday(driver, driverName):
    driver.find_element(
        "xpath", "//button[@class='fc-goToDate-button btn btn-default btn-sm' and @aria-label='Go To Date']").click()
    if (driver.find_element("xpath", "//th[@class='datepicker-switch'and @colspan='5']").text != reservation_date.strftime("%B %Y")):
        driver.find_element("xpath", "//th[@class='next']").click()
        print("--Driver"+str(driverName)+" Page Traveled To Next Month: " +
              driver.find_element("xpath", "//th[@class='datepicker-switch'and @colspan='5']").text)
    driver.find_element("xpath", "//td[@data-date='" + str(
        date_to_unix_timestamp(reservation_date.strftime("%Y-%m-%d"))) + "']").click()
    time.sleep(1)


# Room Finder:
def FoundOurRoom():
    driver = JobOpener('_RoomFinder', isVisible=False)
    time.sleep(1)
    for i in range(len(reservation_rooms)):
        if (checkavailable(driver, i)):
            print("--Found Empty Room: " + reservation_rooms[i])
            JobCloser(driver, '_RoomFinder')
            return reservation_rooms[i]
    print("++All The Rooms Were Unavailable!")
    JobCloser(driver, '_RoomFinder')
    return ''


# creates list of all reservation time (every 30 mins)

def getTimesInList():
    timer = start
    myTimes = []
    while timer <= finish:
        myTimes.append(timer.strftime("%I:%M%p").lstrip('0').lower())
        timer += timedelta(minutes=30)
    return myTimes


# Creates list of availablity strings

def ListAvailablesStrings(roomToReseve):
    i = 0
    timer = start
    finals = []
    myTimes = getTimesInList()
    while timer <= finish:
        finals.append(myTimes[i]+" "+reservation_date.strftime("%A, %B %d, %Y") +
                      " - Room "+roomToReseve+" - Available")
        timer += timedelta(minutes=30)
        i = i + 1
    return finals


# Checks for availability

def checkavailable(driver, roomNum):
    myString = ListAvailablesStrings(reservation_rooms[roomNum])
    try:
        for i in range(len(myString)):
            driver.find_element(
                "xpath", "//a[@class='fc-timeline-event fc-h-event fc-event fc-event-start fc-event-end fc-event-future s-lc-eq-avail' and @aria-label='"+myString[i]+"']")
        return True
    except:
        return False

# Room reservation function


def reserve(Driver, DriverName, Room, From, To):
    try:
        select = (From+" "+reservation_date.strftime("%A, %B %d, %Y") +
                  " - Room "+Room+" - Available")
        temp = Driver.find_element(
            "xpath", "//a[@class='fc-timeline-event fc-h-event fc-event fc-event-start fc-event-end fc-event-future s-lc-eq-avail' and @aria-label='"+select+"']")
        Driver.execute_script("arguments[0].click();", temp)
        time.sleep(1)
        dropdown = Driver.find_element(
            "xpath", "//select[@class='form-control input-sm b-end-date']")
        dropselect = Select(dropdown)
        dropselect.select_by_visible_text(
            To+" "+reservation_date.strftime("%A, %B %d, %Y"))
        Driver.find_element("xpath", "//button[@id='submit_times']").click()
        time.sleep(1)
        print("--Driver" + DriverName + " is booking room: " +
              Room + " from: "+From + " to: " + To)

        # if(not login(Driver, DriverName)):
        #     print("--WARNING: Driver" + DriverName + " FAILED TO Login!")
        # print("--Driver" + DriverName + " login successful")
    except:
        print("++WARNING: Driver" + DriverName +
              " FAILED to book room: " + Room)


# checks how many reserve calls needed and calls them:
def reserveEngine(driver1, driver2, driver3, room):
    tempTimes = getTimesInList()
    myTimes = []
    for i in range(len(tempTimes)):
        if (i == 0 or i % 8 == 0):
            myTimes.append(tempTimes[i])
    if (myTimes[len(myTimes)-1] != finish.strftime("%I:%M%p").lstrip('0').lower()):
        myTimes.append(finish.strftime("%I:%M%p").lstrip('0').lower())

    if (len(myTimes) > 1):
        reserve(Driver=driver1, DriverName='_Booking1',
                Room=room, From=myTimes[0], To=myTimes[1])
    if (len(myTimes) > 2):
        reserve(Driver=driver2, DriverName='_Booking2',
                Room=room, From=myTimes[1], To=myTimes[2])
    if (len(myTimes) > 3):
        reserve(Driver=driver3, DriverName='_Booking3',
                Room=room, From=myTimes[2], To=myTimes[3])


# Log In function

def login(driver, driverName):
    match driverName:
        case '_Booking1':
            username = username1
            password = password1
        case '_Booking2':
            username = username2
            password = password2
        case '_Booking3':
            username = username3
            password = password3
        case _:
            print("++WARNING: WRONG DriverName Passed To Login!")
            return False
    try:
        username_field = driver.find_element(
            "xpath", "//input[@id='userNameInput']")
        username_field.send_keys(username)
        password_field = driver.find_element(
            "xpath", "//input[@id='passwordInput']")
        password_field.send_keys(password)
        sign_on_button = driver.find_element(
            "xpath", "//span[@id='submitButton']")
        sign_on_button.click()
        return True
    except:
        return False

# Driver Jobs:


def JobOpener(driverName, isVisible):
    print("--Job Opened for: Driver"+str(driverName))
    options = Options()
    if (not isVisible):
        options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    gotoday(driver, driverName)
    return driver


def JobCloser(driver, driverName):
    driver.close()
    print("--Job Closed for: Driver" + str(driverName))
    return


# Our GLobals:
reservation_rooms = ["381", "370A", "370B", "176", "172",
                     "386", "387", "388", "389", "377", "371", "372", "373"]
url = "https://ucf.libcal.com/reserve/generalstudyroom"
start = datetime.strptime(StartTime, "%I:%M%p")
finish = datetime.strptime(EndTime, "%I:%M%p")
reservation_date = dt.datetime.now()+timedelta(days=daysTravel)


# Calling Main:
main()
