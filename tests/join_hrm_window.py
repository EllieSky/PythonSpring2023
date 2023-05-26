import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from fixtures.base_fixture import AdminLoginFixture
from pages import base_page, login


class WindowTest(AdminLoginFixture):
    def test_window(self):
        browser = self.browser
        wait = self.wait
        page = login.BASE_URL
        self.assertNotEqual(page, browser.current_url)  # add assertion here
        number_of_windows = len(browser.window_handles)
        original_window = browser.current_window_handle
        browser.find_element(By.XPATH, "//a[@class = 'subscribe']").click()
        self.wait.until(expected_conditions.number_of_windows_to_be(number_of_windows + 1))
        browser.switch_to.window(browser.window_handles[-1])
        self.assertIn("/User_Survey_Registration", browser.current_url)
        browser.close()
        browser.switch_to.window(original_window)
        url = browser.current_url
        browser.find_element(By.XPATH, "//a[@id = 'welcome']").click()
        wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@id = 'welcome-menu']/ul/li[2]/a"))).click()
        wait.until(expected_conditions.url_changes(url))
        self.assertIn(login.BASE_URL, browser.current_url)




if __name__ == '__main__':
    unittest.main()
