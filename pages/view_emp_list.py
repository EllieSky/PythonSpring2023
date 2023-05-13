from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from tests import BASE_URL


class ViewEmployeeListPage(BasePage):
    PAGE_URL = f'{BASE_URL}/pim/viewEmployeeList'
    HEADER = 'Employee Information'

    btn_search = (By.ID, 'searchBtn')
    select_job_title = (By.ID, 'empsearch_job_title')

    def search_by_job_title(self, job_title):
        browser = self.browser
        Select(browser.find_element(*self.select_job_title)
               ).select_by_visible_text(job_title)
        browser.find_element(*self.btn_search).click()

        self.wait.until(expected_conditions.element_located_to_be_selected(
            [By.XPATH, f'//select[@id="{self.select_job_title[1]}"]/option[text()="{job_title}"]']))

    def search_by_name(self, name):
        browser = self.browser
        self.wait.until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint'))).send_keys(name)
        browser.find_element(*self.btn_search).click()
        self.wait.until(expected_conditions.presence_of_element_located(
            [By.CSS_SELECTOR, f'#empsearch_employee_name_empName[value="{name}"]']))

    def search_by_id(self, emp_id):
        browser = self.browser
        self.wait.until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, '#empsearch_id'))).click()
        browser.find_element(By.ID, "empsearch_id").send_keys(emp_id)
        self.wait.until(expected_conditions.text_to_be_present_in_element_value((By.ID, "empsearch_id"), emp_id))
        browser.find_element(By.ID, "searchBtn").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#resultTable tbody')))

    def delete_employee(self):
        # locate correct employee by name / lname / id
        # check / click checkbox
        # click delete
        pass

    def add_employee(self):
        # click the add button
        pass
