import requests
import os
import re
import csv
import json
import time
from collections import OrderedDict
from pandas import DataFrame


API_KEY = os.environ['API_KEY']

COMPANIES_URL = 'https://api.hubapi.com/companies/v2/companies/paged'
companies_downloaded_path = '/media/alxfed/toca/aa-crm/enrich/companies_downloaded.csv'

headers = {"Content-Type": "application/json"}

def MakeParametersString(params_list, offset, limit):
    parameters_string = 'hapikey='+API_KEY
    for item in params_list:
        parameters_string = '{}&properties={}'.format(parameters_string, item)
    parameters_string = '{}&offset={}&limit={}'.format(parameters_string, offset, limit)
    return parameters_string

# company parameters
all_params = ['name', 'phone', 'phone_mobile', 'phone_voip',
              'phone_toll','phone_landline','phone_unidentified',
              'address','city','zip','state',
              'category','website']

# output
output_rows = []
output_columns = ['Name', 'Type', 'Phone Number', 'Phone Mobile',
           'Phone VoIP', 'Phone Toll', 'Phone Landline',
           'Phone Unidentified', 'Address', 'City', 'Zipcode',
           'State', 'Category', 'Website']

# prepare for the pagination
has_more = True
offset = 0
limit = 250

while has_more:
    api_url = '{}?{}'.format(COMPANIES_URL, MakeParametersString(all_params, offset, limit))
    response = requests.request("GET", url=api_url, headers=headers)
    if response.status_code == 200:
        res         = response.json()
        has_more    = res['has-more']
        offset      = res['offset']
        companies   = res['companies']
        for company in companies:
            row = OrderedDict()
            company_properties = company['properties']
            # name = company_properties['name']['value']
            row.update({'Name': company_properties['name']['value']})
            # and other parameters like this                ^
            output_rows.append(row)
        print('offset: ', offset)
    else:
        print(response.status_code)

all_companies = DataFrame.from_records(output_rows)
with open(companies_downloaded_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(output_rows)

print('ok')