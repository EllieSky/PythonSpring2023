from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import BASE_URL


class AddEmployeePage(BasePage):
    PGE_URL = f"{BASE_URL}/pim/addEmployee"
    HEADER = "Add Employee"

    btn_submit = (By.XPATH, "//input[@type= 'button']")
    input_fname = (By.XPATH, "//input[@name= 'firstName']")
    input_lname = (By.XPATH, "//input[@name= 'lastName']")
    input_id = (By.XPATH, "//input[@name= 'employeeId']")

    def fill_form_and_submit(self, first, last):
        """returns list with expected user info submitted from previous page"""
        browser = self.browser
        browser.find_element(*self.input_fname).send_keys(first)
        browser.find_element(*self.input_lname).send_keys(last)
        new_user_id = browser.find_element(*self.input_id).get_attribute('value')
        browser.find_element(*self.btn_submit).click()
        user_info = [first, last, new_user_id]

        return user_info

