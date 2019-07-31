import requests
import os
import uuid


ACCOUNT_ID = os.environ['ACCOUNT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
uu = str(uuid.uuid4())
data = {
    "method":"getLead",
    "params":
            {
              "id":"673960212482"
            },
    "id": uu
    }
api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
r = requests.post(url=api_access, json=data)

e = r.json()
res = e['result']
di = res['lead'][0]
who = di['firstName']
print(who)