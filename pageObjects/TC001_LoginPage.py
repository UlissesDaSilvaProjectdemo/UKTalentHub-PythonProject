import time
from selenium.webdriver.support.wait import WebDriverWait



class LoginPage:
    signin_button_xpath = "//*[@id='header']/div[2]/div/div/nav/div[1]/a"
    email_login_xpath = "//*[@id='email']"
    password_xpath = "//*[@id='passwd']"
    login_button_xpath = "//*[@id='SubmitLogin']"
    _login_button = "//*[@id='SubmitLogin']"


    def __init__(self, driver):
        self.driver = driver

    def signin_button(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.email_login_xpath).clear()
        self.driver.find_element_by_xpath(self.email_login_xpath).send_keys(username)

    def setPassword(self, password):
        time.sleep(1)
        self.driver.find_element_by_xpath(self.password_xpath).clear()
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)

    def login_btn(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    # def login_btn(self):
    #     time.sleep(1)
    #     self.driver.SeleniumDriver.elementClick(self._login_button,locatorType="//*[@id='SubmitLogin']")
    #     self.driver.close()






