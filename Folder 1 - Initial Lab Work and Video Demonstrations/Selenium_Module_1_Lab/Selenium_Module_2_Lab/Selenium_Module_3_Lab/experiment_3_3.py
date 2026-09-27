import requests


url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Python API Test",
    "body": "This is a POST request",
    "userId": 1
}

headers = {
    "Content-Type": "application/json"
}


response = requests.post(
    url,
    json=payload,
    headers=headers
)


output = f"""
Status Code: {response.status_code}

Response Headers:
{response.headers}

Response JSON:
{response.json()}

POST Request Validation: {"PASSED" if response.status_code == 201 else "FAILED"}
"""


print(output)


with open("experiment_3_3_output.txt", "w", encoding="utf-8") as file:
    file.write(output)

print("Output saved to experiment_3_3_output.txt")