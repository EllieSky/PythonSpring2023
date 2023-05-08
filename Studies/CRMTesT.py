import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class CrmLogin(unittest.TestCase):
    def setUp(self) -> None:
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        driver.get('https://sscrm-uat-naa.crm.dynamics.com/')
        waiter = WebDriverWait(driver, 10)
        self.driver = driver
        self.waiter = waiter

    def test_valid_login(self):
        driver = self.driver
        waiter = self.waiter

        # wait for the element to be present
        waiter.until(EC.presence_of_element_located((By.ID, 'i0116'))).send_keys('nokumus.naa.salesmanager18@otis.com')
        waiter.until(EC.presence_of_element_located((By.ID, 'idSIButton9'))).click()
        waiter.until(EC.presence_of_element_located((By.ID, 'i0118'))).send_keys('Ch@ngemen0w')
        waiter.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
        waiter.until(EC.element_to_be_clickable((By.ID, 'idBtn_Back'))).click()
        waiter.until(EC.element_to_be_clickable((By.ID,'mectrl_headerPicture'))).click()

        login_name = waiter.until(EC.presence_of_element_located((By.ID,'mectrl_signedInTitle'))).text
        self.assertEqual('SSCRM UAT NAA', login_name)




if __name__ == '__main__':
    unittest.main()
