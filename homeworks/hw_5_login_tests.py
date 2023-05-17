import unittest
from unittest import skip

from parameterized import parameterized
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

    @skip('not homework; worked out in class')
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

    @skip('not homework; worked out in class')
    def test_valid_login_welcome(self):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')

        browser.find_element(By.ID, 'btnLogin').click()

        actual_welcome = browser.find_element(By.ID, 'welcome').text
        expected_welcome = 'Welcome Admin'

        self.assertEqual(actual_welcome, expected_welcome)

        browser.quit()

    @parameterized.expand([
        (
            'empty credentials',
            ('', ''),
            '/auth/login',
            'Username cannot be empty'
        ),
        (
            'empty username',
            ('', 'password'),
            '/auth/login',
            'Username cannot be empty'
        ),
        (
            'empty password',
            ('admin', ''),
            '/auth/login',
            'Password cannot be empty'
        ),
        (
            'password case',
            ('admin', 'Password'),
            '/auth/validateCredentials',
            'Invalid credentials'
        ),
    ])
    def test_invalid_login(self, test_name, credentials: tuple, expected_url, expected_message):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys(credentials[0])
        browser.find_element(By.ID, 'txtPassword').send_keys(credentials[1])

        browser.find_element(By.ID, 'btnLogin').click()
        url_correct = expected_url in browser.current_url
        error_message = browser.find_element(By.ID, 'spanMessage').text
        self.assertTrue(url_correct and error_message == expected_message)

        browser.quit()



if __name__ == '__main__':
    unittest.main()
