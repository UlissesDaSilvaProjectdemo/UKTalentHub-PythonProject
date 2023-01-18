*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/PO/LandingPage.robot
Resource    ../Resources/PO/TopNav.robot
Resource    ../Resources/PO/ContactForm.robot

*** Variables ***
${Name_locator} =    id=firstname-34dd68e0-b077-4e95-9243-b861f3f2fd7d
${LastName_locator} =    id=lastname-34dd68e0-b077-4e95-9243-b861f3f2fd7d
${Company_locator} =    id=company-34dd68e0-b077-4e95-9243-b861f3f2fd7d
${Phone_locator} =    id=phone-34dd68e0-b077-4e95-9243-b861f3f2fd7d
${Text_locator} =    id=message-34dd68e0-b077-4e95-9243-b861f3f2fd7d
${Email_locator} =    id=email-34dd68e0-b077-4e95-9243-b861f3f2fd7d

*** Keywords ***
Click "Contact" in TopNav
    TopNav.Click on Contact
Input "name" in form
    ContactForm.Fill_Out_Box  ${Name_locator}   Anthony
Input "last name" in form
    ContactForm.Fill_Out_Box  ${LastName_locator}   Miller
Input "company" in form
    ContactForm.Fill_Out_Box  ${Company_locator}   Castellar Ltd
Input "email" in form
    ContactForm.Fill_Out_Box  ${Email_locator}   AMillerC@amazon.com
Input "phone" in form
    ContactForm.Fill_Out_Box  ${Phone_locator}   07748375614
Selecting checkbox
    ContactForm.Select your Checkbox
Input "text" in form
    ContactForm.Fill_Out_Box  ${Text_locator}   "Just testing this form"
Scroll Down 1
    ContactForm.Scroll Down Page    0,500

Scroll Down 2
    ContactForm.Scroll Down Page    0,750

Srcoll Down 3
    ContactForm.Scroll Down Page    0,1000

Click on radio button
    ContactForm.Select in the button    what_would_you_like_to_talk_about_    Partnership Inquiries
Click on Submit button
    ContactForm.Submit