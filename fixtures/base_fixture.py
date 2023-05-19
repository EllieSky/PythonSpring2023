import os
from unittest import TestCase

from selenium.webdriver.support.wait import WebDriverWait

from pages.add_employee import AddEmployeePage
from pages.login import LoginPage
from pages.view_emp_list import ViewEmployeeListPage
from tests import PROJECT_DIR, OUTPUT_DIR, get_browser


class BaseFixture(TestCase):
    def setUp(self) -> None:
        browser = get_browser()

        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

        self.sign_in = LoginPage(browser)
        self.emp_list = ViewEmployeeListPage(browser)
        self.add_emp = AddEmployeePage(browser)

        self.sign_in.goto_page()

    def tearDown(self) -> None:

        if (hasattr(self._outcome,'errors') and self._outcome.errors[1][1]
        ) or (self._outcome.result.failures and self._outcome.result.failures[0][1]):
            output_folder_path = os.path.join(PROJECT_DIR, OUTPUT_DIR)
            if not os.path.exists(output_folder_path):
                os.mkdir(output_folder_path)

            pieces: list = self._outcome.result.current_test_id.split('.')
            screenshot_name = pieces.pop(-1)

            folder_path = output_folder_path
            for piece in pieces:
                folder_path = os.path.join(folder_path, piece)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
            screenshot_path = os.path.join(folder_path, f'{screenshot_name}.png')
            self.browser.save_screenshot(screenshot_path)

            page_source = self.browser.page_source
            page_src_path = os.path.join(folder_path, f'{screenshot_name}.html')
            file = open(page_src_path, 'w')
            file.write(page_source)
            file.close()

        self.browser.quit()

class AdminLoginFixture(BaseFixture):
    def setUp(self) -> None:
        super().setUp()
        self.sign_in.login()