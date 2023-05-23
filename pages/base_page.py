from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.base_methods import BaseMethods
from tests import BASE_URL, DEFAULT_WAIT


class BasePage(BaseMethods):
    PAGE_URL = BASE_URL
    HEADER = ''

    page_header = (By.CSS_SELECTOR, '.head h1')

    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.browser = browser
        self.wait = WebDriverWait(browser, DEFAULT_WAIT)

    def goto_page(self):
        self.browser.get(self.PAGE_URL)

    def get_header(self):
        return self.browser.find_element(*self.page_header).text