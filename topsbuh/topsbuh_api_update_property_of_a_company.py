import requests
import os
import re
import csv
import json
import time
from collections import namedtuple


API_KEY = os.environ['API_KEY']
ME_URL = 'https://api.hubapi.com/integrations/v1/me'
COMPANIES_PROPERTIES_URL = 'https://api.hubapi.com/properties/v1/companies/properties'
COMPANIES_URL = 'https://api.hubapi.com/companies/v2/companies/'
update_path = '/media/alxfed/toca/aa-crm/preparation/companies_to_update.csv'

# request data
data = {"properties": [
                        {
                          "name": "phone",
                          "value": ""
                        }
                      ]
        }

with open(update_path) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    tuple_headers = [re.sub('[^a-zA-Z_]', '_', h) for h in headers]
    Row = namedtuple('Row', tuple_headers)
    for r in f_csv:
        row = Row(*r)
        company_id = row.Company_ID
        data['properties'][0]['value'] = row.Phone_Number
        # data_json = json.dumps(data)
        api_access = "{}{}?hapikey={}".format(COMPANIES_URL, company_id, API_KEY)
        response = requests.put(url=api_access, json=data)

print('ok')