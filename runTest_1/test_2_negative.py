from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/python_selenium/runTest_1/chromedriver')
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

login_standard_user = 'standard_use'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('input login')
pasword = driver.find_element(By.XPATH,'//input[@id="password"]')
pasword.send_keys(password_all)
print('input password')
button_login = driver.find_element(By.XPATH,'//input[@id="login-button"]')
button_login.click()
print('click login Button')
warring_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print('goog test')
driver.refresh()
