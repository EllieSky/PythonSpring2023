import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage


class BaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        # browser.get('http://hrm-online.portnov.com/')
        self.browser = browser
        self.sign_in = LoginPage(browser)
        self.sign_in.goto_page()

    def tearDown(self) -> None:
        self.browser.quit()