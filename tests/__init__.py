import os


QA = 'http://hrm-online.portnov.com'
PRE_PROD = 'http://hrm.portnov.com'

TEST_ENV = os.environ.get('TEST_ENV')

DOMAIN = eval(TEST_ENV) if TEST_ENV else QA
BASE_URL = f'{DOMAIN}/symfony/web/index.php'

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(TESTS_DIR)

OUTPUT_DIR = 'test_run_results'



