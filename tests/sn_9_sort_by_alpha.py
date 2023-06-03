import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tests.search_employee import login


# functions
def get_data_from_table(browser, get_column):
    """selecting conumn and saving value from each row into the list, returns list"""
    data_list = []
    column_with_data = browser.find_elements(By.XPATH, get_column)  # locator for name column "//tbody//tr//td[3]"

    for row in column_with_data:
        data_list.append(row.text)

    return data_list

def get_rest_of_data(browser, list):
    """finding next page locator, if exists -> gets values, goes to the next, returns extended list"""
    next_page_button = f"//a[@class = 'current']/following::a[text() = 2]"
    get_button = browser.find_elements(By.XPATH, next_page_button)
    go = len(get_button) > 0
    path = next_page_button
    i = 0
    while go:
        browser.find_element(By.XPATH, path).click()
        list.extend(get_data_from_table(browser, "//tbody//tr//td[3]"))
        i += 1
        another_page_button = f"//a[@class = 'current']/following::a[text() = {2 + i}]"
        get_button = browser.find_elements(By.XPATH, another_page_button)
        go = len(get_button) > 0
        path = another_page_button

    return list


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser

    def tearDown(self) -> None:
        self.browser.quit()

    # test
    def test_if_table_is_sorted(self):

        browser = self.browser
        browser_wait = WebDriverWait(browser, 3)
        error = "Error: results do not mach"

        login(browser)
        self.assertIn("viewEmployeeList", browser.current_url, error)

        #get unsorted results and sort them
        expected = sorted(get_rest_of_data(browser,get_data_from_table(browser, "//tbody//tr//td[3]")), key=str.lower)

        current_url = browser.current_url
        browser.find_element(By.XPATH, "//a[contains(text(),'First (& Middle) Name')]").click()
        WebDriverWait(browser, 3).until(
                expected_conditions.url_changes(current_url))

        #get ready sorted results from the web
        actual = get_rest_of_data(browser,get_data_from_table(browser, "//tbody//tr//td[3]"))

        #compare sorted raw data vs sorted results from web
        self.assertEqual(expected, actual, error)
