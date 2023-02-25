import logging
from datetime import time

import pytest
import utilities.custom_logger as cl
from pageObjects.TC001_login_page import LoginPage
from pageObjects.TC002_LinksSmokeTestPage import SmokeTest
from pageObjects.TC003_ImgsSmokeTestPage import ImgSmokeTest
from pageObjects.TC005_TDDLoginTestPage import LoginPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig


class Test_TC007_TestSuit( ):
    baseURL = ReadConfig.getApplicationURL()
    getUseremail = ReadConfig.getUseremail()
    getPassword = ReadConfig.getPassword()
    syslog = cl.customLogger(logging.DEBUG)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.syslog.info(" ====== WebDriver manager ======")
        self.syslog.info("Current google-chrome version is 94.0.4606")
        self.syslog.info("Get LATEST driver version for 94.0.4606")

        self.syslog.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.lp.broken_link()

        self.lp.broken_image()
        self.lp.login_btn()


        self.lp.clickLoginLink()
        self.syslog.info("****Started enterEmail Test****")
        self.lp.login('uktalenthub@gmail','hub123')
        self.lp.clickLoginButton()




        act_title = self.driver.title
        if act_title == "Let's Kode It":#Let's Kode It
            self.syslog.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.syslog.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False


