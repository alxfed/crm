import requests
import os
from collections import OrderedDict


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

hasmore = True
rows = {}

while hasmore:
    chunk = OrderedDict()
    response = requests.get(url=DEAL_URL, params=payload)
    read_in = response.json()
    chunk = read_in['deals']
    hasmore = read_in['hasMore']

print('ok')