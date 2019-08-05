import requests
import os
import uuid
import pandas as pd
import json


ACCOUNT_ID = os.environ['ACCOUNT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
uu = str(uuid.uuid4())

data = {
        "method":"getAccounts",
        "params":
                {
                        "where":{"ownerID":"313468425"},
                        "limit":500,
                        "offset":0
                },
        "id": uu
        }

json_data = json.dumps(data)
api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
response = requests.post(url=api_access, json=data)

dict_of_account_parameters = response.json()['result']['account'][0] # the first company out of 500
keys = list(dict_of_account_parameters.keys())
for key in keys:
        print(key, dict_of_account_parameters[key])

print('ok')

'''
{"method":"getLeads",
 "params":{
 "where":{
  "emailAddress":"scottshsp@gmail.com"
 },
 "limit":500,
 "offset":0
},
"id":123
}
'''