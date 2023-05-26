import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    def test_search_by_job_title(self):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')
        browser.find_element(By.ID, 'btnLogin').click()

        self.assertIn('/pim/viewEmployeeList', browser.current_url)

        welcome_message = browser.find_element(By.ID, 'welcome').text
        self.assertEqual('Welcome Admin', welcome_message)  # add assertion here

        browser.find_element(By.ID, 'empsearch_job_title').click()
        browser.find_element(By.CSS_SELECTOR, '#empsearch_job_title > option:nth-child(8)').click()

        browser.find_element(By.ID, 'searchBtn').click()

        time.sleep(2)

        all_job_title_values = browser.find_elements(By.CSS_SELECTOR, '#resultTable tr>td:nth-child(5)')

        for job_title in all_job_title_values:
            self.assertEqual('QA Manager', job_title.text)

        browser.find_element(By.ID, 'welcome').click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT, 'Logout').click()

        self.assertIn('/auth/login', browser.current_url)








    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser

    def tearDown(self) -> None:
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
