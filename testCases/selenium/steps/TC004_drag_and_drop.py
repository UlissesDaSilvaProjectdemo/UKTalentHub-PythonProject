import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


@given('the user navigate to element in the page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(3)
    time.sleep(1)
    context.driver.get('https://jqueryui.com/droppable/')
    context.driver.maximize_window()
    context.driver.switch_to.frame(0)


@when('the user drag and drop the element in the page')
def step_impl(context):
    time.sleep(3)
    context.driver.implicitly_wait(3)
    fromElement = context.driver.find_element_by_xpath("//*[@id='draggable']")
    toElement = context.driver.find_element_by_xpath("//*[@id='droppable']")
    actions = ActionChains(context.driver)
    actions.drag_and_drop(fromElement,toElement).click().perform()
    #actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()



@then('the user should be able to verify a element been drag and dropped in the page.')
def step_impl(context):
    print('verify drag and drop')
