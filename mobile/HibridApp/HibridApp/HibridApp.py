from appium import webdriver
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""
1.) Mobile Browser version and ChromeDriver or respective Browser Driver should be in same version 
2.) 
Two Ways of Identifying locators on webview i) open chrome browser and type "chrome://inspect/#devices" ii) Use Browser 
inspectors 

"""
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/Others/kwad.apk')
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'

# 1. Create the Driver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 2. Create WebDriverWait
wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

# 3. Open the URL in Browser
ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/terms_accept"))
ele.click()

ele2 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/negative_button"))
ele2.click()

ele3 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text"))
ele3.click()

ele4 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar"))
ele4.click()
ele4.send_keys("https://www.google.com/")

driver.press_keycode(66)

time.sleep(5)

# 4. Get the list of Contexts in App
appContexts = driver.contexts
print("AppContexts : ", appContexts)

# 5. switch to webview to perform action on Required URL or on WebView
for appType in appContexts:
    if appType == "WEBVIEW_chrome":
        driver.switch_to.context(appType)

# 6. Do testing on Webview screen in chrome browser or any if we want
ele4 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//*[@name='q']"))
ele4.send_keys("Skill2Lead")

# 7. Switch back to native view to perform action
for appType in appContexts:
    if appType == "NATIVE_APP":
        driver.switch_to.context(appType)

# 8. Do testing on native app screen if we want

ele4 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar"))
ele4.click()
ele4.send_keys("https://www.skill2lead.com/")
driver.press_keycode(66)

# 9. Quit or close the driver object

time.sleep(5)
driver.quit()