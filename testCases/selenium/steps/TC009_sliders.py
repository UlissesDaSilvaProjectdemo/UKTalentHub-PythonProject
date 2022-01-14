import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@given('the user should navigate to slide bar in the home page')
def step_impl(context):

    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(3)
    time.sleep(1)
    context.driver.get("https://jqueryui.com/slider/")
    context.driver.maximize_window()
    context.driver.switch_to.frame(0)

@when('the user should slide the bar icon in the page')
def step_impl(context):

            element = context.driver.find_element(By.XPATH, "//div[@id='slider']//span")
            time.sleep(2)
            try:
                actions = ActionChains(context.driver)
                actions.drag_and_drop_by_offset(element, 100, 0).perform()
                print("Sliding Element Successful")
                time.sleep(2)
            except:
                print("Sliding failed on element")

@then('the user should be able to verify the page.')
def step_impl(context):
   page_title = context.driver.title
   if page_title == "Slider | jQuery UI":
       assert True
   else:
       assert False
       context.driver.close()
