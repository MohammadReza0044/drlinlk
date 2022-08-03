# connect to drlink.crm24.io via api.
# crm user = zargol ahmadi

import json
import requests
import hashlib


def get_token():
    url = "https://drlink.crm24.io/webservice.php?operation=getchallenge&username=zari.architect.eng@gmail.com"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    token = json.loads(response.text)
    token = token['result']['token']
    return (str(token + 'M4iv9zEiYXi6lZ')) 
    # token + crm accessKey


def sessionName():
    url = "https://drlink.crm24.io/webservice.php"
    login_token = get_token() 

    payload={'operation': 'login',
    'username': 'zari.architect.eng@gmail.com',
    'accessKey':hashlib.md5(login_token.encode('utf-8')).hexdigest(),}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    session_Name = json.loads(response.text)
    session_Name = session_Name['result']['sessionName']
    return(session_Name)



# url = "https://drlink.crm24.io/webservice.php"

# payload={'sessionName': sessionName(),
# 'operation': 'create',
# 'elementType': 'Leads',
# 'element': json.dumps({
#     "assigned_user_id": "19x8",
#     "lastname": 'test test',
#     "cf_1198":"test22@test.com",
#     "cf_1190":"سلام. من نیاز به مشاوره دارم.",
#     "creator":"19x1"
  
    
#   })

# }

# files=[

# ]
# headers = {}

# response = requests.request("POST", url, headers=headers, data=payload, files=files)

# print(response.text)



