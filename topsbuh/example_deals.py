import os
import requests
import json

API_KEY = os.environ['API_KEY']
url= 'https://api.hubapi.com/deals/v1/deal?hapikey='
access = '{}{}'.format(url, API_KEY)
headers={}
headers["Content-Type"]="application/json"
data = json.dumps({
  "associations": {
    "associatedCompanyIds": [
      8954037
    ],
    "associatedVids": [
      27136
    ]
  },
  "properties": [
    {
      "value": "Tim's Newer Deal",
      "name": "dealname"
    },
    {
      "value": "appointmentscheduled",
      "name": "dealstage"
    },
    {
      "value": "default",
      "name": "pipeline"
    },
    {
      "value": "24",
      "name": "hubspot_owner_id"
    },
    {
      "value": 1409443200000,
      "name": "closedate"
    },
    {
      "value": "60000",
      "name": "amount"
    },
    {
      "value": "newbusiness",
      "name": "dealtype"
    }
  ]
})

r=requests.post(url, headers = headers, data = data)

print(r.status_code)