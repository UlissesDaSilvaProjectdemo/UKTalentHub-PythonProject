from mobile.Appiumframework.Base.BasePage import BasePage
import mobile.Appiumframework.Utilities.customlogger as cl

class clickMessageBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _clickMessageBar = "Messaging"  # ClassName
    _enterDataSearchBar = "com.android.quicksearchbox:id/search_src_text"

    def clickSearchtFormBar(self):
        self.clickElement(self._clickMessageBar, "text")
        cl.allureLogs("click on the searchbar")






