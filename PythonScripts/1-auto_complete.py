from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

baseUrl = "http://www.goibibo.com"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(3)


@staticmethod
class autocomplete():

    def auto_complet_dropdown(self):
        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by index")