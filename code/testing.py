import requests

headers = {
    "Authorization": "Bearer 65bd66b3-f19b-464e-adc1-10131c37129a"
}

url = "https://api.balldontlie.io/v1/players?search=lebron"
response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Text:", response.text)
