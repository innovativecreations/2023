import requests

header = {
    "x-api-key": "mayank"
}

r = requests.get("https://xapi.mmareg.com/", headers=header)

print(r.text)

