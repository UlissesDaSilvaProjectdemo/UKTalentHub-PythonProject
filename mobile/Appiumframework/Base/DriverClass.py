from appium import  webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel'
        desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/kwad.apk')
        desired_caps['appPackage'] = 'com.qualitestgroup.kwad'
        desired_caps['appActivity'] = 'com.qualitestgroup.kwad.MainActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver

