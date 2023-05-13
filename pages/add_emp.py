from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from tests import BASE_URL


class AddEmployeePage(BasePage):
    PAGE_URL = f'{BASE_URL}/pim/addEmployee'
    HEADER = 'Add Employee'

    def add_by_name(self, first_name, last_name):
        browser = self.browser
        wait = self.wait
        browser.find_element(By.ID, "firstName").send_keys(first_name)
        browser.find_element(By.ID, "lastName").send_keys(last_name)
        browser.find_element(By.ID, "btnSave").click()
        wait.until(expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#profile-pic h1"), f'{first_name} {last_name}'))
