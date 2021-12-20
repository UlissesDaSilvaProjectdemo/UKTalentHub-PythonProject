import time
from behave import *
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

@given('the user navigate to the dropdown section of page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    time.sleep(4)
    context.driver.get('https://courses.letskodeit.com/practice')
    time.sleep(4)
    context.driver.maximize_window()

@when('the user select a dropdown choice by text')
def step_impl(context):
    time.sleep(2)
    element = context.driver.find_element_by_id("carselect")
    sel = Select(element)

    sel.select_by_value("benz")
    print("Select Benz by value")
    time.sleep(2)

    sel.select_by_index("2")
    print("Select Honda by index")
    time.sleep(2)

    sel.select_by_visible_text("BMW")
    print("Select BMW by visible text")
    time.sleep(2)

    sel.select_by_index(2)
    print("Select Honda by index")

@then('the user should be able to verify the dropdown.')
def step_impl(context):
    print('verify choice')
