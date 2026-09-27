*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://automationexercise.com
${BROWSER}   Chrome

*** Test Cases ***
Generate Report And Log
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Log    Browser opened successfully
    Wait Until Page Contains    Automation Exercise    20s
    Log    Automation Exercise home page verified successfully
    Capture Page Screenshot    ${CURDIR}${/}screenshots${/}Experiment_4_7_Result.png
    Log    Screenshot captured successfully
    Close Browser
    Log    Test execution completed successfully