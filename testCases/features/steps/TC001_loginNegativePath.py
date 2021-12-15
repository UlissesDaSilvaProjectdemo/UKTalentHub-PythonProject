import self
from behave import *
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given('the user launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

@when('the user open the trello application homepage')
def step_impl(context):
    context.driver.set_page_load_timeout(100)
    context.driver.implicitly_wait(100)
    context.driver.get('https://trello.com/login')
    context.driver.maximize_window()


@then('the user enter username "{user}" and password "{pwd}"')
def step_impl(context,user, pwd):
    time.sleep(3)
    context.driver.set_page_load_timeout(100)
    context.driver.find_element_by_id("user").send_keys(user)
    time.sleep(3)
    context.driver.set_page_load_timeout(100)
    context.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)

@then('the user click on the login button')
def step_impl(context):
    time.sleep(3)
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_id("login").click()


@then('the user do not successfully login into the application homepage')
def step_impl(context):
    time.sleep(3)
    print('There isnt an account for this email')




@then('the user close the browser')

def step_impl(context):
     time.sleep(3)
     context.driver.close()








