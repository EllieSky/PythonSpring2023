import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests import get_browser


class FramesWindowsExample(unittest.TestCase):
    def setUp(self) -> None:
        browser = get_browser()

        self.browser = browser
        self.wait = WebDriverWait(self.browser, 6)


    def tearDown(self) -> None:
        self.browser.quit()

    def test_frames(self):
        browser = self.browser
        browser.get('https://demoqa.com/nestedframes')

        # default content
        # the title of the page 'Nested Frames'
        self.assertEqual('Nested Frames',
                         browser.find_element(By.CLASS_NAME, 'main-header').text)

        # find the first frame and switch INTO it
        browser.switch_to.frame(browser.find_element(By.ID, 'frame1'))

        # check frame text
        frame1_text = browser.find_element(By.TAG_NAME, 'body').text
        self.assertEqual('Parent frame', frame1_text)

        # This is the size of the parent frame:
        frame_size = browser.find_element(By.TAG_NAME, 'body').size
        self.assertDictEqual({'height': 330, 'width': 480}, frame_size)


        child_frame_size = browser.find_element(By.TAG_NAME, 'iframe').size
        self.assertDictEqual({'height': 154, 'width': 304}, child_frame_size)
        # switch to nested iframe (it does not have id, so using xpath to locate)

        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//body/iframe')))
        # browser.switch_to.frame(browser.find_element(By.XPATH, '//body/iframe'))

        # check nested frame text
        frame2_text = browser.find_element(By.TAG_NAME, 'p').text
        self.assertEqual('Child Iframe', frame2_text)

        browser.switch_to.default_content()
        # default content
        # the title of the page 'Nested Frames'
        self.assertEqual('Nested Frames',
                         browser.find_element(By.CLASS_NAME, 'main-header').text)

    def test_windows(self):
        browser = self.browser
        browser.get('https://demoqa.com/browser-windows')

        current_number_of_windows = len(browser.window_handles)

        browser.find_element(By.ID, 'tabButton').click()
        self.wait.until(EC.number_of_windows_to_be(current_number_of_windows + 1))

        original_window = browser.current_window_handle
        browser.switch_to.window(browser.window_handles[-1])

        new_tab_text = browser.find_element(By.ID, 'sampleHeading').text
        self.assertEqual('This is a sample page', new_tab_text)

        # we closed the new tab
        browser.close()
        browser.switch_to.window(original_window)

        current_handles = browser.window_handles
        browser.find_element(By.ID, 'windowButton').click()
        self.wait.until(EC.new_window_is_opened(current_handles))

        browser.switch_to.window(browser.window_handles[-1])

        new_window_text = browser.find_element(By.ID, 'sampleHeading').text
        self.assertEqual('This is a sample page', new_window_text)

    def test_shadow_root(self):
        browser = self.browser
        browser.get('http://uitestingplayground.com/shadowdom')

        # get_shadow_root_script = 'document.querySelector("guid-generator").shadowRoot'
        # all *args get passed by execute_script command into JS as arguments[] list
        get_shadow_root_script = 'return arguments[0].shadowRoot;'
        shadow_root_element: WebElement = browser.execute_script(get_shadow_root_script, browser.find_element(By.TAG_NAME, 'guid-generator'))
        shadow_root_element.find_element(By.ID, 'buttonGenerate').click()
        guid = shadow_root_element.find_element(By.ID, 'editField').get_attribute('value')
        self.assertNotEqual('', guid)







if __name__ == '__main__':
    unittest.main()
