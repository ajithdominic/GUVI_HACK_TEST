# TC_006 : Login and Access Booked Itinerary and Cancel existing booking 
#          in Adactin Hotel Website - Chrome Browser

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
        
# Booked Itinerary Search and Cancel existing Booking    
    def booked(self):
        self.driver.find_element(by=By.LINK_TEXT, value='Booked Itinerary').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="booked_form"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/input').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="booked_form"]/table/tbody/tr[3]/td/input[1]').click()
        sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()
        sleep(10)
        self.driver.quit()



Ajith().login()
Ajith().booked()