import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage
from pages.view_emp_list import ViewEmployeeListPage


def get_greeting(browser):
    return browser.find_element(By.ID, 'welcome').text

def get_table_data(browser, num_column):
    return browser.find_elements(By.CSS_SELECTOR, f'#resultTable tr>td:nth-child({num_column})')

def logout(browser):
    current_url = browser.current_url
    browser.find_element(By.ID, 'welcome').click()
    wait = WebDriverWait(browser, 3)
    wait.until(
        expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, 'Logout'))).click()
    wait.until(expected_conditions.url_changes(current_url),
               'url failed to change after logout was clicked')

class MyTestCase(unittest.TestCase):
    def test_search_by_job_title(self):
        browser = self.browser

        # login
        self.sign_in.login()
        # login(browser)

        self.assertIn('/pim/viewEmployeeList', browser.current_url)

        # get the greeting message
        welcome_message = get_greeting(browser)
        self.assertEqual('Welcome Admin', welcome_message)  # add assertion here

        # search/filter by job title
        self.emp_list.search_by_job_title('QA Manager')
        # search_by_job_title(browser, 'QA Manager')


        # get resulting table data
        all_job_title_values = get_table_data(browser, 5)

        for job_title in all_job_title_values:
            self.assertEqual('QA Manager', job_title.text)

        # logout
        logout(browser)

        self.assertIn('/auth/login', browser.current_url)

    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser
        self.sign_in = LoginPage(browser)
        self.emp_list = ViewEmployeeListPage(browser)

    def tearDown(self) -> None:
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
