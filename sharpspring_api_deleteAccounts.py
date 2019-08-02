import requests
import os
import uuid
import pandas as pd
import numpy as np


ACCOUNT_ID = os.environ['ACCOUNT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
uu = str(uuid.uuid4())
company_data = pd.read_csv('/media/alxfed/toca/aa-crm/500company_ids_plus_plus.csv')
ids = company_data['id']

list_of_objects = []
for i in range(2, 412):
        list_of_objects.append({'id': str(ids[i])})

print('ok')
data = {
        "method":"deleteAccounts",
        "params":{"objects": list_of_objects},
        "id": uu
        }

print('ok')
api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
r = requests.post(url=api_access, json=data)

e = r.json()
#res = e['result']
print('ok')