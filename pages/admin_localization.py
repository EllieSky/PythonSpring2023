from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from tests import BASE_URL


class AdminLocalizationPage(BasePage):
    PAGE_URL = f'{BASE_URL}/admin/localization'
    HEADER = 'Localization'

    btn_save = (By.ID, 'btnSave')
    btn_edit = btn_save

    def save(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.btn_save)).click()

    def edit(self):
        self.save()
