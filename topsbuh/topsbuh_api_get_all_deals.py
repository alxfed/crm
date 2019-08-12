import requests
import os
import re
import csv
import json
import time
from collections import namedtuple


API_KEY = os.environ['API_KEY']
# https://api.hubapi.com/deals/v1/deal/paged?hapikey=demo&includeAssociations=true&limit=2&properties=dealname
DEAL_URL = 'https://api.hubapi.com/deals/v1/deal/paged'
file_path = '/media/alxfed/toca/aa-crm/preparation/all_deals_now.csv'

# request data
payload = {
    'hapikey': API_KEY,
    'includeAssociations':True,
    'limit':2,
    'properties':
        [
            'dealname',
            'closedate'
        ]
}

response = requests.get(url=DEAL_URL, params=payload)
got_it = response.json()

print('ok')