*** Settings ***
Documentation    This is some basic info about the whole suite


Resource    ../Resources/common.robot
Resource    ../Resources/PO/LandingPage.robot
Resource    ../Resources/PO/ThanksPage.robot
Resource    ../Resources/QualitestApp.robot
Test Setup    common.Begin Web Test
Test Teardown    common.End Web Test
*** Variables ***
${BROWSER} =    chrome
${WEB_PAGE} =    http://qualitestgroup.com
${LOGIN_EMAIL} =    AMillerBristol@amazon.com


*** Test Cases ***
Qualitest Contact Form
     LandingPage.Load
     LandingPage.Verify Page Loaded
     LandingPage.Maximize_Page
     QualitestApp.Click "Contact" in TopNav
     QualitestApp.Scroll Down 1
     QualitestApp.Input "name" in form
     QualitestApp.Input "last name" in form
     QualitestApp.Input "company" in form
     QualitestApp.Click on radio button
     QualitestApp.Scroll Down 2
     QualitestApp.Input "email" in form
     QualitestApp.Input "phone" in form
     QualitestApp.Selecting checkbox
     QualitestApp.Srcoll Down 3
     QualitestApp.Input "text" in form
     QualitestApp.Click on Submit button
     ThanksPage.Verify Page Loaded