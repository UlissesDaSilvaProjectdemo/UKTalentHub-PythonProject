import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

@given('the user navigate to mouse hovering element in the page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(3)
    time.sleep(1)
    context.driver.get('https://courses.letskodeit.com/practice')
    context.driver.maximize_window()


@when('the user mouse hovering the element in the page')
def step_impl(context):
    context.driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(1)
    element = context.driver.find_element_by_id("mousehover")
    itemToClickLocator = "//*[@href="#top"]"
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    topLink = driver.find_element_by_xpath(itemToClickLocator)
    time.sleep(3)
    actions.move_to_element(topLink).click().perform()
    


@then('the user should be able to verify a element been mouse over in the page.')
def step_impl(context):
    page_title = context.driver.title
    if page_title == "Practice Page":
        assert True
    else:
        assert False
        context.driver.close()
