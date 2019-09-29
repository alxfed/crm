import requests
import os
import csv
from collections import OrderedDict
import hubspot


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

request_url = f'{hubspot.COMPANY_SEARCH_URL}{domain}/companies' #.format(hubspot.COMPANY_SEARCH_URL, domain)
response = requests.request('POST', url=request_url,
                            headers=hubspot.hbsp_headr,
                            json=payld,
                            params=hubspot.hbsp_param)
if response.status_code == 200:
    res = response.json()
else:
    print(response.status_code)
print('ok')