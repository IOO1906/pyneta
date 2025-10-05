import requests

url = "https://httpbin.org/get"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Resonse Body:", response.text)


