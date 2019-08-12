"""
datetime to unix
https://docs.python.org/3/library/datetime.html
"""
import requests
import os
import re
import csv
import json
import time
from collections import namedtuple
from datetime import datetime

API_KEY = os.environ['API_KEY']
ME_URL = 'https://api.hubapi.com/integrations/v1/me'
DEAL_URL = 'https://api.hubapi.com/deals/v1/deal/'
update_path = '/media/alxfed/toca/aa-crm/preparation/hubspot-crm-exports-all-deals-2019-08-12.csv'
hdrs = {}

# request data
data = {
          "properties":   [
                            {
                              "name": "closedate",
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
        deal_id = row.Deal_ID
        date = datetime.fromisoformat(row.Permit_Issue_Date)
        data['properties'][0]['value'] = int(1000*date.timestamp())
        data_json = json.dumps(data)
        api_access = "{}{}?hapikey={}".format(DEAL_URL, deal_id, API_KEY)
        print(data_json)
        hdrs["Content-Type"] = "application/json"
        response = requests.put(url=api_access, headers=hdrs, data=data_json)

print('ok')
