import json
import requests
import hashlib


def get_token():
    url = "https://drlink.crm24.io/webservice.php?operation=getchallenge&username=hi@drlink.ir"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    token = json.loads(response.text)
    token = token['result']['token']
    return (str(token))



url = "https://drlink.crm24.io/webservice.php"

payload={'operation': 'login',
'username': 'hi@drlink.ir',
'accessKey':hashlib.md5('vtTd7NZiOKnAMhUget_token()'.encode('utf-8')).hexdigest(),}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
# print(payload)
print(response.text)

