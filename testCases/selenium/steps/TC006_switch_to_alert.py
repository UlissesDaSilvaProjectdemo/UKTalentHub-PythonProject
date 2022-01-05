import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


@given('the user navigate to home page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(3)
    time.sleep(1)
    context.driver.get('https://courses.letskodeit.com/practice')
    context.driver.maximize_window()


@when('the user switch to the alert the page')
def step_impl(context):
    context.driver.find_element_by_id("name").send_keys("Anil")
    context.driver.find_element_by_id( "alertbtn").click()
    time.sleep(2)
    alert1 = context.driver.switch_to.alert
    alert1.accept()
    time.sleep(2)
    context.driver.find_element_by_id("name").send_keys("Anil")
    context.driver.find_element_by_id("confirmbtn").click()
    time.sleep(2)
    alert2 = context.driver.switch_to.alert
    alert2.dismiss()

@then('the user should be able to verify the alert page.')
def step_impl(context):
   page_title = context.driver.title
   if page_title == "Practice Page":
       assert True
   else:
       assert False
