from behave import step

from lib.base_methods import BaseMethods


@step('I open the {url} url')
def open_url(context, url):
    context.browser.get(url)

@step('I look for the element {by}={locator}')
def find_elem(context, by, locator):
    bm: BaseMethods = context.base_methods
    return bm.find_elem((by, locator))

@step('I enter text {text} into the element {by}={locator}')
def enter_text(context, text, by, locator):
    find_elem(context, by, locator).send_keys(text)

@step('I click the {by}={locator} element')
def click_element(context, by, locator):
    find_elem(context, by, locator).click()

@step('the url should contain {url}')
def url_contains(context, url):
    assert url in context.browser.current_url,\
        f'Expected url to be {url} but it was actually {context.browser.current_url}'

@step('I get the text from element {by}={locator}')
def get_text(context, by, locator):
    context.element_text = find_elem(context, by, locator).text

@step('the text should be {text}')
def text_is(context, text):
    assert text == context.element_text,\
        f'Expected text to be {text} but it was actually {context.element_text}'