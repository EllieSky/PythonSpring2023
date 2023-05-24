import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.base_fixture import AdminLoginFixture
from tests import get_browser

# 1. Login to http://hrm-online.portnov.com/
# 2. In the top right corner click the green button "Join OrangeHRM Community"
# 3. Check the url of the new window
# 4. Close the window
# 5. Switch to original window
# 6. Logout

class HW13TestCase(AdminLoginFixture):
    def setUp(self) -> None:
        browser = get_browser()

        self.browser = browser
        self.wait = WebDriverWait(self.browser, 6)


    def tearDown(self) -> None:
        self.browser.quit()
    def test_something(self):
        browser = self.browser

        current_number_of_windows = len(browser.window_handles)

        browser.find_element(By.CLASS_NAME, 'subscribe').click()
        self.wait.until(EC.number_of_windows_to_be(current_number_of_windows + 1))

        original_window = browser.current_window_handle
        browser.switch_to.window(browser.window_handles[-1])

        self.assertIn('https://www.orangehrm.com/User_Survey_Registration', browser.current_url)

        browser.close()
        browser.switch_to.window(original_window)


if __name__ == '__main__':
    unittest.main()
