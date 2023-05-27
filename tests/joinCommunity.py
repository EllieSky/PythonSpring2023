import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.base_fixture import AdminLoginFixture


class JoinCommunity(AdminLoginFixture):
    """
        1. Login to http://hrm-online.portnov.com/
        2. In the top right corner click the green button "Join OrangeHRM Community"
        3. Check the url of the new window
        4. Close the window
        5. Switch to original window
        6. Logout
    """
    def test_user_navigates_to_correct_url(self):
        browser = self.browser
        wait = self.wait

        join_community_button = browser.find_element(By.XPATH, '//div[@id="branding"]/a')
        community_url = "https://www.orangehrm.com/User_Survey_Registration"
        original_window = browser.current_window_handle
        join_community_button.click()
        browser.switch_to.window(browser.window_handles[-1])
        community_footer_item = By.XPATH, '//div[@class="footer-main-section"]//h5[text()="Policies"]'
        wait.until(EC.visibility_of_element_located(community_footer_item))
        self.assertEqual(community_url, browser.current_url)
        browser.close()
        browser.switch_to.window(original_window)
        self.sign_in.logout()


if __name__ == '__main__':
    unittest.main()
