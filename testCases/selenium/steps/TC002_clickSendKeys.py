import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('the user navigate to the text field section of page')
def navigate(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    time.sleep(4)
    context.driver.get('https://letskodeit.teachable.com')
    context.driver.maximize_window()

@when('the user select a text field and perform sendkeys action')
def select(context):
    time.sleep(1)
    clickLogin = context.driver.find_element(By.XPATH,"//*[@id='navbar']/div/div/div/ul/li[2]/a")
    clickLogin.click()

    time.sleep(1)
    emailField = context.driver.find_element(By.ID,"email")
    emailField.send_keys("test")

    time.sleep(1)
    passwordField = context.driver.find_element(By.ID,"password")
    passwordField.send_keys("test")

    time.sleep(1)
    emailField.clear()

    time.sleep(1)
    emailField.send_keys("test")


@then('the user should be able to sendkeys action in the page.')
def verify_sendkeys(context):
    print('user able to send keys')
