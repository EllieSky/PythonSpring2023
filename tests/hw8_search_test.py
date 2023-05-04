import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SearchTestCase(unittest.TestCase):

    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser


    def test_search(self, search_result=None):
        browser = self.browser
        browser.find_element(By.CSS_SELECTOR, "#txtUsername").send_keys("admin")
        browser.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys("password")
        browser.find_element(By.CSS_SELECTOR, '.button').click()
        self.assertIn("/pim/viewEmployeeList", browser.current_url)

        welcome_message = browser.find_element(By.ID, "welcome").text
        self.assertEqual('Welcome Admin', welcome_message)

        # Assertion that QA Engineer role exists within the list
        content = browser.find_element(By.XPATH, "//option[text()='QA Manager']").text
        self.assertEqual("QA Manager", content)

        # Assertion that Part Time option is present
        employment_status = browser.find_element(By.XPATH, "//option[text()='Part Time']").text
        self.assertEqual("Part Time", employment_status)

        # Selecting both filters
        browser.find_element(By.XPATH, "//option[text()='QA Manager']").click()
        browser.find_element(By.XPATH, "//option[text()='Part Time']").click()

        browser.find_element(By.CSS_SELECTOR, "#searchBtn").click()

        time.sleep(2)

        # Adding assertion for the result list for QA Manager with a Part Time Employment Status using the for loop.
        job_title = "QA Manager"
        job_type = "Part Time"
        search_result_list = browser.find_elements(By.XPATH, "//td[text()='QA Manager']")
        search_job_type = browser.find_elements(By.XPATH, "//td[text()='Part Time']")

        for qa_manager in search_result_list:
            print(qa_manager.text)
            if job_title == qa_manager.text:
                self.assertTrue(job_title, qa_manager)
            else:
                self.assertFalse(job_title, qa_manager)

        for part_time in search_job_type:
            print(part_time.text)
            if job_type == part_time.text:
                self.assertTrue(job_type, part_time)
            else:
                self.assertFalse(job_type, part_time)

        # Logging out of the account
        browser.find_element(By.CSS_SELECTOR, "#welcome").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "//a[text()='Logout']").click()
        time.sleep(1)
        self.assertIn("/index.php/auth/login", browser.current_url)




















if __name__ == '__main__':
    unittest.main()
