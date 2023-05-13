import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class EmployeeList(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser
    def test_employee_list(self):
        browser = self.browser
        browser.find_element(By.CSS_SELECTOR, '#txtUsername').send_keys('admin')
        browser.find_element(By.CSS_SELECTOR, '#txtPassword').send_keys('password')
        browser.find_element(By.CSS_SELECTOR, '#btnLogin').click()
        self.assertIn('/pim/viewEmployeeList', browser.current_url)
        time.sleep(1)
        welcome_message = browser.find_element(By.ID, 'welcome').text
        self.assertEqual('Welcome Admin', welcome_message)

        browser.find_element(By.XPATH, "//select[@id='empsearch_job_title']").click()
        time.sleep(1)
        job_title_qa = browser.find_element(By.XPATH, '//option[text()="QA Manager"]').text
        self.assertEqual('QA Manager', job_title_qa)

        browser.find_element(By.XPATH, '//option[text()="QA Manager"]').click()
        browser.find_element(By.XPATH, '//input[@id="searchBtn"]').click()
        time.sleep(2)

        job_title_result = browser.find_elements(By.XPATH, '//td[text()="QA Manager"]')
        for i in job_title_result:
            job_title = i.text
            print(f'Job Title only: {job_title}')
            self.assertEqual('QA Manager', job_title)

        time.sleep(1)

        browser.find_element(By.CSS_SELECTOR, '#empsearch_employee_status').click()
        employee_status = browser.find_element(By.XPATH, '//option[contains(text(),"Full")]').text
        self.assertEqual("Full Time", employee_status)

        browser.find_element(By.XPATH, '//option[contains(text(),"Full")]').click()
        browser.find_element(By.XPATH, '//input[@id="searchBtn"]').click()
        time.sleep(2)

        job_title_result = browser.find_elements(By.XPATH, '//td[text()="QA Manager"]')
        for i in job_title_result:
            job_title = i.text
            self.assertEqual('QA Manager', job_title)

        employee_status_result = browser.find_elements(By.XPATH, '//td[text()="Full Time"]')
        for n in employee_status_result:
            status = n.text
            print(f'Job Title: "{job_title}" and Employee Status: "{status}"')
            self.assertEqual('Full Time', status)

        time.sleep(1)

        browser.find_element(By.ID, 'welcome').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '//a[text()="Logout"]').click()
        time.sleep(2)
        self.assertIn('/auth/login', browser.current_url)


if __name__ == '__main__':
    unittest.main()
