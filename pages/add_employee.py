from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from tests import BASE_URL


class AddEmployeePage(BasePage):
    PAGE_URL = f'{BASE_URL}/pim/addEmployee'
    HEADER = 'Add Employee'

    btn_save = (By.ID, 'btnSave')

    def input_employee_info(self, first_name, last_name, middle_name=None, emp_id=None):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, 'firstName'))).send_keys(first_name)
        self.browser.find_element(By.ID, 'lastName').send_keys(last_name)
        if middle_name:
            self.browser.find_element(By.ID, 'middleName').send_keys(middle_name)
        if emp_id is not None:
            fld_emp_id = self.browser.find_element(By.ID, 'employeeId')
            fld_emp_id.clear()
            fld_emp_id.send_keys(emp_id)

    def get_employee_id(self):
        return self.wait.until(expected_conditions.presence_of_element_located((By.ID, 'employeeId'))).get_attribute('value')

    def save(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.btn_save)).click()
