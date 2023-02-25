import pytest
from pageObjects.TC005_TDDLoginTestPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities import XLUtils
import time

import utilities.custom_logger as cl
import logging

class Test_TC002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    syslog = cl.customLogger(logging.DEBUG)

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.syslog.info("******* Starting Test_002_DDT_Login Test **********")
        self.syslog.info("******* Starting Login Set up **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.syslog.error("******* Starting Login **********")
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.signin_button()
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.login_btn()





            time.sleep(5)
            act_title = self.driver.current_url
            exp_title = "https://accounts.lambdatest.com/login" #Login - My Store
            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.syslog.info("**** passed ****")
                    self.lp.click_password();

                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.syslog.info("**** failed ****")
                    self.lp.click_password();

                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.syslog.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.syslog.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)

        if "Fail" not in lst_status:
            self.syslog.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.syslog.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.syslog.info("******* End of Login DDT Test **********")
        self.syslog.info("**************** Completed  TC_LoginDDT_002 ************* ");
