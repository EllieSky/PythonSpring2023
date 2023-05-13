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

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.base_fixture import BaseFixture
from tests.search_employee import get_greeting


def get_greeting(browser):
    return browser.find_element(By.ID, 'welcome').text


def logout(browser):
    current_url = browser.current_url
    browser.find_element(By.ID, 'welcome').click()
    wait = WebDriverWait(browser, 3)
    wait.until(
        expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, 'Logout'))).click()
    wait.until(expected_conditions.url_changes(current_url),
               'url failed to change after logout was clicked')


class MyTestCase(BaseFixture):
    def test_addEmployee(self):
        # TODO use faker
        first_name = "Antony"
        last_name = "Moor"

        browser = self.browser
        wait = self.wait

        self.sign_in.login()

        self.assertIn(self.emp_list.PAGE_URL, browser.current_url)
        welcome_message = get_greeting(browser)
        self.assertEqual('Welcome Admin', welcome_message)
        btn_add = browser.find_element(By.ID, "btnAdd")

        btn_add.click()
        wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#content h1"), "Add Employee"))
        self.add_emp.add_by_name(first_name, last_name)
        emp_id = browser.find_element(By.ID, "personal_txtEmployeeId").get_attribute('value')

        # TODO add 43-44 to navigateToPage
        browser.find_element(By.ID, "menu_pim_viewPimModule").click()
        wait.until(expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#employee-information h1"), "Employee Information"))

        self.emp_list.search_by_id(emp_id)
        results_first_name = browser.find_element(By.XPATH, "//table[@id='resultTable']//td[3]/a").text
        results_last_name = browser.find_element(By.XPATH, "//table[@id='resultTable']//td[4]/a").text
        self.assertEqual(first_name, results_first_name)
        self.assertEqual(last_name, results_last_name)

        logout(browser)
        self.assertIn('/auth/login', browser.current_url)


if __name__ == '__main__':
    unittest.main()
