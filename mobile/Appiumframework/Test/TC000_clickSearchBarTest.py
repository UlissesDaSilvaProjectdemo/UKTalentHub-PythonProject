import unittest
import pytest
from mobile.Appiumframework.Base.DriverClass import Driver
from mobile.Appiumframework.Base.BasePage import BasePage
from mobile.Appiumframework.Pages.TC000_clickSearchBarPage import clickSearchBar
import mobile.Appiumframework.Utilities.customlogger as cl
import warnings
log=cl.customLogger()


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class SearchBarTest(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classObjects(self):
        log.info("-----------Starting  Mobile Click Search Bar Test ------------- ")
        self.cf=clickSearchBar(self.driver)


    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        self.cf.clickSearchtFormBar()

    @pytest.mark.run(order=2)
    def test_enter_DataSearchBar(self):
        self.cf.clickEnter_DataSearchBar()






