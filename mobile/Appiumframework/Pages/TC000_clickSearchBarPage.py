from mobile.Appiumframework.Base.BasePage import BasePage
import mobile.Appiumframework.Utilities.customlogger as cl

class clickSearchBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _clickSearchtFormBar = "com.android.quicksearchbox:id/search_widget_text"  # ClassName


    def clickSearchtFormBar(self):
        self.clickElement(self._clickSearchtFormBar, "id")





