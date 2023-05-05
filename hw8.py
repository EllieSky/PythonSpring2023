import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser

    def test_login(self):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')
        browser.find_element(By.ID, 'btnLogin').click()
        self.assertIn('pim/viewEmployeeList', browser.current_url)
        welcome_message = browser.find_element(By.ID, 'welcome').text
        self.assertEqual('Welcome Admin', welcome_message)

    def test_HW9(self):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')
        browser.find_element(By.ID, 'btnLogin').click()
        browser.find_element(By.XPATH, "//label[text()='Job Title' ]/following::select/option[8]").click()
        browser.find_element(By.XPATH, "//input[@type='button']").click()
        time.sleep(2)
        browser.find_elements(By.XPATH, "//tr/td[5]")
        message = browser.find_element(By.XPATH, "//tr/td[text()='QA Manager']").text
        self.assertEqual('QA Manager', message)

if __name__ == '__main__':
    unittest.main()
