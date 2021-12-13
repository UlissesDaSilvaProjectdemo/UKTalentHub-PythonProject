import requests
from utilities.customLogger import LogGen
logger = LogGen.loggen()

# A server generates HTTP Status codes in response to the request submitted
# by the client to the server.
# 200 – Valid Link/success
# 301/302 - Page redirection temporary/permanent
# 404 – Page not found
# 400 – Bad request
# 401 – Unauthorized
# 500 – Internal Server Error

class  SmokeTest:
    Login_linkBtn_xpath = "//a[@class='btn btn-sm btn-link text-primary']"
    textbox_username_id = "user"
    login_btn_id = "login"
    find_elements_by_css_selector="a"

    def __init__(self, driver):
        self.driver = driver


    def broken_link(self):
        self.driver.get('https://www.bbc.co.uk/')
        links = self.driver.find_elements_by_css_selector(self.find_elements_by_css_selector)
        for link in links:
            r = requests.head(link.get_attribute('href'))
            print(link.get_attribute('href'), r.status_code)


    def click_login_link(self):
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(self.Login_linkBtn_xpath).click()

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(password)

    def login_btn(self):
        self.synchronize()
        self.driver.find_element_by_id(self.login_btn_id).click()



