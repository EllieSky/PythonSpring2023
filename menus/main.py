from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from lib.base_methods import BaseMethods


class MainMenu (BaseMethods):

    admin_viewAdmin = (By.ID, 'menu_admin_viewAdminModule')
    admin_userManagement = (By.ID, 'menu_admin_UserManagement')
    admin_configuration = (By.ID, 'menu_admin_Configuration')
    admin_localization = (By.ID, 'menu_admin_localization')

    pim_viewPim = (By.ID, 'menu_pim_viewPimModule')
    pim_viewMyDetails = (By.ID, 'menu_pim_viewMyDetails')



    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.action = ActionChains(browser)


    def view_pim(self):
        self.click_elem(self.pim_viewPim)

    def view_myDetails(self):
        self.click_elem(self.pim_viewMyDetails)

    def view_admin_localization(self):
        url = self.browser.current_url

        self.action.move_to_element(self.find_elem(self.admin_viewAdmin))
        self.action.move_to_element(self.find_elem(self.admin_userManagement))
        self.action.move_to_element(self.find_elem(self.admin_configuration))
        self.action.click(self.find_elem(self.admin_localization))
        self.action.perform()
        self.action.reset_actions()

        self.wait.until(EC.url_changes(url))