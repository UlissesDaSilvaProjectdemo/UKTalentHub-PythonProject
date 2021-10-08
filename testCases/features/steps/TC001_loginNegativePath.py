import self
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager


@given('the user launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

@when('the user open the trello application homepage')
def step_impl(context):
    context.driver.get('https://trello.com/login')

@then('the user enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("user").send_keys(user)
    context.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)

@then('the user click on the login button')
def step_impl(context):
    context.driver.find_element_by_id("login").click()





