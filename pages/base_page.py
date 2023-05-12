from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(browser, 3)