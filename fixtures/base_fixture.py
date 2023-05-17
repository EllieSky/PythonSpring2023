import os
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage
from pages.view_emp_list import ViewEmployeeListPage
from pages.add_employee import AddEmployeePage
from tests import PROJECT_DIR, OUTPUT_DIR


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
        output_folder_path = os.path.join(PROJECT_DIR, OUTPUT_DIR)
        if not os.path.exists(output_folder_path):
            os.mkdir(output_folder_path)

        pieces: list = self._outcome.result.current_test_id.split('.')
        screenshot_name = pieces.pop(-1)

        folder_path = output_folder_path
        for piece in pieces:
            folder_path = os.path.join(folder_path, piece)
            os.mkdir(folder_path)
        screenshot_path = os.path.join(folder_path, f'{screenshot_name}.png')
        self.browser.save_screenshot(screenshot_path)
        self.browser.quit()


class AdminLoginFixture(BaseFixture):
    def setUp(self) -> None:
        super().setUp()
        self.sign_in.login()