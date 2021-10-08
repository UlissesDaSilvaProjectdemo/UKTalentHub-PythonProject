import self
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager


@given(u'the user navigate to the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user navigate to the login page')


@when(u'the user set username "trellologin2021@gmail.com" andtrellologin20221@1234$ password "')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user set username "trellologin2021@gmail.com" andtrellologin20221@1234$ password "')


@then(u'the user click on atlassian signup')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user click on atlassian signup')


@then(u'the user click on already have account')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user click on already have account')


@then(u'the user click can\'t login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user click can\'t login')


@then(u'the user click return login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user click return login')


@then(u'the user enter trello password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user enter trello password')


@then(u'the user click on atlassian login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user click on atlassian login')


@given(u'the user navigate to the first card')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user navigate to the first card')


@when(u'the user verify first card with comment')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user verify first card with comment')


@when(u'the user add new comment first card')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user add new comment first card')


@then(u'the user close first card')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user close first card')


@given(u'the user navigate to the second card')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user navigate to the second card')


@when(u'the user verify second card')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user verify second card')


@then(u'the user close second card')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user close second card')


@then(u'the user set card to done')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user set card to done')
