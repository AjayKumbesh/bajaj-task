import requests

url = "http://127.0.0.1:5000/bfhl"
payload = {
    "data": ["a", "1", "334", "4", "R", "$"]
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
