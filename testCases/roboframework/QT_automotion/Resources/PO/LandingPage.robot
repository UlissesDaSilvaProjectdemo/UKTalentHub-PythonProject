*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Keywords ***

Load
    Go To    ${WEB_PAGE}

Verify Page Loaded
    wait until page contains    Enabling digital transformation. Touching lives.

Maximize_Page
    MAXIMIZE BROWSER WINDOW
    sleep    2s