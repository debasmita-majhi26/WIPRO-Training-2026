*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary

*** Variables ***
${URL}              https://automationexercise.com/products
${BROWSER}          Chrome
${SCREENSHOT_DIR}   ${CURDIR}${/}screenshots

*** Test Cases ***
UI Assertion Test
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//input[@id='search_product']    20s
    Page Should Contain Element    xpath=//input[@id='search_product']
    Input Text    xpath=//input[@id='search_product']    Blue Top
    Click Button    xpath=//button[@id='submit_search']
    Wait Until Element Is Visible    xpath=//div[@class='productinfo text-center']    20s
    Page Should Contain Element    xpath=//div[@class='productinfo text-center']
    Log    Product search assertion passed successfully
    Capture Page Screenshot    ${SCREENSHOT_DIR}${/}Experiment_4_4_UI.png
    Close Browser

API Response Assertion Test
    Create Session    jsonplaceholder    https://jsonplaceholder.typicode.com
    ${response}=    GET On Session    jsonplaceholder    /posts/1
    Should Be Equal As Strings    ${response.status_code}    200
    Log    API response status verified successfully