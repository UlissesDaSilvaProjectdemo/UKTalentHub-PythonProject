import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from pageObjects.TC006_third_solutionPage import TC006_third_solutionPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    trello_password = ReadConfig.trello_password()
    supportUrl = ReadConfig.supportUrl()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = TC006_third_solutionPage(self.driver)
        self.lp.click_login_link()
        self.lp.setPassword(self.password)
        self.lp.setUserName(self.username)
        self.lp.login_btn()
        self.lp.atlassian_signup(self.supportUrl)
        self.lp.already_have_an_account()
        self.lp.click_cant_login()
        self.lp.click_return_login()
        self.lp.trello_enter_password(self.trello_password)
        self.lp.atlassian_click_login()
        self.lp.navigate_to_first_card()
        self.lp.open_first_card()
        self.lp.add_new_comment_first_card()
        self.lp.close_first_card()
        self.lp.navigate_to_second_card()
        self.lp.verify_second_card()
        self.lp.close_second_card()
        self.lp.verify_first_card()
        self.lp.verify_first_card_with_comment()
        #self.lp.set_card_to_done()


        act_title = self.driver.title
        if act_title == "New Name for second card on Plentific_Trello":  # Boards | Trello
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False







