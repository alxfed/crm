import requests
import os
import uuid
import pandas as pd
import json


ACCOUNT_ID = os.environ['ACCOUNT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
uu = str(uuid.uuid4())
data = {
        "method":"getAccount",
        "params":
                {
                  "id":"7745634306"
                },
        "id": uu
        }

json_data = json.dumps(data)
api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
response = requests.post(url=api_access, json=data)

dict_of_account_parameters = response.json()['result']['account'][0]
keys = list(dict_of_account_parameters.keys())
for key in keys:
        print(key, dict_of_account_parameters[key])

print('ok')

# df.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/500company_ids_plus_plus.csv', index=False)