import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

@given('the user should navigate to home page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(3)
    time.sleep(1)
    context.driver.get('https://courses.letskodeit.com/practice')
    context.driver.maximize_window()


@when('the user switch to window page')
def step_impl(context):

    # Find parent handle -> Main Window
    parentHandle = context.driver.current_window_handle
    # Find open window button and click it
    context.driver.find_element_by_id( "openwindow").click()
    time.sleep(4)
    # Find all handles, there should two handles after clicking open window button
    handles = context.driver.window_handles
    # Switch to window and search course
    for handle in handles:
        if handle not in parentHandle:
            context.driver.switch_to.window(handle)
            searchBox = context.driver.find_element_by_id("search")
            searchBox.send_keys("python")
            time.sleep(3)
            driver.close()
            break
    # Switch back to the parent handle
    context.driver.switch_to.window(parentHandle)
    context.driver.find_element_by_id("name").send_keys("Test Successful")

@then('the user should be able to verify the page')
def step_impl(context):
   page_title = context.driver.title
   if page_title == "All Coures":
       assert True
   else:
       assert False
       context.driver.close()
