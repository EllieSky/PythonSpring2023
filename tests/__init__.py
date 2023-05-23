import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

QA = 'http://hrm-online.portnov.com'
PRE_PROD = 'http://hrm.portnov.com'

TEST_ENV = os.environ.get('TEST_ENV')

DOMAIN = eval(TEST_ENV) if TEST_ENV else QA
BROWSER = os.environ.get('BROWSER') or 'chrome'
BASE_URL = f'{DOMAIN}/symfony/web/index.php'

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(TESTS_DIR)

DEFAULT_WAIT = 6

OUTPUT_DIR = 'test_run_results'

def get_browser(browser_type=BROWSER):
    if browser_type == 'chrome':
        options = webdriver.ChromeOptions()
        if os.environ.get('HEADLESS'):
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            options.add_argument("--remote-debugging-port=9222")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--ignore-certificate-errors")
        return webdriver.Chrome(options=options, service=Service(
            executable_path=ChromeDriverManager().install()))
    elif browser_type == 'firefox':
        return webdriver.Firefox(service=Service(
            executable_path=GeckoDriverManager().install()))
    else:
        raise TypeError(f'Unsupported browser type: {browser_type}')
