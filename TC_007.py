# TC_007 : Login and Selecting hotels in multiple locations should not show
#          same hotels in Adactin Hotel Website - Chrome Browser

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
        
# Hotel Search    
    def hotel_search(self):
        location = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="location"]'))
        sleep(5)
        location.select_by_visible_text("Los Angeles")
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="hotels"]').click()
        sleep(3)
        location = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="location"]'))
        sleep(5)
        location.select_by_visible_text("Sydney")
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="hotels"]').click()
        sleep(3)
        location = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="location"]'))
        sleep(5)
        location.select_by_visible_text("Melbourne")
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="hotels"]').click()
        sleep(3)
        location = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="location"]'))
        sleep(5)
        location.select_by_visible_text("London")
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="hotels"]').click()
        sleep(3)
        location = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="location"]'))
        sleep(5)
        location.select_by_visible_text("New York")
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="hotels"]').click()
        sleep(3)
        location = Select(self.driver.find_element(by=By.XPATH, value='//*[@id="location"]'))
        sleep(5)
        location.select_by_visible_text("Paris")
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="hotels"]').click()
        sleep(3)
        self.driver.quit()
        


Ajith().login()
Ajith().hotel_search()