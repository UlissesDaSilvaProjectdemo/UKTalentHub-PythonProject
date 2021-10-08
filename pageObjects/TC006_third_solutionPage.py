import logging
import driver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from utilities.customLogger import LogGen
import softest
logger = LogGen.loggen()


class TC006_third_solutionPage:
    Login_linkBtn_xpath = "//a[@class='btn btn-sm btn-link text-primary']"
    textbox_username_id = "user"
    login_btn_id = "login"
    login_with_attassian_id = "login"
    textbox_password_id = "password"
    atlassian_signup_xpath = "//*[@id='signup']"
    atlassian_already_have_an_account_id = "already-have-an-account"
    atlassian_click_login_xpath = "//*[@id='login-submit']/span"
    navigate_to_card_xpath = "//*[@class='board-tile-details is-badged']"
    click_first_card_xpath = "//*[@id='board']/div[1]/div/div[2]/a[1]"
    verify_firs_card_text_xpath = "//*[@class='list-card-edit-title js-edit-card-title']"
    close_first_card_xpath = "//*[@id='chrome-container']/div[3]/div/div[2]/a"
    click_second_card_xpath = "//*[@id='board']/div[1]/div/div[2]/a[2]"
    verify_second_card_text_xpath = "//*[@id='chrome-container']/div[3]/div/div[2]/div/div[3]/div[1]/h2"
    add_comment_second_card_xpath = "//*[@id='chrome-container']/div[3]/div/div[2]/div/div[4]/div[11]/div[2]/form/div/div/textarea"
    close_second_card_xpath = "//a[@class='icon-md icon-close dialog-close-button js-close-window']"
    verify_first_card_with_comment_xpath = "//*[@class='current-comment js-friendly-links js-open-card']"
    add_new_comment_first_card_xpath = "//*[@class= 'comment-box-input js-new-comment-input']"
    source_element_xpath = "//*[@id='board']/div[1]/div/div[2]/a[1]"
    target_element_xpath = "//*[@id='board']/div[4]/div/div[1]/textarea"
    click_cant_login_id = "resetPassword"
    click_return_login_xpath = "//*[@id='reset-password-email-cancel']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

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
        self.synchronize()
        self.driver.find_element_by_id(self.login_btn_id).click()

    def atlassian_signup(self, supportUrl):
        self.driver.get(supportUrl)
        self.synchronize_atlassian_signup()
        self.driver.find_element_by_xpath(self.atlassian_signup_xpath).click()

    def already_have_an_account(self):
        self.synchronize()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_id(self.atlassian_already_have_an_account_id).click()

    def click_cant_login(self):
        self.synchronize()
        self.driver.find_element_by_id(self.click_cant_login_id).click()

    def click_return_login(self):
        self.synchronize()
        self.driver.find_element_by_xpath(self.click_return_login_xpath).click()

    def trello_enter_password(self, trello_password):
        self.synchronize_pwd()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(trello_password)

    def atlassian_click_login(self):
        self.synchronize()
        self.driver.find_element_by_xpath(self.atlassian_click_login_xpath).click()

    def navigate_to_first_card(self):
        self.synchronize_first_card()
        self.driver.find_element_by_xpath(self.navigate_to_card_xpath).click()

    def open_first_card(self):
        self.synchronize()
        self.driver.find_element_by_xpath(self.click_first_card_xpath).click()

    def verify_first_card(self):
        self.synchronize()
        self.card_name = self.driver.find_element_by_xpath(self.verify_firs_card_text_xpath)
        self.first_card_title = self.card_name.get_attribute('class')
        if self.first_card_title == "first_card":
            logger.info('Verify first card is valid (%s)', self.first_card_title)
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            logger.error('Verify First card not valid! (%s)', self.first_card_title)


    def verify_first_card_with_comment(self):
        self.synchronize()
        card_name = self.driver.find_element_by_xpath(self.verify_first_card_with_comment_xpath)
        first_card_comment = card_name.get_attribute('class')
        try:
            if first_card_comment == "Fancy new comment":
                logger.error('Verify card valid! (%s)', self.first_card_title)
                assert True
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
                logger.error('Verify   card  not valid! (%s)', self.first_card_title)
                assert False
        except:
            print('Second Card with Assertions Fails')




    def add_new_comment_first_card(self):
        self.synchronize()
        self.driver.find_element_by_xpath(self.add_new_comment_first_card_xpath).send_keys("add new comment")

    def close_first_card(self):
        self.synchronize()
        self.driver.find_element_by_xpath(self.close_first_card_xpath).click()

    def navigate_to_second_card(self):
        self.synchronize()
        self.driver.find_element_by_xpath(self.click_second_card_xpath).click()

    def verify_second_card(self):
        self.synchronize()
        self.driver.find_element_by_xpath(self.add_comment_second_card_xpath).send_keys(
            "verify second card and set as done")
        card_name = self.driver.find_element_by_xpath(self.verify_second_card_text_xpath)
        second_card_title = card_name.get_attribute('class')
        try:
            if second_card_title == "verify second card and set as done":
                logger.error('verify second card and set as done valid! (%s)', self.first_card_title)
                assert True
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
                logger.error('verify second card and set as done not valid! (%s)', self.first_card_title)
                assert False
        except:
            print('verify second card and set as done Assertions Fails')

    def close_second_card(self):
        self.synchronize()
        self.driver.find_element_by_xpath(self.close_second_card_xpath).click()

    def set_card_to_done(self):
        self.synchronize()
        self.driver.find_element_by_xpath(self.click_second_card_xpath).click()
        self.synchronize()
        target = self.driver.find_element_by_xpath(self.click_second_card_xpath)
        source = self.driver.find_element_by_xpath(self.source_element_xpath)
        actions = ActionChains(driver)
        actions.drag_and_drop(target, source).perform()

    def synchronize(self):
        try:
            self.driver.implicitly_wait(120)
        except:
            print("Enterself.driver.implicitly_wait(10) time out fail "
                  "will increase the time to 10 seconds more "
                  "to max 60")
        try:
            self.driver.set_page_load_timeout(120)
        except:
            print("Enter self.driver.set_page_load_timeout(20) time out fail "
                  "will increase the time to 10 seconds more"
                  "to max 60")
        try:
            self.driver.set_page_load_timeout(120)
            wait = WebDriverWait(driver, 120, poll_frequency=1)
        finally:
            print("page is taking to long to load the elements  in the DOM")

    def synchronize_pwd(self):
        try:
            self.driver.implicitly_wait(120)
        except:
            print("Enter self.driver.implicitly_wait(10)  time out fail "
                  "will increase the time to 10 seconds more "
                  "to max 60")
        try:
            self.driver.set_page_load_timeout(120)
        except:
            print("Enter self.driver.set_page_load_timeout(20) time out fail "
                  "will increase the time to 10 seconds more"
                  "to max 60")
        try:
            self.driver.set_page_load_timeout(120)
            wait = WebDriverWait(driver, 120, poll_frequency=1)
        finally:
            print("page is taking to long to load elements  in the DOM")

    def synchronize_first_card(self):
        try:
            self.driver.implicitly_wait(120)
            self.driver.set_page_load_timeout(120)
        except:
            print("Enter page load time out fail "
                  "will increase the time to 10 seconds more"
                  "to max 60")
        try:
            wait = WebDriverWait(driver, 120, poll_frequency=1)
            self.driver.find_element_by_id(self.textbox_password_id).send_keys(Keys.ENTER)
        except:
            print("Enter page load time out fail "
                  "will increase the time to 10 seconds more"
                  "to max 60")

    def synchronize_atlassian_signup(self):
        try:
            self.driver.implicitly_wait(120)
        except:
            print("Enter page load time out fail "
                  "will increase the time to 10 seconds more "
                  "to max 60")
        try:
            self.driver.set_page_load_timeout(120)
        except:
            print("Enter page load time out fail "
                  "will increase the time to 10 seconds more"
                  "to max 60")
        try:
            self.driver.set_page_load_timeout(120)
            wait = WebDriverWait(driver, 120, poll_frequency=1)
        finally:
            print("page is taking to long to load elements  in the DOM")