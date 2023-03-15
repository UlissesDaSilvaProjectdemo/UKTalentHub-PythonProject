from selenium import webdriver
import utilities.CustomLogger as cl


class WebDriverClass:
    log = cl.customLogger()

    sauce_username = "code2lead"
    sauce_access_key = "xxxxxxxx-8f43-xxxx-8339-xxxxxxxxxxxx"

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome("/Users/sujithreddy/Documents/Code2Lead/Others/drivers/chromedriver")
            self.log.info("Chrome Driver is initializing")
        elif browserName == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari Driver is initializing")
        elif browserName == "firefox":
            driver = webdriver.Firefox(executable_path="/Users/sujithreddy/Documents/Code2Lead/drivers/geckodriver")
            self.log.info("FireFox Driver is initializing")

        return driver

    def cloudDriver(self,pName,bName,bVersion):
        SauceOptions = {
            'name': 'Dummy Point Test FrameWork',
            'build': 'Version 1',
            'screenResolution': '1280x768',
            'username': self.sauce_username,
            'accessKey': self.sauce_access_key,
            # tags to filter test reporting.
            'tags': ['Framework', 'pytest', 'module4'],
        }

        capabilities = {
            'browserName': bName,
            'browserVersion': bVersion,
            'platformName': pName,
            'sauce:options': SauceOptions
        }

        url = "https://ondemand.saucelabs.com:443/wd/hub"

        driver = webdriver.Remote(command_executor=url, desired_capabilities=capabilities, keep_alive=True)

        return driver
