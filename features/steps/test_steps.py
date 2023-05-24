from behave import given, when, then, step

@step('my last name is {name}')
@given('my name is {name}')
@given('my word is {name}')
def store_input(context, name):
    context.my_name = context.my_name + name if hasattr(context, 'my_name') else name

@when('I count the letters in my name')
@when('I count the letters in my word')
def count_letters(context):
    context.name_length = len(context.my_name)


@then('there should be {count} letters in total')
def check_count(context, count):
    assert context.name_length == int(count),\
        f'Expected name length to be {count} characters but it was actually {context.name_length} characters'