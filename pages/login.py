from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from tests import BASE_URL


class LoginPage(BasePage):

    PAGE_URL = f'{BASE_URL}/auth/login'
    HEADER =
    page_header =

    def login(self, user='admin', password='password'):
        self.browser.find_element(By.ID, 'txtUsername').send_keys(user)
        self.browser.find_element(By.ID, 'txtPassword').send_keys(password)
        self.browser.find_element(By.ID, 'btnLogin').click()