import os

from behave import *
from selenium.webdriver.support.wait import WebDriverWait

from lib.base_methods import BaseMethods
from menus.main import MainMenu
from pages.add_employee import AddEmployeePage
from pages.admin_localization import AdminLocalizationPage
from pages.login import LoginPage
from pages.view_emp_list import ViewEmployeeListPage
from tests import get_browser, DEFAULT_WAIT, DOMAIN, PROJECT_DIR, OUTPUT_BDD_DIR


# def before_all / after_all
# def before_feature(context, feature) / after_feature
# def before_scenario(context, scenario) / after_scenario
# def before_step(context, step) / after_step
# def before_tag(context, tag) / after_tag

def before_scenario(context, scenario):
    if "no-selenium" in scenario.effective_tags:
        return
    context.url = DOMAIN
    browser = get_browser()

    context.browser = browser
    context.wait = WebDriverWait(browser, DEFAULT_WAIT)
    context.base_methods = BaseMethods(context.browser)

    context.browser.get(context.url)

    context.main_menu = MainMenu(browser)

    context.sign_in = LoginPage(browser)
    context.employee_list = ViewEmployeeListPage(browser)
    context.add_employee = AddEmployeePage(browser)
    context.admin_localization = AdminLocalizationPage(browser)




def after_scenario(context, scenario):
    if "no-selenium" in scenario.effective_tags:
        return
    if context.failed:
        output_folder_path = os.path.join(PROJECT_DIR, OUTPUT_BDD_DIR)
        if not os.path.exists(output_folder_path):
            os.mkdir(output_folder_path)

        scenario_name = scenario.name.replace(' ', '_').lower()
        folder_path = os.path.join(output_folder_path, scenario_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)


        screenshot_path = os.path.join(folder_path, 'screenshot.png')
        context.browser.save_screenshot(screenshot_path)

        page_source = context.browser.page_source
        page_src_path = os.path.join(folder_path, 'page_source.html')
        file = open(page_src_path, 'w')
        file.write(page_source)
        file.close()

    context.browser.quit()