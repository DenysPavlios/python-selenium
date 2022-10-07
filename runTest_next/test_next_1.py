import pytest

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com')

    def test_02(self):
        driver = self.driver
        input_fild = driver.find_element(By.XPATH, '//input[@type="text"]')
        input_fild.send_keys('python')
        input_fild.send_keys(Keys.ENTER)

        assert 'python' in driver.page_source
        print('test_Next_2_Прошел успешно')


if __name__ == '__main__':
    unittest.main()
