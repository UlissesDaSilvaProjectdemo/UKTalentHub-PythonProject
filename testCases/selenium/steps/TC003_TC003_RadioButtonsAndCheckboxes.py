import time
from behave import *
from driver import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




@given('the user navigate to the radio button and checkbox  section of  the page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(3)
    time.sleep(1)
    context.driver.get('https://courses.letskodeit.com/practice')
    context.driver.maximize_window()

@when('the user select a radio button and checkbox  in the page')
def step_impl(context):


    bmwRadioBtn = context.driver.find_element_by_id("bmwradio")
    bmwRadioBtn.click()

    time.sleep(2)
    benzRadioBtn = context.driver.find_element_by_id("benzradio")
    benzRadioBtn.click()

    time.sleep(2)
    bmwCheckbox = context.driver.find_element_by_id("bmwcheck")
    bmwCheckbox.click()

    time.sleep(2)
    benzCheckbox = context.driver.find_element_by_id("benzcheck")
    benzCheckbox.click()



@then('the user should be able to select the radio button and checkbox  in the page.')
def step_impl(context):
    print('verify checkboxes and radio button')


