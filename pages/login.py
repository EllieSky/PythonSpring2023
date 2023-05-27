from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from tests import BASE_URL


class LoginPage(BasePage):

    PAGE_URL = f'{BASE_URL}/auth/login'
    HEADER ='LOGIN Panel'

    page_header = (By.ID, 'logInPanelHeading')

    def login(self, user='admin', password='password'):
        self.browser.find_element(By.ID, 'txtUsername').send_keys(user)
        self.browser.find_element(By.ID, 'txtPassword').send_keys(password)
        self.browser.find_element(By.ID, 'btnLogin').click()

    def logout(self):
        current_url = self.browser.current_url
        self.browser.find_element(By.ID, 'welcome').click()
        wait = WebDriverWait(self.browser, 3)
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.LINK_TEXT, 'Logout'))).click()
        wait.until(expected_conditions.url_changes(current_url),
                   'url failed to change after logout was clicked')