import requests
import os
import csv
from collections import OrderedDict


API_KEY = os.environ['API_KEY']
COMPANY_SEARCH_URL = 'https://api.hubapi.com/companies/v2/domains/'


headers = {"Content-Type": "application/json"}
querystring = {"hapikey": API_KEY}

payload = {
      "limit": 2,
      "requestOptions": {
        "properties": [
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

# output - none
delete_log = []
output_columns = ['companyId', 'deleted', 'reason']

domain = 'ethanalleninc.com'


with open(companies_to_delete_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        id = row['Company ID']
        req_url = '{}{}'.format(COMPANY_DELETE_URL, id)
        response = requests.request('POST', url=req_url,
                                    headers=headers, params=querystring)
        if response.status_code == 200:
            res = response.json()
            delete_log.append(res)
            print(res, '200')
        else:
            res = response.json()
            delete_log.append(res)
            print(res, response.status_code)

'''
with open(delete_log_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(delete_log)

'''

print('ok')