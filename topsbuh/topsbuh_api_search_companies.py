import requests
import os
import csv
from collections import OrderedDict
import hubspot


#API_KEY = os.environ['API_KEY']
API_KEY = hubspot.api_key
COMPANY_SEARCH_URL = 'https://api.hubapi.com/companies/v2/domains/'

headers = {"Content-Type": "application/json"}
querystring = {"hapikey": API_KEY}

payld = {
      "limit": 2,
      "requestOptions": {
        "properties": [  # list of parameters that will come in the response
          "domain",
          "createdate",
          "name",
          "hs_lastmodifieddate"
        ]
      },
      "offset": {
        "isPrimary": True,
        "companyId": 0
      }
    }

domain = 'ethanalleninc.com'

req_url = '{}{}/companies'.format(COMPANY_SEARCH_URL,domain)
response = requests.request('POST', url=req_url, headers=headers, json=payld, params=querystring)
if response.status_code == 200:
    res = response.json()
else:
    print(response.status_code)
print('ok')