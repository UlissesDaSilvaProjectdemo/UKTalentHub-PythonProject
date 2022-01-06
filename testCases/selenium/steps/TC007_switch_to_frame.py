import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

@given('the user should navigate to switch frame home page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(3)
    context.driver.maximize_window()
    context.driver.get('https://courses.letskodeit.com/practice')
    context.driver.execute_script("window.scrollBy(0, 800);")

@when('the user switch to frame  page')
def step_impl(context):
    # # Switch to frame using Id
    context.driver.switch_to.frame('courses-iframe')
    time.sleep(2)

    # Switch to frame using name
    #context.driver.switch_to.frame('iframe-name')

    # Switch to frame using numbers
    #context.driver.switch_to.frame(0)

    context.driver.find_element_by_xpath("//*[@id='search']").send_keys("python")
    time.sleep(2)

    context.driver.switch_to.default_to.default_content()
    context.driver.execute_script("window.scrollBy(0, -1000):")
    time.sleep(2)
    context.driver.find_element_by_id('name').send_Keys('Test sucessfull')


@then('the user should be able to verify the switch to frame page.')
def step_impl(context):
   page_title = context.driver.title
   if page_title == "Practice Page":
       assert True
   else:
       assert False
