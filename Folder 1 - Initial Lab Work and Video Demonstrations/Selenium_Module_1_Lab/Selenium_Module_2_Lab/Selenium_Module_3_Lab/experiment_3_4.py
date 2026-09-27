import requests


url = "https://jsonplaceholder.typicode.com/posts/1"


# PUT request
put_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated using PUT",
    "userId": 1
}

put_response = requests.put(url, json=put_data)


# PATCH request
patch_data = {
    "title": "Partially Updated Title"
}

patch_response = requests.patch(url, json=patch_data)


# DELETE request
delete_response = requests.delete(url)


output = f"""
PUT REQUEST
Status Code: {put_response.status_code}
Response: {put_response.json()}


PATCH REQUEST
Status Code: {patch_response.status_code}
Response: {patch_response.json()}


DELETE REQUEST
Status Code: {delete_response.status_code}


PUT Validation: {"PASSED" if put_response.status_code == 200 else "FAILED"}
PATCH Validation: {"PASSED" if patch_response.status_code == 200 else "FAILED"}
DELETE Validation: {"PASSED" if delete_response.status_code == 200 else "FAILED"}
"""


print(output)


with open("experiment_3_4_output.txt", "w", encoding="utf-8") as file:
    file.write(output)

print("Output saved to experiment_3_4_output.txt")