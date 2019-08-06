import requests
import os
import uuid
import pandas as pd
import json


ACCOUNT_ID = os.environ['ACCOUNT_ID']
SECRET_KEY = os.environ['SECRET_KEY']


def RequestAccounts(**kwargs):
        id      = kwargs.get('id', None)
        ownerID = kwargs.get('ownerID', None)
        data = {"method": "getAccounts", "params":{"limit": "500", "offset": ""}, "id": ""}
        if id or ownerID:
            if id:
                where = {'where': str(id)}
                data['params'].update(where)
            elif ownerID:
                where = {'where': str(ownerID)}
                data["params"].update(where)
            else:
                raise

        api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
        page = 0
        while not done:
            data['offset'] = page * 500
            data['id'] = str(uuid.uuid4())
            json_data = json.dumps(data)
            response = requests.post(url=api_access, json=json_data)

            result  = response.json()['result']
            error   = response.json()['error']
            id      = response.json()['id']         # the first company out of 500
            keys = list(result['account'][0].keys())
            for key in keys:
                print(key, result['account'][0][key])
                account_data = 0

            page += 1
            if result[]:
                done = True

        return account_data

a = RequestAccounts(ownerID = 313468425)

print('ok')

'''
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
'''