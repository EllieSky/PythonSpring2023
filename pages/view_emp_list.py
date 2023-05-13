from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class ViewEmployeeListPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
    def search_by_job_title(self, job_title):
        browser = self.browser
        Select(browser.find_element(By.ID, 'empsearch_job_title')).select_by_visible_text(job_title)
        browser.find_element(By.ID, 'searchBtn').click()

        wait = WebDriverWait(browser, 3)
        wait.until(expected_conditions.element_located_to_be_selected([By.XPATH, f'//select[@id="empsearch_job_title"]/option[text()="{job_title}"]']))

    def delete_employee(self):
        browser = self.browser
        #find employee
        #check box next to employee we want to delete
        #click delete button
        pass

    def add_employee(self):
        browser = self.browser
        # click the add button
        pass

    def search_by_name(self, name):
        browser = self.browser
        browser.find_element(By.ID, 'empsearch_employee_name_empName').send_keys(name)
        browser.find_element(By.ID, 'searchBtn').click()
        wait = WebDriverWait(browser,3)
        wait.until(expected_conditions.presence_of_element_located([By.CSS_SELECTOR, f'#empsearch_employee_name_empName[value="{name}"']))
        pass