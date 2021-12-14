import pytest
from pageObjects.TC003_ImgsSmokeTestPage import ImgSmokeTest
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_001_Login:
            baseURL = ReadConfig.getApplicationURL()
            username = ReadConfig.getUseremail()
            password = ReadConfig.getPassword()
            logger = LogGen.loggen()

            @pytest.mark.sanity
            @pytest.mark.regression
            def test_login(self, setup):

                self.logger.info("****Started Login Test****")
                self.driver = setup
                self.driver.get(self.baseURL)
                self.lp = ImgSmokeTest(self.driver)
                self.lp.broken_image()

                act_title = self.driver.title
                if act_title == "BBC - Home":  # Page title
                    self.logger.info("****Login test passed ****")
                    self.driver.close()
                    assert True
                else:
                    self.logger.error("****Login test failed ****")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
                    # self.driver.close()
                    assert False



