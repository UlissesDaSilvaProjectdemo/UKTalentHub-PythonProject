import openpyxl
import requests
from bs4 import BeautifulSoup
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from bs4 import BeautifulSoup


class data_listScrape:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def data_list(self):
        self.driver.get('https://en.wikipedia.org/wiki/Lists_of_cities')
        data_list = self.driver.find_elements_by_tag_name('li')
        for item in data_list:
            text = item.text
            print(text)














