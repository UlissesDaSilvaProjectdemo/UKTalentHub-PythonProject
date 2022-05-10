*** Settings ***
Library    SeleniumLibrary

*** Variables ***

*** Keywords ***
Begin Web Test
    open browser     about:blank   ${BROWSER}

End Web Test
    close browser