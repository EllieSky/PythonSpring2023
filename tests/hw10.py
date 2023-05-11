import unittest

import parameterized as parameterized
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def login(browser):
    browser.find_element(By.ID, 'txtUsername').send_keys('admin')
    browser.find_element(By.ID, 'txtPassword').send_keys('password')
    browser.find_element(By.ID, 'btnLogin').click()


class CreateEmployee(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser

    @parameterized.parameterized.expand([
        ('tom', 'test'),
        ('charlie', 'chaplin')
    ])
    def test_add_employee(self, fname, lname):
        browser = self.browser
        login(browser)
        browser.find_element(By.CSS_SELECTOR, '#btnAdd').click()
        browser.find_element(By.XPATH, "//input[@id='firstName']").send_keys(fname)
        browser.find_element(By.XPATH, "//input[@id='lastName']").send_keys(lname)
        emp_id = browser.find_element(By.XPATH, "//input[@id='employeeId']").get_attribute('value')
        browser.find_element(By.XPATH, "//input[@id='btnSave']").click()
        browser.find_element(By.XPATH, "//a[@id='menu_pim_viewEmployeeList']").click()
        browser.find_element(By.XPATH, "//input[@id ='empsearch_id']").send_keys(emp_id)
        browser.find_element(By.XPATH, "//input[@id ='searchBtn']").click()
        table_data_elements = browser.find_elements(By.XPATH, "//table[@id= 'resultTable']//td")
        table_data = []
        for element in table_data_elements:
            table_data.append(element.text)
        user_data_given = [emp_id, fname, lname]
        assert(set(user_data_given).issubset(set(table_data)))