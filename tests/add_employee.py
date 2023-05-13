# Homework:
# 1: login
# 2: click Add button, to add a new employee
# 3: enter required data
# 4: save employee id
# 5: click save
# 6: ensure new employee was created
# 7: perform search for the employee by the employee id, and ensure all data matches.
# Use WebDriverWait as needed
import unittest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.maximize_window()
        browser.get("http://hrm-online.portnov.com/")
        self.browser = browser
        wait = WebDriverWait(browser, 5)
        self.wait = wait

    def tearDown(self) -> None:
        browser = self.browser
        browser.quit()

    def test_addEmployee(self):
        username = "admin"
        password = "password"
        login_message = "Welcome Admin"
        first_name = "Antony"
        last_name = "Moor"

        browser = self.browser
        wait = self.wait
        browser.find_element(By.ID, "logInPanelHeading").is_displayed()
        browser.find_element(By.ID, "txtUsername").send_keys(username)
        browser.find_element(By.ID, "txtPassword").send_keys(password)
        browser.find_element(By.ID, "btnLogin").click()
        wait.until(expected_conditions.text_to_be_present_in_element((By.ID, "welcome"), login_message))

        browser.find_element(By.ID, "btnAdd").click()
        wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#content h1"), "Add Employee"))
        browser.find_element(By.ID, "firstName").send_keys(first_name)  # TODO use faker
        browser.find_element(By.ID, "lastName").send_keys(last_name)  # TODO use faker
        browser.find_element(By.ID, "btnSave").click()
        wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#profile-pic h1"), f'{first_name} {last_name}'))
        emp_id = browser.find_element(By.ID, "personal_txtEmployeeId").get_attribute('value')

        browser.find_element(By.ID, "menu_pim_viewPimModule").click()
        wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#employee-information h1"), "Employee Information"))
        browser.find_element(By.ID, "empsearch_id").click()
        browser.find_element(By.ID, "empsearch_id").send_keys(emp_id)
        wait.until(expected_conditions.text_to_be_present_in_element_value((By.ID, "empsearch_id"), emp_id))
        browser.find_element(By.ID, "searchBtn").click()
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#resultTable tbody')))
        results_first_name = browser.find_element(By.XPATH, "//table[@id='resultTable']//td[3]/a").text
        results_last_name = browser.find_element(By.XPATH, "//table[@id='resultTable']//td[4]/a").text
        self.assertEqual(first_name, results_first_name)
        self.assertEqual(last_name, results_last_name)


if __name__ == '__main__':
    unittest.main()
