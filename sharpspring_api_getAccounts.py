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
        if id or ownerID:
                where = {}
                if id:
                        where.append('"where": {"id": str(id)}')

        api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
        uid = str(uuid.uuid4())
        data = {
                "method": "getAccounts",
                "params":
                        {
                                "where": {"ownerID": "313468425"},
                                "limit": 500,
                                "offset": 0
                        },
                "id": uid
        }
        json_data = json.dumps(data)
        response = requests.post(url=api_access, json=json_data)

        dict_of_account_parameters = response.json()['result']['account'][0]  # the first company out of 500
        keys = list(dict_of_account_parameters.keys())
        for key in keys:
                print(key, dict_of_account_parameters[key])
        account_data = 0
        return account_data

a = RequestAccounts(id = 313468425)

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