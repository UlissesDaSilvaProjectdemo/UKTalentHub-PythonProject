import time
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@given('the user should navigate to scrolling element in the home page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(3)
    time.sleep(1)
    context.driver.get("https://www.qualitest.com/contact/")
    context.driver.maximize_window()

@when(u'the user should  be able to scrolling the element icon in the page')
def step_impl(context):
    # Scroll Down
    context.driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(3)

    #Scroll Up
    context.driver.execute_script("window.scrollBy(0, -1000);")
    time.sleep(3)

    # Scroll Element Into View
    element = context.driver.find_element(By.ID, "mousehover")
    context.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    context.driver.execute_script("window.scrollBy(0, -150);")

    # Native Way To Scroll Element Into View
    time.sleep(2)
    context.driver.execute_script("window.scrollBy(0, -1000);")
    location = element.location_once_scrolled_into_view
    print("Location: " + str(location))
    context.driver.execute_script("window.scrollBy(0, -150);")


@then(u'the user should be able to verify the scrolling the element the page.')
def step_impl(context):
    page_title = context.driver.title
    if page_title == "Practice Page":
        assert True
    else:
        context.driver.close()
        assert False
