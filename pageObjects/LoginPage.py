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
    Login_linkBtn_xpath = "//a[@class='btn btn-sm btn-link text-primary']"
    textbox_username_id = "user"
    login_btn_id = "login"
    atlassian_password_xpath = "//*[@id='password']"
    login_with_attassian_id = "login"
    textbox_password_id = "password"
    atlassian_signup_xpath = "//*[@id='signup']"
    atlassian_already_have_an_account_id = 'already-have-an-account'
    atlassian_click_login_xpath = "//*[@id='login-submit']/span"
    navigate_to_card_xpath = " //*[@id='content']/div/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/ul/li[1]/a/div/div[1]"
    click_work_space_xpath = "//*[@id='content']/div/div[2]/div/div[1]/div/div/div[1]/nav/div[2]/daiv/ul/li/a/span[1]"
    click_first_card_xpath = "//*[@id='board']/div[1]/div/div[2]/a[1]"
    verify_firs_card_text_xpath = "//*[@id='chrome-container']/div[3]/div/div[2]/div/div[4]/div[11]/div[2]/form/div/div/textarea"
    close_first_card_xpath = "//*[@id='chrome-container']/div[3]/div/div[2]/a"
    click_second_card_xpath = "//*[@id='board']/div[1]/div/div[2]/a[2]"
    verify_second_card_text_xpath = "//*[@id='chrome-container']/div[3]/div/div[2]/div/div[3]/div[1]/h2"
    add_comment_second_card_xpath = "//*[@id='chrome-container']/div[3]/div/div[2]/div/div[4]/div[11]/div[2]/form/div/div/textarea"
    close_second_card_xpath = "//a[@class='icon-md icon-close dialog-close-button js-close-window']"
    verify_first_card_with_comment_xpath = "//*[@class='current-comment js-friendly-links js-open-card']"
    add_new_comment_first_card_xpath = "//*[@id='chrome-container']/div[3]/div/div[2]/div/div[4]/div[11]/div[2]/form/div/div/textarea"

    source_element = "//*[@id='board']/div[1]/div/div[2]/a[1]"
    target_element = "//*[@id='board']/div[4]/div/div[1]/textarea"

    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    #Implicit wait Mix With Explicit  Synchronization Not Recomended -----------------------//------------------
    def click_login_link(self):
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(self.Login_linkBtn_xpath).click()

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def login_btn(self):
        self.driver.find_element_by_id(self.login_btn_id).click()

    def atlassian_signup(self, supportUrl):
        self.driver.get(supportUrl)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        self.driver.implicitly_wait(120)
        self.driver.set_page_load_timeout(120)
        wait = WebDriverWait(driver, 120, poll_frequency=1)
        self.driver.find_element_by_xpath(self.atlassian_signup_xpath).click()

    def already_have_an_account(self):
        self.driver.implicitly_wait(120)
        self.driver.set_page_load_timeout(120)
        wait = WebDriverWait(driver, 120, poll_frequency=1)
        self.driver.find_element_by_id(self.atlassian_already_have_an_account_id).click()

    def trello_enter_password(self, trello_password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(20)
        wait = WebDriverWait(driver, 30, poll_frequency=1)
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(40)
        self.driver.set_page_load_timeout(50)
        wait = WebDriverWait(driver, 60, poll_frequency=1)
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(trello_password)

    def atlassian_click_login(self):
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(20)
        wait = WebDriverWait(driver, 30, poll_frequency=1)
        self.driver.find_element_by_xpath(self.atlassian_click_login_xpath).click()

    def navigate_to_first_card(self):
        self.driver.implicitly_wait(60)
        self.driver.set_page_load_timeout(70)
        wait = WebDriverWait(driver, 30, poll_frequency=1)
        self.driver.find_element_by_xpath(self.navigate_to_card_xpath)
        self.driver.implicitly_wait(60)
        self.driver.set_page_load_timeout(70)
        wait = WebDriverWait(driver, 60, poll_frequency=1)
        self.driver.find_element_by_xpath(self.navigate_to_card_xpath)
        self.driver.implicitly_wait(70)
        self.driver.set_page_load_timeout(120)
        wait = WebDriverWait(driver, 120, poll_frequency=1)
        self.driver.find_element_by_xpath(self.navigate_to_card_xpath).click()

    def open_first_card(self):
        self.driver.implicitly_wait(70)
        self.driver.set_page_load_timeout(80)
        wait = WebDriverWait(driver, 90, poll_frequency=1)
        self.driver.find_element_by_xpath(self.click_first_card_xpath).click()

    def verify_first_card(self):
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        self.card_name = self.driver.find_element_by_xpath(self.verify_firs_card_text_xpath)
        self.first_card_title = self.card_name.get_attribute('class')
        if self.first_card_title == "first_card":
            self.soft_assert(first_card_title)

    def verify_first_card_with_comment(self):
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        card_name = self.driver.find_element_by_xpath(self.verify_first_card_with_comment_xpath)
        first_card_comment = card_name.get_attribute('class')
        if first_card_comment == "Fancy new comment":
            soft_assert(first_card_comment)

    def add_new_comment_first_card(self):
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        wait = WebDriverWait(driver, 60, poll_frequency=1)
        self.driver.find_element_by_xpath(self.add_new_comment_first_card_xpath).send_keys("add new comment")

    def close_first_card(self):
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        wait = WebDriverWait(driver, 60, poll_frequency=1)
        self.driver.find_element_by_xpath(self.close_first_card_xpath).click()

    def navigate_to_second_card(self):
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        wait = WebDriverWait(driver, 60, poll_frequency=1)
        self.driver.find_element_by_xpath(self.click_second_card_xpath).click()

    def verify_second_card(self):
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        wait = WebDriverWait(driver, 60, poll_frequency=1)
        self.driver.find_element_by_xpath(self.add_comment_second_card_xpath).send_keys(
            "verify second card and set as done")
        card_name = self.driver.find_element_by_xpath(self.verify_second_card_text_xpath)
        second_card_title = card_name.get_attribute('class')
        if second_card_title == "New Name for second card":
            soft_assert(second_card_title)

    def close_second_card(self):
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        wait = WebDriverWait(driver, 60, poll_frequency=1)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.close_second_card_xpath).click()

    def set_card_to_done(self):
        source_element = driver.find_element_by_xpath(self.source_element)  # mouse over to admin
        target_element = driver.find_element_by_xpath(self.target_element)  # mpuse over  to usermanagement
        actions = ActionChains(driver)  # create object of action chain class
        actions.move_to_element(source_element).move_to_element(target_element).click()

