from mobile.Appiumframework.Base.BasePage import BasePage
import mobile.Appiumframework.Utilities.customlogger as cl

class clickSearchBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _clickSearchtFormBar = "android.widget.TextView"  # ClassName
    _enterDataSearchBar = "com.android.quicksearchbox:id/search_src_text"

    def clickSearchtFormBar(self):
        self.clickElement(self._clickSearchtFormBar, "class")

    def clickEnter_DataSearchBar(self):
        self.sendText( "UK_TALENT_HUB",self._enterDataSearchBar, "id")




