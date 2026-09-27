*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://automationexercise.com/login
${BROWSER}   Chrome
${SCREENSHOT_DIR}    ${CURDIR}${/}screenshots

@{EMAILS}    test1@example.com    test2@example.com    test3@example.com
@{PASSWORDS}    password1    password2    password3

*** Test Cases ***
Data Driven Login Test
    FOR    ${email}    ${password}    IN ZIP    ${EMAILS}    ${PASSWORDS}
        Open Browser    ${URL}    ${BROWSER}
        Maximize Browser Window
        Wait Until Element Is Visible    xpath=//input[@data-qa='login-email']    15s
        Input Text    xpath=//input[@data-qa='login-email']    ${email}
        Input Text    xpath=//input[@data-qa='login-password']    ${password}
        Log    Testing login with ${email}
        Capture Page Screenshot    ${SCREENSHOT_DIR}${/}Experiment_4_2_${email}.png
        Close Browser
    END