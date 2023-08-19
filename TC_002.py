# TC_002 : Invalid Login to Adactin Hotel Website - Chrome Browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Ajith():
    url = 'https://adactinhotelapp.com/index.php'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    username = 'ajithd23'
    password = 'invalid password'

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
        self.driver.quit()

Ajith().login()