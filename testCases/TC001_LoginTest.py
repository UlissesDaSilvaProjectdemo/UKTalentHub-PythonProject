import pytest
from pageObjects.TC001_LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import utilities.custom_logger as cl
import logging

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    #logger = LogGen.loggen()
    syslog = cl.custom_Logger(logging.DEBUG)

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
        self.lp.signin_button() 
        self.lp.setPassword(self.password)
        self.lp.setUserName(self.username)
        self.syslog.info("****Finished Login Test****")
        self.lp.login_btn()



        act_title = self.driver.title
        if act_title == "xxxxLogin - My Store":#Login - My Store
            self.syslog.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.syslog.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False


