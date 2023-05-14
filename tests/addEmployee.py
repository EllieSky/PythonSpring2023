import unittest

from selenium.webdriver.support import expected_conditions

from fixtures.base_fixture import BaseFixture


class AddEmployee(BaseFixture):

    def test_create_user(self):
        browser = self.browser

        self.sign_in.login()
        self.wait.until(expected_conditions.url_contains(self.emp_list.PAGE_URL))

        browser.find_element(*self.emp_list.btn_add).click()
        self.wait.until(expected_conditions.url_contains(self.add_employee.PAGE_URL))

        emp_info_sent = self.add_employee.fill_form_and_submit("Sofi", "Naidina")
        self.wait.until(expected_conditions.url_contains(self.view_user.PAGE_URL))

        emp_info_recorded = self.view_user.get_user_details()

        self.assertEqual(emp_info_sent, emp_info_recorded)

        employee_exists_actual = self.emp_list.find_created_employee_by_id(emp_info_sent[2])
        employee_exists_expected  = True

        self.assertEqual(employee_exists_actual, employee_exists_expected)



