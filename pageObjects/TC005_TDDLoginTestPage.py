import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    signin_button_xpath = "//*[@id=mail']"
    password_xpath = "//*[@id='p'header']/div[2]/div/div/nav/div[1]/a"
    email_login_xpath = "//*[@id='eassword']"
    login_button_xpath = "//*[@id='login-button']"

    signin_button = "//*[@id='login-button']"

    _logout_btn_xpath ="//*[@id='header']/div[2]/div/div/nav/div[2]/a"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def signin_button(self):
        self.driver.find_element(By.XPATH,"//*[@id='header']/nav/div/div/div[2]/div/div/div[2]/a[1]").click()


    def setUserName(self, username):

        self.driver.find_element(By.XPATH,"//*[@id='email']").clear()
        self.driver.find_element(By.XPATH,"//*[@id='email']").send_keys(username)



    def setPassword(self, password):
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//*[@id='password']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)


    def login_btn(self):
        time.sleep(2)
        #self.driver.find_element_by_xpath(self.login_button_xpath).click()
        self.driver.find_element(By.XPATH,"//*[@id='login-button']").click()


    def click_password(self):
        time.sleep(1)
        self.driver.get('https://www.lambdatest.com/')






