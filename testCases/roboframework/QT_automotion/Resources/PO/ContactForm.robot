*** Settings ***
Library    SeleniumLibrary

*** Variables ***

*** Keywords ***
Scroll Down Page
    [Arguments]    ${CORDS}
    execute javascript    window.scrollTo(${CORDS})
    sleep    2s
Fill_Out_Box
    [Arguments]    ${text_locator}    ${text}

    input text    ${text_locator}    ${text}
    sleep    0.75s

Select in the button
    [Arguments]    ${name}    ${value}
    select radio button    ${name}    ${value}
Select your Checkbox
    click element    //*[@id="location-34dd68e0-b077-4e95-9243-b861f3f2fd7d"]
    sleep  1s
    click element    //option[@value='North America']
    sleep    1s
Submit
    click button    //input[@type='submit']
    sleep    5s
