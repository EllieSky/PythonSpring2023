from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.add_emp import AddEmployeePage
from pages.login import LoginPage
from pages.view_emp_list import ViewEmployeeListPage


class BaseFixture(TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

        self.browser = browser
        self.wait = WebDriverWait(self.browser, 6)

        self.sign_in = LoginPage(browser)
        self.emp_list = ViewEmployeeListPage(browser)
        self.add_emp = AddEmployeePage(browser)

        self.sign_in.goto_page()

    def tearDown(self) -> None:
        self.browser.quit()


class AdminLoginFixture(BaseFixture):
    def setUp(self) -> None:
        super().setUp()
        self.sign_in.login()