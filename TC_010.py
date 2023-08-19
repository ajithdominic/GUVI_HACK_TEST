# TC_010 : Login and Selecting hotels in desired location and booking won't happen
#          until the CVV Number is in proper 3 digit format in Adactin Hotel Website - Chrome Browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


class Ajith():
    url = 'https://adactinhotelapp.com/index.php'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    username = 'ajithd23'
    password = 'admin123'
    checkin = '20/08/2023'
    checkout = '22/08/2023'
    firstname = 'Admin'
    lastname = 'Guy'
    address = '400 S Main St Los Angeles, California(CA), 90013'
    creditcard = '1234567887654321'
    cvv = '7'

# Render Website and Login
    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="login"]').click()
        sleep(5)
        
# Hotel Search    
    def hotel_search(self):
        location = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="location"]'))
        location.select_by_visible_text("Los Angeles")
        sleep(1)
        hotels = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="hotels"]'))
        hotels.select_by_visible_text("Hotel Sunshine")
        sleep(1)
        roomtype = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="room_type"]'))
        roomtype.select_by_visible_text("Double")
        sleep(1)
        adults = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="room_nos"]'))
        adults.select_by_visible_text("1 - One")
        sleep(1)
        self.driver.find_element(by=By.XPATH, value='//*[@id="datepick_in"]').clear()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value='//*[@id="datepick_in"]').send_keys(self.checkin)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value='//*[@id="datepick_out"]').clear()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value='//*[@id="datepick_out"]').send_keys(self.checkout)
        sleep(1)
        adults = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="adult_room"]'))
        adults.select_by_visible_text("2 - Two")
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="Submit"]').click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="radiobutton_0"]').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="continue"]').click()
        sleep(5)

# Booking by filling in payment details
    def booking(self):
        self.driver.find_element(by=By.XPATH, value='//*[@id="first_name"]').send_keys(self.firstname)
        self.driver.find_element(by=By.XPATH, value='//*[@id="last_name"]').send_keys(self.lastname)
        self.driver.find_element(by=By.XPATH, value='//*[@id="address"]').send_keys(self.address)
        self.driver.find_element(by=By.XPATH, value='//*[@id="cc_num"]').send_keys(self.creditcard)
        sleep(1)
        cctype = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="cc_type"]'))
        cctype.select_by_visible_text("American Express")
        sleep(1)
        ccmonth = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="cc_exp_month"]'))
        ccmonth.select_by_visible_text("August")
        sleep(1)
        ccyear = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="cc_exp_year"]'))
        ccyear.select_by_visible_text("2028")
        sleep(1)
        self.driver.find_element(by=By.XPATH, value='//*[@id="cc_cvv"]').send_keys(self.cvv)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value='//*[@id="book_now"]').click()
        sleep(10)
        self.driver.quit()


Ajith().login()
Ajith().hotel_search()
Ajith().booking()