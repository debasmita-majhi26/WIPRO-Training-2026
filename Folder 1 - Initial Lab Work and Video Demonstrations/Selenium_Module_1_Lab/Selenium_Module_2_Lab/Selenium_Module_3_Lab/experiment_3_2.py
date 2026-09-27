import requests


# Send GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")


# Prepare output
output = f"""
Status Code: {response.status_code}

Response Headers:
{response.headers}

Response JSON:
{response.json()}

Status Code Validation: {"PASSED" if response.status_code == 200 else "FAILED"}
"""


# Display output in terminal
print(output)


# Save output to a text file
with open("experiment_3_2_output.txt", "w", encoding="utf-8") as file:
    file.write(output)

print("Output saved to experiment_3_2_output.txt")