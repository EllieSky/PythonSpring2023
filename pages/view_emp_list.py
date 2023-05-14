from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from tests import BASE_URL


class ViewEmployeeListPage(BasePage):
    PAGE_URL = f'{BASE_URL}/pim/viewEmployeeList'
    HEADER = 'Employee Information'

    header_view_employee_list_btn = (By.XPATH, '//a[@id = "menu_pim_viewEmployeeList"]')
    btn_search = (By.ID, 'searchBtn')
    select_job_title = (By.ID, 'empsearch_job_title')
    btn_add = (By.XPATH, '//input[@id = "btnAdd"]')


    def search_by_job_title(self, job_title):
        browser = self.browser
        Select(browser.find_element(*self.select_job_title)
               ).select_by_visible_text(job_title)
        browser.find_element(*self.btn_search).click()

        self.wait.until(expected_conditions.element_located_to_be_selected(
            [By.XPATH, f'//select[@id="{self.select_job_title[1]}"]/option[text()="{job_title}"]']))

    def search_by_name(self, name):
        browser = self.browser
        self.wait.until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint'))).send_keys(name)
        browser.find_element(*self.btn_search).click()
        self.wait.until(expected_conditions.presence_of_element_located(
            [By.CSS_SELECTOR, f'#empsearch_employee_name_empName[value="{name}"]']))


    def find_created_employee_by_id(self, user_id):
        browser = self.browser
        current_url = browser.current_url
        browser.find_element(*self.header_view_employee_list_btn).click()
        self.wait.until(expected_conditions.url_changes(current_url))
        rows = []
        results = browser.find_elements(By.XPATH, "//tbody/tr/td[2]")
        for result in results:
            rows.append(result.text)

        i = 0
        while len(browser.find_elements(By.XPATH, f"//a[@class = 'current']/following::a[text() = 2 + {i}]")) > 0:
            browser.find_element(By.XPATH, f"//a[@class = 'current']/following::a[text() = 2 + {i}]").click()
            results = browser.find_elements(By.XPATH, "//tbody/tr/td[2]")
            for result in results:
                rows.append(result.text)
                i += 1
        count = 1
        for item in rows:
            if item == user_id:
                return True
            count += 1
        return False








    def delete_employee(self):
        # locate correct employee by name / lname / id
        # check / click checkbox
        # click delete
        pass

    def add_employee(self):
        # click the add button
        pass
