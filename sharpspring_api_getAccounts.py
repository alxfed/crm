import requests
import os
import uuid
import pandas as pd


ACCOUNT_ID = os.environ['ACCOUNT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
uu = str(uuid.uuid4())
data = {
        "method":"getAccounts",
        "params":
                {
                  "where":''
                },
        "id": uu
        }
api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
r = requests.post(url=api_access, json=data)

e = r.json()
res = e['result']
list_of_accounts = res['account']
df = pd.DataFrame(list_of_accounts)
df.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/500company_ids.csv', index=False)