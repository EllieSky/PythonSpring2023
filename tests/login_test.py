import unittest

from parameterized import parameterized
from selenium.webdriver.common.by import By

from fixtures.base_fixture import BaseFixture


class LoginTestCase(BaseFixture):
    def test_valid_login(self):
        browser = self.browser
        self.assertEqual(self.sign_in.HEADER, self.sign_in.get_header())

        self.sign_in.login()

        self.assertEqual(self.emp_list.PAGE_URL, browser.current_url)

        welcome_message = browser.find_element(By.ID, 'welcome').text
        self.assertEqual('Welcome Admin', welcome_message)  # add assertion here

    @parameterized.expand([
        ('no password','admin', '', '/auth/login', 'Password cannot be empty'),
        ('no username','', 'password', '/auth/login', 'Username cannot be empty'),
        ('bad password','admin', 'passW0rd', '/auth/validateCredentials', 'Invalid credentials'),
    ])
    def test_(self, test_name, username, password, url, expected_error_message):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys(username)
        browser.find_element(By.ID, 'txtPassword').send_keys(password)
        browser.find_element(By.ID, 'btnLogin').click()

        self.assertIn(url, browser.current_url)

        error_message = browser.find_element(By.ID, 'spanMessage').text
        self.assertEqual(expected_error_message, error_message)


if __name__ == '__main__':
    unittest.main()
















