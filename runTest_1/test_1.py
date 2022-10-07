import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test():

    def __init__(self):
        self.login = 'standard_user'
        self.passwordAll = 'secret_sauce'


    def setUp(self):
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')



        # driver = webdriver.Firefox(executable_path='/Users/mcden/Desktop/pythonPRO/python_selenium/geckodriver')


        user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
        print(user_name.is_displayed())
        print(user_name.is_enabled())

        user_name.send_keys(self.login)
        print('input login')
        pasword = driver.find_element(By.XPATH, '//input[@id="password"]')
        pasword.send_keys(self.passwordAll)
        print('input password')
        button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
        button_login.click()
        print('click login')
            # text_products = driver.find_element(By.XPATH,'//span[@class="title"]')
            # value_text_producrs = text_products.text
            # print(value_text_producrs)
            # assert value_text_producrs == 'PRODUCTS'
            # print('GOOD')
        url = 'https://www.saucedemo.com/inventory.html'
        get_url = driver.current_url
        print(get_url)
        assert url == get_url
        print('GOOD')


        driver.close()
        driver.quit()

run = Test()
run.setUp()


