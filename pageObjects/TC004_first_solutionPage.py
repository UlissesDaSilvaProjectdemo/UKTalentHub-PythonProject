import driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class TC004_first_solutionPage:
    # emaillogin =
    email_login = ReadConfig.emaillogin()

    # password =
    password = ReadConfig.password()

    #loginbutton
    login_button = ReadConfig.password()

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.emaillogin).clear()
        self.driver.find_element_by_id(self.emaillogin).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.loginbutton).send_keys(password)

    def login_btn(self):
        self.driver.find_element_by_id(self.loginbutton).click()

