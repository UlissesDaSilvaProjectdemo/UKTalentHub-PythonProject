import unittest
import pytest
import time

from behave import step, given,when,then

from pages.EnterTextPage import EnterText


class EnterTextTest:


    @given("Create the class objects")
    def classObjects(context):
        context.et = EnterText(context.driver)
        print(context.testVariable)


    @when("Click on Locators Page")
    def clickOnLocatorsPage(context):
        context.et.clickOnLocatorsPage()

    @when("Enter Data")
    def enterDataInEditBox(context):
        context.driver.maximize_window()
        time.sleep(2)
        context.et.enterText()

    @then("CLick on Submit button")
    def clickOnSubmitB(context):
        context.et.clickOnSubmitButton()