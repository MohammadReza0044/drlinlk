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
    return (str(token + 'vtTd7NZiOKnAMhU'))


def sessionName():
    url = "https://drlink.crm24.io/webservice.php"
    login_token = get_token() 

    payload={'operation': 'login',
    'username': 'hi@drlink.ir',
    'accessKey':hashlib.md5(login_token.encode('utf-8')).hexdigest(),}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    session_Name = json.loads(response.text)
    session_Name = session_Name['result']['sessionName']
    return(session_Name)



url = "https://drlink.crm24.io/webservice.php"

payload={'sessionName': sessionName(),
'operation': 'create',
'elementType': 'Contacts',
'element': json.dumps({
    "assigned_user_id": "19x1",
    "firstname": "mohammad reza",
    "lastname": "shaygan",
    "mobile": "09370946898",
    "salutationtype": "mr"
  })

}

files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)



