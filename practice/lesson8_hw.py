# login to orange hrm, navigate to PIM tab
#find Job Title fied, pick an option = QA Manager
#click Search button
#verify Job Title(every row) = QA Manager
# Tip: use time.sleep(3)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
driver.get('http://hrm-online.portnov.com/')

def test_find_all_qa_mngrs():

    username = driver.find_element(By.ID, "txtUsername")
    username.send_keys('admin')

    password = driver.find_element(By.ID, "txtPassword")
    password.send_keys('password')

    login_btn = driver.find_element(By.ID, "btnLogin")
    login_btn.click()
    time.sleep(3)

    pim_btn = driver.find_element(By.ID, "menu_pim_viewPimModule")
    pim_btn.click()

    employee_list_btn = driver.find_element(By.ID, "menu_pim_viewEmployeeList")
    employee_list_btn.click()

    job_title_btn = driver.find_element(By.ID, "empsearch_job_title").click()
    time.sleep(3)
    qa_mngr_opt = driver.find_element(By.CSS_SELECTOR, '#empsearch_job_title > option:nth-child(8)').click()

    search_btn = driver.find_element(By.ID, "searchBtn").click()
    time.sleep(3)

def test_verify_job_title():
    job_titles = driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(5)')

    if len(job_titles) == 0:
        print("No employees found")
        return False

    first_title = job_titles[0].text

    for job_title in job_titles[1:]:
        if job_title.is_displayed() and job_title.text == first_title:
            print("Job Title of employee does match")
        elif job_title.is_displayed() and job_title.text != first_title:
            print("Job Title of employee doesn't match")
            return False

    return True
















