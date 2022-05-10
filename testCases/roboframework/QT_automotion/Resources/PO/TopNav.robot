*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${Contact_Button} =    xpath=//a[@class='main-nav-btn']
*** Keywords ***
Click on Contact
    click link    ${Contact_Button}
    sleep    2s

