import configparser
import self
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def trello_password():
        trello_password = config.get('common info', 'trello_password')
        return trello_password

    @staticmethod
    def supportUrl():
        supportUrl = config.get('common info', 'supportUrl')
        return supportUrl

    # Cucumber page Object
    @staticmethod
    def Login_linkBtn_xpath():
        Login_linkBtn_xpath = config.get('common info', 'Login_linkBtn_xpath')
        return Login_linkBtn_xpath

    @staticmethod
    def textbox_username_id():
        textbox_username_id = config.get('common info', 'textbox_username_id')
        return textbox_username_id

    @staticmethod
    def login_btn_id():
        login_btn_id = config.get('common info', 'login_btn_id')
        return login_btn_id

    @staticmethod
    def login_with_atlassian_id():
        login_with_atlassian_id = config.get('common info', 'login_with_atlassian_id')
        return login_with_atlassian_id

    @staticmethod
    def textbox_password_id():
        textbox_password_id = config.get('common info', 'textbox_password_id ')
        return textbox_password_id

    @staticmethod
    def atlassian_already_have_an_account_id():
        atlassian_already_have_an_account_id = config.get('common info', 'atlassian_already_have_an_account_id')
        return atlassian_already_have_an_account_id

    @staticmethod
    def atlassian_signup_xpath():
        atlassian_signup_xpath = config.get('common info', 'atlassian_signup_xpath')
        return atlassian_signup_xpath

    @staticmethod
    def atlassian_click_login_xpath():
        atlassian_click_login_xpath = config.get('common info', 'atlassian_click_login_xpath')
        return atlassian_click_login_xpath

    @staticmethod
    def navigate_to_card_xpath():
        navigate_to_card_xpath = config.get('common info', 'navigate_to_card_xpath')
        return navigate_to_card_xpath

    @staticmethod
    def click_first_card_xpath():
        click_first_card_xpath = config.get('common info', 'click_first_card_xpath')
        return click_first_card_xpath

    @staticmethod
    def verify_firs_card_text_xpath():
        verify_firs_card_text_xpath = config.get('common info', 'verify_firs_card_text_xpath')
        return verify_firs_card_text_xpath

    @staticmethod
    def close_first_card_xpath():
        close_first_card_xpath = config.get('common info', 'close_first_card_xpath')
        return close_first_card_xpath

    @staticmethod
    def click_second_card_xpath():
        click_second_card_xpath = config.get('common info', 'click_second_card_xpath')
        return click_second_card_xpath

    @staticmethod
    def verify_second_card_text_xpath():
        verify_second_card_text_xpath = config.get('common info', 'verify_second_card_text_xpath')
        return verify_second_card_text_xpath

    @staticmethod
    def add_comment_second_card_xpath():
        add_comment_second_card_xpath = config.get('common info', 'add_comment_second_card_xpath')
        return add_comment_second_card_xpath

    @staticmethod
    def close_second_card_xpath():
        close_second_card_xpath = config.get('common info', 'close_second_card_xpath')
        return close_second_card_xpath

    @staticmethod
    def verify_first_card_with_comment_xpath():
        verify_first_card_with_comment_xpath = config.get('common info', 'verify_first_card_with_comment_xpath')
        return verify_first_card_with_comment_xpath

    @staticmethod
    def add_new_comment_first_card_xpath():
        add_new_comment_first_card_xpath = config.get('common info', 'add_new_comment_first_card_xpath')
        return add_new_comment_first_card_xpath

    @staticmethod
    def source_element_xpath():
        source_element_xpath = config.get('common info', 'source_element_xpath')
        return source_element_xpath

    @staticmethod
    def target_element_xpath():
        target_element_xpath = config.get('common info', 'target_element_xpath')
        return target_element_xpath

    @staticmethod
    def click_cant_login_id():
        click_cant_login_id = config.get('common info', 'click_cant_login_id')
        return click_cant_login_id

    @staticmethod
    def click_return_login_xpath():
        click_return_login_xpath = config.get('common info', 'click_return_login_xpath')
        return click_return_login_xpath

    @staticmethod
    def link_logout_linktext():
        link_logout_linktext = config.get('common info', 'link_logout_linktext')
        return link_logout_linktext

    @staticmethod
    def account_sign_up():
        account_sign_up = config.get('common info', 'account_sign_up')
        return account_sign_up

    @staticmethod
    def login_button():
        account_sign_up = config.get('common info', 'login_button')
        return login_button
