from behave import step
from selenium.webdriver.common.by import By


@step('I am on the {page} page')
def open_page(context, page):
    page_obj = getattr(context, page.lower().replace(' ', '_'))
    page_obj.goto_page()

@step('I login as {user}')
@step('I login as {user} / {password}')
def login(context, user, password=None):
    if password:
        context.sign_in.login(user=user, password=password)
    else:
        context.sign_in.login(user=user)

@step('the welcome message should be {text}')
def welcome_message_is(context, text):
    welcome_message = context.base_methods.find_elem((By.ID, 'welcome')).text
    assert text == welcome_message, f'Expected welcome message to be {text} but it was actually {welcome_message}'