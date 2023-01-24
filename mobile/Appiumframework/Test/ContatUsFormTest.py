import logging
import unittest
import pytest
from mobile.Appiumframework.Base.DriverClass import Driver
from mobile.Appiumframework.Pages.ContactsForm import ContactForm
from mobile.Appiumframework.Utilities.customlogger import customLogger
from mobile.Appiumframework.Base.BasePage import BasePage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self. cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()



#driver = Driver()
#log = customLogger()
#driver.getDriverMethod()
#log.info("lunch the app")


#bp=BasePage(driver)
#element = bp.waitForElement()
#cf=ContactForm(Driver)

#element =bp.isDisplayed("com.qualitest.kawd:id/ContactUs","id")
#bp.clickElement("com.qualitest.kawd:id/ContactUs","id")
#bp.screenShot("qualitest")

#cf.clickContactFormButton()
#cf.enterName()
#cf.enterAddress()
#cf.enterEmail()
#cf.clickSubmitButton()






