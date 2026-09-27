*** Settings ***
Resource    resources.robot

Test Setup       Open Application
Test Teardown    Close Application

*** Test Cases ***
Verify Home Page Using Resource Keywords
    Verify Home Page
    Capture Page Screenshot    ${CURDIR}${/}screenshots${/}Experiment_4_8_Result.png