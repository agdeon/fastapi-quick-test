import requests

url = "http://127.0.0.1:8000/post_test/"
data = {
    "id": 343432,
    "name": "Andrew",
    "price": 1441.57,
    "description": "Some text in description..",
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.json()["message"])
else:
    print(f"Error: {response.status_code}, {response.text}")