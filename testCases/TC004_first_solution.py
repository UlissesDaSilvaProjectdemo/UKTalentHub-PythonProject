import pytest
from selenium import webdriver
from pageObjects.TC004_first_solutionPage import TC004_first_solutionPage
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
        self.lp = TC004_first_solutionPage(self.driver)
        self.lp.setPassword(self.password)
        self.lp.setUserName(self.username)
        self.lp.login_btn()


        act_title = self.driver.title
        if act_title == "New Name for second card on Plentific_Trello":  # Boards | Trello
            self.logger.info("****Login test passed ****")
            # self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            # self.driver.close()
            assert False



