import softest
import self
import driver
from testCases import TC002_syncrhonize_login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class LoginPage:

    emaillogin = "//*[@id='email']"
    password = "//*[@id='passwd']"
    login_button ="//*[@id=SubmitLogin']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.emaillogin).clear()
        self.driver.find_element_by_id(self.emaillogin).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def login_btn(self):
        self.driver.find_element_by_id(self.login_btn).click()