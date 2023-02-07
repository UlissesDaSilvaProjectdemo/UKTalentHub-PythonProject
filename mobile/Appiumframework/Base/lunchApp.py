from appium import webdriver


#desired_caps = {}
#desired_caps['platformName'] = 'Android'
#desired_caps['automationName'] = 'UiAutomator2'
#desired_caps['udid'] = 'emulator-5554'
#desired_caps['deviceName'] = 'Pixel_6'
#desired_caps['app'] = ('C:\Users\Ulisses.Dasilva\Downloads\Appium\demoApk\Android_Demo_App.apk')
#desired_caps['appPackage'] = 'com.google.android.apps.nexuslauncher'
#desired_caps['appActivity'] = 'com.google.android.apps.nexuslauncher.NexusLauncherActivity'

#driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


caps = {}
caps['platformName'] = "Android"
caps['appium:deviceName'] = "Android GoogleAPI Emulator"
caps['appium:deviceOrientation'] = "portrait"
caps['appium:platformVersion'] = "12.0"
caps['appium:automationName'] = "UiAutomator2"
caps['appium:app'] = "storage:filename=<your-app>.apk"
caps['sauce:options'] = {}
caps['sauce:options']['build'] = 'appium-build-IEZ6N'
caps['sauce:options']['name'] = '<your test name>'

url = 'https://oauth-ulissesdasilva39-33bb5:45fe4b87-6d25-44e7-9afe-cd383b6b634f@ondemand.eu-central-1.saucelabs.com:443/wd/hub';
driver = webdriver.Remote(url, caps)
