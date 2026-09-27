import requests


# GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Print response status
print("Status Code:", response.status_code)

# Print response data as JSON
print("Response JSON:")
print(response.json())