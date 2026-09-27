*** Settings ***
Library    SeleniumLibrary

Test Setup       Open Application
Test Teardown    Close Application

*** Variables ***
${URL}       https://automationexercise.com/login
${BROWSER}   Chrome

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Close Application
    Close All Browsers

*** Test Cases ***
Verify Login Page
    Wait Until Element Is Visible    xpath=//input[@data-qa='login-email']    20s
    Page Should Contain Element    xpath=//input[@data-qa='login-email']
    Page Should Contain Element    xpath=//input[@data-qa='login-password']
    Log    Login page verified successfully
    Capture Page Screenshot    ${CURDIR}${/}screenshots${/}Experiment_4_5_Result.png