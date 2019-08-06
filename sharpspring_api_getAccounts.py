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
                where.update('"where": {"id": {}}'.format(str(id)))
            else:
                where.update('"where": {"ownerID": {}}'.format(str(ownerID)))

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

        result  = response.json()['result']
        error   = response.json()['error']
        id      = response.json()['id']         # the first company out of 500

        keys = list(result['account'][0].keys())
        for key in keys:
                print(key, result['account'][0][key])
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