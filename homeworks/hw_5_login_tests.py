import unittest
from unittest import skip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginTestCase(unittest.TestCase):

    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

        # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # 'executable_path=' can be omitted as above because
        # executable_path is the first positional argument of Service anyway

        browser.get('http://hrm-online.portnov.com')
        self.browser = browser

    def test_valid_login_landing_url(self):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')

        browser.find_element(By.ID, 'btnLogin').click()

        # to emulate "power user", who hits 'Enter' instead of clicking with a mouse
        # the question is, on which WebElement object should be called? the below works btw
        # browser.find_element(By.ID, 'txtPassword').submit()

        actual_url = browser.current_url
        expected_url_suffix = '/pim/viewEmployeeList'

        self.assertIn(expected_url_suffix, actual_url)

        browser.quit()

    def test_valid_login_welcome(self):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')

        browser.find_element(By.ID, 'btnLogin').click()

        actual_welcome = browser.find_element(By.ID, 'welcome').text
        expected_welcome = 'Welcome Admin'

        self.assertEqual(actual_welcome, expected_welcome)

        browser.quit()


if __name__ == '__main__':
    unittest.main()
