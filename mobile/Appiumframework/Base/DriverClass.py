from appium import  webdriver
class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel 2 API TiramisuPrivacySandbox'
        desired_caps['app'] = ('C:\Users\Ulisses.Dasilva\Downloads\Appium\demoApk\Android_Demo_App')
        desired_caps['appPackage'] = 'com.google.android.apps.nexuslauncher'
        desired_caps['appActivity'] = 'com.google.android.apps.nexuslauncher.NexusLauncherActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver

