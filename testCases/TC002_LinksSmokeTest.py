import pytest
from pageObjects.TC002_LinksSmokeTestPage import SmokeTest
from utilities.readProperties import ReadConfig
import utilities.custom_logger as cl
import logging
from allure_commons.types import AttachmentType
import allure

@allure.description('Test allure report - allure.severity_level.NORMAL')
@allure.severity(severity_level="NORMAL")

@pytest.mark.sanity
@pytest.mark.regression

class Test_TC02_LinkSmokeTest:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    syslog = cl.customLogger(logging.DEBUG)


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.syslog.info(" ====== WebDriver manager ======")
        self.syslog.info("Current google-chrome version is 94.0.4606")
        self.syslog.info("Get LATEST driver version for 94.0.4606")
        self.syslog.info("****Started Login Test****")

        self.syslog.info(" ====== WebDriver manager ======")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = SmokeTest(self.driver)
        self.lp.broken_link()


    def page_title_assertion(self):
        act_title = self.driver.title
        if act_title == "BBC - Home":  #
            self.syslog.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.syslog.info("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driverget_screenshot_as_png()

            self.driver.close()
            assert False
