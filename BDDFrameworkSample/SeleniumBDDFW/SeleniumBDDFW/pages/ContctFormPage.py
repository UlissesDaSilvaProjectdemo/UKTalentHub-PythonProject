from base.BasePage import BaseClass
import utilities.CustomLogger as cl


class ContactForm(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators  values in Contact form page

    _contactFromPage = "Form"  # link
    _formPage = "reused_form"  # id
    _enterName = "name"  # id
    _enterEmail = "email"  # id
    _enterMessage = "message"  # id
    _getCaptcha = "captcha_image"  # id
    _enterCaptha = "captcha"  # id
    _postButton = "btnContactUs"  # id

    def clickContactForm(self):
        self.clickOnElement(self._contactFromPage, "link")
        cl.allureLogs("Clicked on Contact Form")

    def verifyFormPage(self):
        element = self.isElementDisplayed(self._formPage, "id")
        assert element == True
        cl.allureLogs("Verified Contact Form")

    def enterName(self):
        self.sendText("Code2Lead", self._enterName, "id")
        cl.allureLogs("Entered Name")

    def enterEmail(self):
        self.sendText("abc@gmail.com", self._enterEmail, "id")
        cl.allureLogs("Entered Email")

    def enterMessage(self):
        self.sendText("This is a Code2Lead", self._enterMessage, "id")
        cl.allureLogs("Entered Message")

    def getCaptha(self):
        cap = self.getText(self._getCaptcha, "id")
        cl.allureLogs("Got the captcha data")
        return cap

    def enterCaptha(self):
        self.sendText(self.getCaptha(), self._enterCaptha, "id")
        cl.allureLogs("Entered captcha")

    def clickOnPostButton(self):
        self.scrollTo(self._postButton, "id")
        self.clickOnElement(self._postButton, "id")
        cl.allureLogs("Clicked on the post button")
