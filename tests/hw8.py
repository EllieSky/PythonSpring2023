import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class Hw8(unittest.TestCase):
    def setUp(self):
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser

    def test_filter(self):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')
        browser.find_element(By.ID, 'btnLogin').click()
        dropdown = Select(browser.find_element(By.CSS_SELECTOR, '#empsearch_job_title'))
        dropdown.select_by_visible_text('QA Manager')
        browser.find_element(By.CSS_SELECTOR, '#searchBtn').click()
        time.sleep(2)
        qa_locator_list = browser.find_elements(By.CSS_SELECTOR, '#resultTable tr td:nth-child(5)')
        for qa_locator in qa_locator_list:
            self.assertEqual(qa_locator.text, 'QA Manager')
        browser.find_element(By.XPATH, "//a[text()='Welcome Admin']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//a[text()='Logout']").click()
        assert browser.current_url == 'http://hrm-online.portnov.com/symfony/web/index.php/auth/login'






if __name__ == '__main__':
    unittest.main()
