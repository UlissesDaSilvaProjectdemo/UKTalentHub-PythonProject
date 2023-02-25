from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel_6'
desired_caps['appPackage'] = 'com.android.launcher3'
desired_caps['appActivity'] = 'com.android.launcher3.uioverrides.QuickstepLauncher'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(3)
ele_text = driver.find_element(AppiumBy.CLASS_NAME,'android.widget.TextView')
ele_text.click()







