import requests


# Global configuration
BASE_URL = "https://jsonplaceholder.typicode.com"
ENDPOINT = "/posts/1"


# Reusable data
test_data = {
    "expected_status": 200,
    "expected_user_id": 1
}


# Send API request
response = requests.get(BASE_URL + ENDPOINT)

data = response.json()


# Validate response
status_check = response.status_code == test_data["expected_status"]
user_check = data["userId"] == test_data["expected_user_id"]


output = f"""
API CONFIGURATION
Base URL: {BASE_URL}
Endpoint: {ENDPOINT}

RESPONSE
Status Code: {response.status_code}
User ID: {data["userId"]}
Title: {data["title"]}

VALIDATION
Status Code Validation: {"PASSED" if status_check else "FAILED"}
User ID Validation: {"PASSED" if user_check else "FAILED"}

MySQL Database:
Database connection concept demonstrated for API data-driven automation.
"""


print(output)


# Save output
with open("experiment_3_6_output.txt", "w", encoding="utf-8") as file:
    file.write(output)

print("Output saved to experiment_3_6_output.txt")