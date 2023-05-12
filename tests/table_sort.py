import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from fixtures.base_fixture import AdminLoginFixture


class TableSort(AdminLoginFixture):

    def test_sort_by_first_middle_name(self):
        browser = self.browser
        browser.find_element(By.XPATH, '//*[@id="resultTable"]/thead/tr/th[3]/a').click()

        self.wait.until(expected_conditions.url_contains('sortField=firstMiddleName&sortOrder=ASC'))

        previous_name = ''
        last_page = False
        while not last_page:
            list_of_names = browser.find_elements(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[3]/a')

            for name in list_of_names:
                self.assertLessEqual(previous_name, name.text.lower())
                previous_name = name.text.lower()

            pagination = browser.find_elements(By.CLASS_NAME, 'desc')
            # []
            # [WebElement, WebElement]
            if not pagination or pagination[0].text.split(' ')[-1] in pagination[0].text.split(' ')[0]:
                last_page = True
            else:
                browser.find_element(By.LINK_TEXT, 'Next').click()



if __name__ == '__main__':
    unittest.main()
