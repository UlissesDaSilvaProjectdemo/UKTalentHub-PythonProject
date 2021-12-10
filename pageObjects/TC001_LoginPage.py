from telnetlib import EC

from driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    contact_xpath ="//*[@id='contact-link']/a"
    signin_button_xpath = "//*[@id='header']/div[2]/div/div/nav/div[1]/a"
    emaillogin_xpath = "//*[@id='email']"
    password_xpath = "//*[@id='passwd']"
    login_button_xpath ="//*[@id='SubmitLogin']"

    def __init__(self, driver):
        self.driver = driver

    def contact(self):
        self.driver.find_element_by_xpath(self.contact_xpath).click()

    def signin_button(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.emaillogin_xpath).clear()
        self.driver.find_element_by_xpath(self.emaillogin_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.password_xpath).clear()
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)

    def login_btn(self):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='SubmitLogin']")))
        element.click()
        self.driver.find_element_by_id(self.login_button_xpath).click()


