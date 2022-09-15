import requests

res = requests.get("https://raw.githubusercontent.com/marzookh/cmput404Lab1/main/request_version.py")
print(res.text)
