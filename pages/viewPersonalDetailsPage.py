from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import BASE_URL


class ViewPersonalDetailsPage(BasePage):
    PAGE_URL = f"{BASE_URL}/pim/viewPersonalDetails/empNumber/" #emp_id at the end
    HEADER = "Personal Details"

    first = (By.XPATH, '//input[@id = "personal_txtEmpFirstName"]')
    last = (By.XPATH, '//input[@id = "personal_txtEmpLastName"]')
    id = (By.XPATH, '//input[@id = "personal_txtEmployeeId"]')

    def get_user_details(self):
        """returning tuple with default user details """
        browser = self.browser
        first = browser.find_element(*self.first).get_attribute('value')
        last = browser.find_element(*self.last).get_attribute('value')
        id = browser.find_element(*self.id).get_attribute('value')
        user_info = [first, last, id]

        return user_info



