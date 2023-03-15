from base.BasePage import BaseClass
import utilities.CustomLogger as cl


class EnterText(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact form
    _locatorsPage="Locators" # link
    _enterTextEditBox = "user_input"  # id
    _submitButton = "submitbutton"  # id

    def clickOnLocatorsPage(self):
        self.clickOnElement(self._locatorsPage,"link")

    def enterText(self):
        self.sendText("Code2Lead",self._enterTextEditBox,"id")
        cl.allureLogs("Entered Text in Edit Box")

    def clickOnSubmitButton(self):
        self.clickOnElement(self._submitButton,"id")