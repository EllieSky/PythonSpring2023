import time
import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser

    def test_find_qa_manager(self):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')
        browser.find_element(By.ID, 'btnLogin').click()

        self.assertIn('/pim/viewEmployeeList', browser.current_url)

        welcome_message = browser.find_element(By.ID, 'welcome').text
        self.assertEqual('Welcome Admin', welcome_message)

        browser.find_element(By.CSS_SELECTOR, '#empsearch_job_title option:nth-child(8)').click()
        browser.find_element(By.CSS_SELECTOR, '#searchBtn').click()
        time.sleep(1)

        self.assertIn('/pim/viewEmployeeList', browser.current_url)

        qa_managers = browser.find_elements(By.XPATH, '//td[text()="QA Manager"]')
        for i in qa_managers:
            job_title = i.text
            self.assertEqual('QA Manager', job_title)

        browser.find_element(By.ID, 'welcome').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//a[text()="Logout"]').click()
        time.sleep(1)
        self.assertIn('/auth/login', browser.current_url)


if __name__ == '__main__':
    unittest.main()
