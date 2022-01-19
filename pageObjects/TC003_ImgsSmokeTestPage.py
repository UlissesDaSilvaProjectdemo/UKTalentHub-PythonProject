import requests
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class ImgSmokeTest:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def broken_image(self):
        self.driver.get('https://www.bbc.co.uk/')
        image_list = self.driver.find_elements_by_tag_name('img')
        for img in image_list:
            r = requests.head(img.get_attribute('src'))
            print(img.get_attribute('src'),r.status_code)



