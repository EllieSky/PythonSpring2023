import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.base_fixture import AdminLoginFixture


class MyTestCase(AdminLoginFixture):
    def test_open_localization_using_menu(self):
        browser = self.browser
        actions = ActionChains(self.browser)

        actions.move_to_element(self.wait.until(EC.visibility_of_element_located((By.ID, 'menu_admin_viewAdminModule'))))
        actions.move_to_element(self.wait.until(EC.visibility_of_element_located((By.ID, 'menu_admin_UserManagement'))))
        actions.move_to_element(self.wait.until(EC.visibility_of_element_located((By.ID, 'menu_admin_Configuration'))))
        actions.click(self.wait.until(EC.element_to_be_clickable((By.ID, 'menu_admin_localization'))))
        actions.perform()
        # actions.reset_actions()

        page_header = browser.find_element(By.CSS_SELECTOR, '.head>h1').text

if __name__ == '__main__':
    unittest.main()
