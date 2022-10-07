import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/python_selenium/runTest_1/chromedriver')
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

userName = driver.find_element(By.XPATH,'//input[@id="user-name"]')
userName.send_keys(login_standard_user)
userName.send_keys(Keys.BACKSPACE)
time.sleep(2)
userName.send_keys('r')

pasword = driver.find_element(By.XPATH,'//input[@id="password"]')
pasword.send_keys(password_all)
pasword.send_keys(Keys.RETURN)

driver.execute_script('window.scrollTo(0,500)')
driver.close()