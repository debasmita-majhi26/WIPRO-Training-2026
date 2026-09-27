import requests


session = requests.Session()


# Send GET request using session
response = session.get(
    "https://httpbin.org/cookies/set/student/module3"
)


# Get cookies from session
cookies = session.cookies


# Prepare output
output = f"""
Status Code: {response.status_code}

Session Cookies:
{cookies}

Cookie Value:
{cookies.get("student", "Not Found")}

Session Validation: {"PASSED" if "student" in cookies else "FAILED"}
"""


print(output)


# Save output
with open("experiment_3_5_output.txt", "w", encoding="utf-8") as file:
    file.write(output)

print("Output saved to experiment_3_5_output.txt")