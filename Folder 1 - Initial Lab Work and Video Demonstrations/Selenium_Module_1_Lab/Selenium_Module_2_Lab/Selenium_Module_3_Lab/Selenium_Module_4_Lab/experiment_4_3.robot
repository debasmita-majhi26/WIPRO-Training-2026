*** Settings ***
Library    BuiltIn
Library    String
Library    ${CURDIR}${/}python_keywords${/}custom_keywords.py

*** Test Cases ***
Custom Python Keyword Test
    ${result}=    Calculate Sum    10    20
    Should Be Equal As Integers    ${result}    30
    Log    Sum calculated using Python custom keyword: ${result}

BuiltIn String And Math Test
    ${text}=    Set Variable    robot framework
    ${upper_text}=    Convert To Upper Case    ${text}
    Should Be Equal    ${upper_text}    ROBOT FRAMEWORK
    ${number}=    Evaluate    10 + 20
    Should Be Equal As Integers    ${number}    30
    Log    String and mathematical operations completed successfully