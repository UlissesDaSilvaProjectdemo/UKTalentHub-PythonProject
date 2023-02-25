from behave import *
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given('the user launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

@when('the user open the trello application homepage')
def step_impl(context):
    context.driver.implicitly_wait(10 )
    context.driver.get('https://trello.com/login')
    context.driver.maximize_window()


@then('the user enter username "{username}" and password "{password}"')
def step_impl(context,username , password):
    time.sleep(1)
    context.driver.find_element("xpath","//*[@id='user']").send_keys(username)
    time.sleep(1)
    context.driver.find_element("xpath","//*[@id='password']").send_keys(password)


@then('the user click on the login button')
def step_impl(context):
    time.sleep(1)
    context.driver.implicitly_wait(20)
    context.driver.find_element_by_id("login").click()


@then('the user do not successfully login into the application homepage')
def step_impl(context):
    time.sleep(1)
    print('There isnt an account for this email')




@then('the user close the browser')

def step_impl(context):
     time.sleep(1)









