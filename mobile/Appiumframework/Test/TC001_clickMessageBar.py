import unittest
import pytest
from mobile.Appiumframework.Base.DriverClass import Driver
from mobile.Appiumframework.Base.BasePage import BasePage
from mobile.Appiumframework.Pages.TC001_SearchBarPage import LunchAppPage
import mobile.Appiumframework.Utilities.customlogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(BasePage):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf =LunchAppPage(self.driver)

    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
            self.cf.clickSearchtFormBar()