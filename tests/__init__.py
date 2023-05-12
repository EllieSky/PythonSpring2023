import os


QA = 'http://hrm-online.portnov.com'
PRE_PROD = 'http://hrm.portnov.com'

TEST_ENV = os.environ.get('TEST_ENV')

DOMAIN = eval(TEST_ENV) if TEST_ENV else QA
BASE_URL = f'{DOMAIN}/symfony/web/index.php'



