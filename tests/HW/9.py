import unittest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser
    def test_sorted_employee_list(self):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')
        browser.find_element(By.ID, 'btnLogin').click()
        browser.find_element(By.CSS_SELECTOR,  "#menu_pim_viewPimModule").click()
        browser.find_element(By.CSS_SELECTOR, '#resultTable > thead > tr > th:nth-child(3) > a').click()
        wait = WebDriverWait(browser,3)
        wait.until(
            expected_conditions.url_contains('index.php/pim/viewEmployeeList?sortField=firstMiddleName&sortOrder=ASC'))
        employee_list = browser.find_element(By.XPATH, "//tbody/tr/td[3]")
        employee_list = []
        emp = employee_list
        self.assertEqual(emp, sorted(emp))

    def test_employee_list(self):
            browser = self.browser
            browser.find_element(By.ID, 'txtUsername').send_keys('admin')
            browser.find_element(By.ID, 'txtPassword').send_keys('password')
            browser.find_element(By.ID, 'btnLogin').click()
            browser.find_element(By.CSS_SELECTOR, "#menu_pim_viewPimModule").click()
            browser.find_element(By.CSS_SELECTOR, '#resultTable > thead > tr > th:nth-child(3) > a').click()
            wait = WebDriverWait(browser, 3)
            wait.until(expected_conditions.url_contains(
                    '/viewEmployeeList?sortField=firstMiddleName&sortOrder=ASC'))
            employee_list = browser.find_element(By.XPATH, "//tbody/tr/td[3]")
            employee_list = []
            emp = employee_list
            if emp == sorted(emp):
                browser.find_element(By.XPATH, '//*[@id="frmList_ohrmListComponent"]/div[1]/ul/li[6]/a').click()
                wait = WebDriverWait(browser, 3)
                wait.until(expected_conditions.url_contains(
                    'index.php/pim/viewEmployeeList'))
                employee_list2 = browser.find_element(By.XPATH, "//tbody/tr/td[3]")
                employee_list2 = []
                emp2 = employee_list2
                if emp2 == sorted(emp2):
                 self.assertEqual(emp2, sorted(emp2))