import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.base_fixture import BaseFixture


def get_greeting(browser):
    return browser.find_element(By.ID, 'welcome').text

def get_table_data(browser, num_column):
    return browser.find_elements(By.CSS_SELECTOR, f'#resultTable tr>td:nth-child({num_column})')

def logout(browser):
    current_url = browser.current_url
    browser.find_element(By.ID, 'welcome').click()
    wait = WebDriverWait(browser, 3)
    wait.until(
        expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, 'Logout'))).click()
    wait.until(expected_conditions.url_changes(current_url),
               'url failed to change after logout was clicked')

class MyTestCase(BaseFixture):
    def test_search_by_job_title(self):
        browser = self.browser

        # login
        self.sign_in.login()
        # login(browser)

        self.assertIn(self.emp_list.PAGE_URL, browser.current_url)

        # get the greeting message
        welcome_message = get_greeting(browser)
        self.assertEqual('Welcome Admin', welcome_message)  # add assertion here

        # search/filter by job title
        self.emp_list.search_by_job_title('QA Manager')
        # search_by_job_title(browser, 'QA Manager')


        # get resulting table data
        all_job_title_values = get_table_data(browser, 5)

        for job_title in all_job_title_values:
            self.assertEqual('QA Manager', job_title.text)

        # logout
        logout(browser)

        self.assertIn('/auth/login', browser.current_url)

    def test_search_by_name(self):
        self.sign_in.login()
        self.emp_list.search_by_name('Jo')
        all_fname_values = get_table_data(self.browser, 3)
        all_lname_values = get_table_data(self.browser, 4)

        num_rows = len(all_fname_values)
        for i in range(num_rows):
            self.assertIn('Jo', f'{all_fname_values[i].text} {all_lname_values[i].text}')







if __name__ == '__main__':
    unittest.main()