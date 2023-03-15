import unittest
import pytest
import time

from behave import step,given,when,then

from base.BasePage import BaseClass
from pages.ContctFormPage import ContactForm
import utilities.CustomLogger as cl


class ContactFormTest:

    @given("Create the class objects in cfp")
    def classObjects(context):
        context.cf = ContactForm(context.driver)
        context.bp = BaseClass(context.driver)


    @when("Click Contact Form")
    def contactformPage(context):
        context.cf.clickContactForm()

    @then("verify form page")
    def verifyContactForm(context):
        context.cf.verifyFormPage()


    @then("Enter the data in form")
    def enterDataInForm(context):
        time.sleep(5)
        context.cf.enterName()
        context.cf.enterEmail()
        context.cf.enterMessage()
        context.cf.enterCaptha()
        context.cf.clickOnPostButton()
