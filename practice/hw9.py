import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import math

first_names_from_page = []


def login(browser):
    browser.find_element(By.ID, 'txtUsername').send_keys('admin')
    browser.find_element(By.ID, 'txtPassword').send_keys('password')
    browser.find_element(By.ID, 'btnLogin').click()


# function to get names from table on a page
def get_names_from_page(browser):
    first_name_elements = browser.find_elements(By.CSS_SELECTOR, '#resultTable td:nth-child(3)')
    for element in first_name_elements:
        first_names_from_page.append(element.text)


class Alphabetize(unittest.TestCase):
    def setUp(self):
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser

    # function to verify list from table is alphabetized
    def test_verify_alphabetization(self):
        browser = self.browser
        login(browser)

        # sort table column and wait for all sorted elements to be present
        browser.find_element(By.XPATH, "//th/a[contains(text(),'First')]").click()
        WebDriverWait(browser,2).until(
            expected_conditions.presence_of_all_elements_located((
                By.CSS_SELECTOR, '#resultTable td:nth-child(3)'
            ))
        )

        # get total number of pages
        pagination_text = browser.find_element(By.CSS_SELECTOR, '.desc').text.split()
        total_names_count = int(pagination_text[2])
        first_page_names_count = int(pagination_text[0].split('-')[1])
        num_of_pages = math.ceil(total_names_count/first_page_names_count)

        # get names from a page and check if it is the last page
        for num in range(1,num_of_pages+1):
            get_names_from_page(browser)
            if num != num_of_pages:
                browser.find_element(By.XPATH, "//a[text()='Next'][1]").click()

        # verify names from table are alphabetized
        alphabetized_list = first_names_from_page.copy()
        alphabetized_list.sort()

        assert alphabetized_list == first_names_from_page


if __name__ == '__main__':
    unittest.main()
