import time
import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def login(browser, user='admin', password='password'):
    browser.find_element(By.ID, 'txtUsername').send_keys(user)
    browser.find_element(By.ID, 'txtPassword').send_keys(password)
    browser.find_element(By.ID, 'btnLogin').click()


def get_greeting(browser):
    return browser.find_element(By.ID, 'welcome').text


def search_by_job_title(browser, job_title):
    Select(browser.find_element(By.ID, '#empsearch_job_title')
           ).select_by_visible_text(job_title)
    browser.find_element(By.CSS_SELECTOR, '#searchBtn').click()
    wait = WebDriverWait(browser, 3)
    wait.until(expected_conditions.element_located_to_be_selected(
        (By.CSS_SELECTOR, f'//select[@id="empsearch_job_title"/option[text()={job_title}]')))




class LoginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser

    def test_find_qa_manager(self):
        browser = self.browser

        # login
        login(browser)

        self.assertIn('/pim/viewEmployeeList', browser.current_url)

        # get the greeting message
        welcome_message = get_greeting(browser)
        self.assertEqual('Welcome Admin', welcome_message)

        # search/filter by job title
        search_by_job_title(browser, 'QA Manager')

        self.assertIn('/pim/viewEmployeeList', browser.current_url)

        # get resulting table data
        all_job_title_values = browser.find_elements(By.CSS_SELECTOR, '#resultTable tr>td:nth-child(5)')

        for job_title in all_job_title_values:
            self.assertEqual('QA Manager', job_title.text)

        # logout
        browser.find_element(By.ID, 'welcome').click()
        wait = WebDriverWait(browser, 3)
        wait.until(expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, 'Logout'))).click()
        # browser.find_element(By.XPATH, '//a[text()="Logout"]').click()
        self.assertIn('/auth/login', browser.current_url)


if __name__ == '__main__':
    unittest.main()
