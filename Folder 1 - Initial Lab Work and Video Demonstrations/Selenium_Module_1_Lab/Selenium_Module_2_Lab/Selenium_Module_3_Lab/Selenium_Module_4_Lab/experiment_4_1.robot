*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://automationexercise.com/products
${BROWSER}   Chrome

*** Test Cases ***
Basic Robot Framework Web Test
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//input[@id='search_product']    20s
    Page Should Contain Element    xpath=//input[@id='search_product']
    Input Text    xpath=//input[@id='search_product']    Blue Top
    Click Button    xpath=//button[@id='submit_search']
    Wait Until Element Is Visible    xpath=//h2[contains(translate(., 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'SEARCHED PRODUCTS')]    20s
    Log    Product search completed successfully
    Close Browser