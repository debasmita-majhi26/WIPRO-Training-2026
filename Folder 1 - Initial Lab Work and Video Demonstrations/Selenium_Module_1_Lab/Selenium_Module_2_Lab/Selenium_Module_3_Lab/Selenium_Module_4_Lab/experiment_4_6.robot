*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://automationexercise.com
${BROWSER}   Chrome

*** Test Cases ***
Verify Home Page
    [Tags]    smoke
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains    Automation Exercise    20s
    Log    Home page verified successfully
    Capture Page Screenshot    ${CURDIR}${/}screenshots${/}Experiment_4_6_Home.png
    Close Browser

Verify Products Page
    [Tags]    regression
    Open Browser    ${URL}/products    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//input[@id='search_product']    20s
    Page Should Contain Element    xpath=//input[@id='search_product']
    Log    Products page verified successfully
    Capture Page Screenshot    ${CURDIR}${/}screenshots${/}Experiment_4_6_Products.png
    Close Browser