*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Keywords ***


Verify Page Loaded
    wait until page contains    Thanks for contacting us.
