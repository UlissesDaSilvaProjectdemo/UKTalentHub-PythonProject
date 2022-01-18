import requests
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from webdriver_manager import driver



class ImgSmokeTest:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def broken_image(self):

        capabilities = {
            "build": "[Python] Finding broken images on a webpage using Selenium",
            "name": "[Python] Finding broken images on a webpage using Selenium",
            "platform": "Windows 10",
            "browserName": "Chrome",
            "version": "latest"
        }

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        remote_url = self.driver.get('https://www.bbc.co.uk/')
        image_list = self.driver.find_elements(By.TAG_NAME, "img")
        print('Total number of images on ' + remote_url + ' are ' +str(image_list))

        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if (response.status_code != 200):
                    print(img.get_attribute('outerHTML') + " is broken.")
                    iBrokenImageCount = (iBrokenImageCount + 1)
            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except:
                print("Encountered Some other Exception")
        print('The page ' + remote_url + ' has ' + str(iBrokenImageCount) + ' broken images')
        self.driver.quit()