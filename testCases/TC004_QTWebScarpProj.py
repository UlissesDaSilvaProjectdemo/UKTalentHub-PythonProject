import pytest
from pageObjects.TC004_QTWebScarpProjPage import data_listScrape
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_001_CleintData:
            baseURL = ReadConfig.getApplicationURL()
            logger = LogGen.loggen()


            @pytest.mark.sanity
            @pytest.mark.regression
            def test_ClientData(self, setup):
                self.logger.info("****Started  Test_001_CleintData Test****")
                self.driver = setup
                self.driver.get(self.baseURL)
                self.lp = data_listScrape(self.driver)
                self.lp.data_list()



                act_title = self.driver.title
                if act_title == "Lists of cities - Wikipedia":  # Page title
                    self.logger.info("****Login test passed ****")
                    self.driver.close()
                    assert True
                else:
                    self.logger.error("****Login test failed ****")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
                    self.driver.close()
                    assert False






