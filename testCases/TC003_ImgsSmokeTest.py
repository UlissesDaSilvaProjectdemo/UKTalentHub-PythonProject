
import pytest
from pageObjects.TC003_ImgsSmokeTestPage import ImgSmokeTest
from utilities.readProperties import ReadConfig
import utilities.custom_logger as cl
import logging


@pytest.mark.sanity
@pytest.mark.regressio
class Test_TC003_ImgSmokeTest:
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

                self.driver = setup
                self.driver.get(self.baseURL)
                self.lp = ImgSmokeTest(self.driver)
                self.lp.broken_image()

                act_title = self.driver.title
                if act_title == "BBC - Home":  # Page title
                    self.syslog.info("****Login test passed ****")
                    self.driver.close()
                    assert True
                else:
                    self.syslog.info("****Login test failed ****")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
                    self.driverget_screenshot_as_png()
                    self.driver.close()
                    assert False






