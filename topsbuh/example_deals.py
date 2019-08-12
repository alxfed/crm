import os
import requests
import json

API_KEY = os.environ['API_KEY']
url= 'https://api.hubapi.com/deals/v1/deal/923367048?hapikey='
access_url = '{}{}'.format(url, API_KEY)
headers={}
headers["Content-Type"]="application/json"
data = json.dumps(
  {"properties":
     [
       {
         "name": "closedate",
         "value": 1561006800000
        }
     ]
  })

r=requests.put(access_url, headers = headers, data = data)

print(r.status_code)