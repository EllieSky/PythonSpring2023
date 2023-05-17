import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import wait
from webdriver_manager.chrome import ChromeDriverManager


class LoginTestCase(unittest.TestCase):

    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

        # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # executable_path is the first positional argument of Service anyway

        browser.get('http://hrm-online.portnov.com')
        self.browser = browser

    def test_login_positive(self):
        browser = self.browser
        browser.find_element()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
