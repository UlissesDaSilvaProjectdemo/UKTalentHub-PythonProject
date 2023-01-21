from mobile.Appiumframework.Base.BasePage import BasePage


class ContactForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _contactFromButton = "com.code2lead.kwad:id/ContactUs"  # id
    _pagetitle = "Contact Us form"  # text
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobileNumber = "4"  # index number
    _submitButton = "SUBMIT"  # text

    def clickContactFormButton(self):
        self.clickElement(self._contactFromButton, "id")

    def verifyContactPage(self):
        element = self.isDisplayed(self._pagetitle, "text")
        assert element == True

    def enterName(self):
        self.sendText("Code2Lead",self._enterName,"text")

    def enterEmail(self):
        self.sendText("abc@gmail.com",self._enterEmail,"text")

    def enterAddress(self):
        self.sendText("India",self._enterAddress,"text")

    def enterMNumber(self):
        self.sendText("987654210",self._enterMobileNumber,"index")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton,"text")
