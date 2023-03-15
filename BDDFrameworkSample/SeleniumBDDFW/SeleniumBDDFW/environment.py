
import time
from behave import step
from base.BasePage import BaseClass
from base.DriverClass import WebDriverClass
import utilities.CustomLogger as cl
import configurationfiles.DeviceConfig as dc

log = cl.customLogger()


def before_all(context):
    log.info("Automation Started")
    context.testVariable = "This is a Test variable"
    context.driver1 = WebDriverClass()
    context.driver = context.driver1.getWebDriver(dc.bName)
    context.bp = BaseClass(context.driver)
    context.bp.launchWebPage(dc.url, dc.title)


def after_all(context):
    time.sleep(5)
    context.driver.quit()
    log.info("Automation Ended")
