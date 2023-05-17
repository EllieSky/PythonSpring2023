import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from fixtures.base_fixture import AdminLoginFixture


class AddEmployee(AdminLoginFixture):
    def test_add_employee_basic(self):
        self.emp_list.add_employee()
        self.add_emp.input_employee_info('Joe', 'Smith')
        empl_id =  self.add_emp.get_employee_id()
        self.add_emp.save()
        self.wait.until(expected_conditions.url_changes(self.add_emp.PAGE_URL))
        # optionally you can then verify the new page header

        self.emp_list.goto_page()
        self.emp_list.search_by_employee_id(empl_id)
        # result = self.emp_list.get_table_row_data(1)

        self.assertEqual(empl_id, self.browser.find_element(By.XPATH, '//tbody/tr[1]/td[2]/a').text)
        self.assertEqual('Joe', self.browser.find_element(By.XPATH, '//tbody/tr[1]/td[3]/a').text)
        self.assertEqual('Smith', self.browser.find_element(By.XPATH, '//tbody/tr[1]/td[4]/a').text)



if __name__ == '__main__':
    unittest.main()
