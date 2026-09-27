*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://automationexercise.com
${BROWSER}   Chrome

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Close Application
    Close All Browsers

Verify Home Page
    Wait Until Page Contains    Automation Exercise    20s
    Log    Home page verified successfullydone
    