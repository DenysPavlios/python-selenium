import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/python_selenium/runTest_1/chromedriver')
# driver = webdriver.Firefox(executable_path='/Users/mcden/Desktop/pythonPRO/python_selenium/geckodriver')

driver.get('https://www.saucedemo.com/')

# user_name = driver.find_element(By.ID,'user-name') # ID
# user_name = driver.find_element(By.NAME,'user-name') #NAME
# user_name = driver.find_element(By.XPATH,'//*[@id="user-name"]') #Full XPath
# user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]') #XPath
user_name = driver.find_element(By.XPATH,'//input[@data-test="username"]') #data-test
user_name.send_keys('standard_user')
pasword = driver.find_element(By.CSS_SELECTOR,'#password') #CSS
pasword.send_keys('secret_sauce')
login = driver.find_element(By.XPATH,'//input[@id="login-button"]') #login
login.click()
time.sleep(3)
driver.close()
