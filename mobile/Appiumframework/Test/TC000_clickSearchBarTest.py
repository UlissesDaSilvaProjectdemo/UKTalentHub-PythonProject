import unittest
import pytest
from mobile.Appiumframework.Base.DriverClass import Driver
from mobile.Appiumframework.Pages.TC000_clickSearchBarPage import clickSearchBar
import mobile.Appiumframework.Utilities.customlogger as cl
import warnings
log=cl.customLogger()


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class SearchBarTest(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver


    @pytest.fixture(autouse=True)
    def classObjects(self):
        log.info("----------- UK_TALENT_HUB - Starting  Mobile Click Search Bar Test ------------- ")
        cl.allureLogs('TEST UK Click Mobile search abr logs')
        self.cf=clickSearchBar(self.driver)

    @pytest.mark.run()
    def test_opencontactForm(self):
        self.cf.clickSearchtFormBar()








