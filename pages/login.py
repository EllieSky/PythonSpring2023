from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:

    def _init__(self,browser: WebDriver):
        self.browser = browser
    def login(self, user = 'admin', password = 'password'):
        self.browser.find_element(By.ID, 'txtUsername').send_keys(user)
        self.browser.find_element(By.ID, 'txtPassword').send_keys(password)
        self.browser.find_element(By.ID, 'btnLogin').click()


