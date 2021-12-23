import time
from behave import *
from driver import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('the user navigate to element in the page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(3)
    time.sleep(1)
    context.driver.get('https://jqueryui.com/droppable/')
    context.driver.maximize_window()


@when('the user drag and drop the element in the page')
def step_impl(context):
    fromElement = context.driver.find_element(By.ID, "draggable")
    toElement = context.driver.find_element(By.ID, "droppable")
    
    try:
        actions = ActionChains(driver)
        actions.drag_and_drop(fromElement, toElement).perform()
        # actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
        print("Drag And Drop Element Successful")
        time.sleep(2)
    except:
        print("Drag And Drop failed on element")


@then('the user should be able to verify a element been drag and dropped in the page.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user should be able to verify a element been drag and dropped in the page.')