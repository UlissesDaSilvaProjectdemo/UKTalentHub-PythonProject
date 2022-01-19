import pytest
from pageObjects.TC002_LinksSmokeTestPage import SmokeTest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from allure_commons.types import AttachmentType
import allure





@allure.description('Test allure report - allure.severity_level.NORMAL')
@allure.severity(severity_level="NORMAL")
@pytest.mark.sanity
@pytest.mark.regression
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @allure.description('Test allure report - allure.severity_level.NORMAL')
    @allure.severity(severity_level="NORMAL")
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = SmokeTest(self.driver)
        self.lp.broken_link()

    def driverget_screenshot_as_png(self):
        allure.attached(self.driverget_screenshot_as_png(), name="testloginScreen",
                         attachment_type=AttachmentType.png)
        pass

    @allure.severity(severity_level="CRITICAL")
    def page_title_assertion(self):
        act_title = self.driver.title
        if act_title == "BBC - Home":  #
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driverget_screenshot_as_png()

            self.driver.close()
            assert False
