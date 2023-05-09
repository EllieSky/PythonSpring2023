"""
login to HRM
click "First(& Middle) Name" table header
verify table is sorted in alphabetical order by that column on all pages
* names can be case-sensitive
* check pagination if exists
Hints:
- pagination shows 50-75 of 75
- wait for elements between pages

bonus: finish converting hm8 into POM
"""
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
wait = WebDriverWait(browser, 5)


def login(self, message, username='admin', password='password'):
    browser.find_element(By.ID, "logInPanelHeading").is_displayed()
    browser.find_element(By.ID, "txtUsername").send_keys(username)
    browser.find_element(By.ID, "txtPassword").send_keys(password)
    browser.find_element(By.ID, "btnLogin").click()
    wait.until(expected_conditions.visibility_of(browser.find_element(By.XPATH, "//a[@id='menu_pim_viewPimModule']"
                                                                                "/b[text()='PIM']")))
    self.assertEqual(get_greeting(), message)


def get_greeting():
    return browser.find_element(By.ID, "welcome").text


def sort_table(header):
    browser.find_element(By.XPATH, f'(//table[@id="resultTable"]//th)[{header}]').click()
    wait.until(expected_conditions.visibility_of(browser.find_element(By.XPATH, "//table[@id='resultTable']/tbody"
                                                                                "//tr[1]")))


def verify_results(self, header):
    verify_page_results(self, header)
    pagination = browser.find_element(By.XPATH, "//ul[contains(@class, 'paging')]")
    if pagination.is_displayed():
        description = browser.find_element(By.XPATH, "//ul[contains(@class, 'paging')]//li[@class='desc']").text
        page = description.split(' ')[0].split('-')[-1]
        pages = description.split(' ')[-1]
        if page != pages:
            browser.find_element(By.XPATH, "//ul[contains(@class, 'paging')]//li[@class='next']/a").click()
            verify_results(self, header)


def verify_page_results(self, header):
    wait.until(expected_conditions.visibility_of(browser.find_element(By.XPATH, "//table[@id='resultTable']//tbody"
                                                                                "//td")))
    elements = browser.find_elements(By.XPATH, f'//table[@id="resultTable"]//tbody//td[{header}]')
    list_elements = []
    for element in elements:
        list_elements.append(element.text.lower())
    for i in range(0, len(list_elements) - 1):
        self.assertTrue(list_elements[i] <= list_elements[i + 1], f'element {list_elements[i]} is not smaller or equal'
                                                                  f' to {list_elements[i + 1]}')


class Hh9Sort(unittest.TestCase):
    def setUp(self) -> None:
        browser.maximize_window()
        browser.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        browser.quit()

    def test_sort_by_first_name(self):
        username = "admin"
        password = "password"
        message = "Welcome Admin"

        login(self, message, username, password)
        sort_table(3)
        verify_results(self, 3)


if __name__ == '__main__':
    unittest.main()
