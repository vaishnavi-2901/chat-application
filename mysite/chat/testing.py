import requests

url = "http://localhost:8001/chat/"

# payload = "{\"email\":\"vaishnavi@attentive.ai\",\"password\":\"Password!123\"}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers)

print(response.text)
