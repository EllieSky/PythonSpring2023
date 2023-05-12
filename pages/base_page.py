from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests import BASE_URL


class BasePage:
    PAGE_URL = BASE_URL
    HEADER = ''
    page_header = (By.CSS_SELECTOR, '.head h1')

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(browser, 3)

    def goto_page(self):
        self.browser.get(self.PAGE_URL)

    def get_header(self):
        return self.browser.find_element(*self.page_header)


