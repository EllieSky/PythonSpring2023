import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage
from pages.view_emp_list import ViewEmployeeListPage


def login(browser, user='admin', password='password'):
    browser.find_element(By.ID, 'txtUsername').send_keys(user)
    browser.find_element(By.ID, 'txtPassword').send_keys(password)
    browser.find_element(By.ID, 'btnLogin').click()

def get_greeting(browser):
    return browser.find_element(By.ID, 'welcome').text

def search_by_job_title(browser, job_title):
    Select(browser.find_element(By.ID, 'empsearch_job_title')
           ).select_by_visible_text(job_title)
    browser.find_element(By.ID, 'searchBtn').click()

    wait = WebDriverWait(browser, 3)
    wait.until(expected_conditions.element_located_to_be_selected(
        [By.XPATH, f'//select[@id="empsearch_job_title"]/option[text()="{job_title}"]']))

class MyTestCase(unittest.TestCase):
    def test_search_by_job_title(self):
        browser = self.browser

        # login
        self.sign_in.login()

        self.assertIn('/pim/viewEmployeeList', browser.current_url)

        # get the greeting message
        welcome_message = get_greeting(browser)
        self.assertEqual('Welcome Admin', welcome_message)  # add assertion here

        # search/filter by job title
        emp_list = ViewEmployeeListPage(browser).search_by_job_title('QA Manager')

        # get resulting table data
        all_job_title_values = browser.find_elements(By.CSS_SELECTOR, '#resultTable tr>td:nth-child(5)')

        for job_title in all_job_title_values:
            self.assertEqual('QA Manager', job_title.text)

        # logout
        browser.find_element(By.ID, 'welcome').click()
        wait = WebDriverWait(browser, 3)
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.LINK_TEXT, 'Logout'))).click()
        # browser.find_element(By.LINK_TEXT, 'Logout').click()

        self.assertIn('/auth/login', browser.current_url)

    def test_search_by_name(self):
        self.sign_in.login()
        self.emp_list.search_by_name('Jo')
        all_fname_values = get_table_data(self.browser,3)
        all_lname_values = get_table_data(self.browser, 4)

        num_rows = len(all_fname_values)
        for i in range()
            self.assertIn('Jo', )
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