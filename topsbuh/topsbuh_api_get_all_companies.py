import requests
import os
import re
import csv
import json
import time
from pandas import DataFrame


API_KEY = os.environ['API_KEY']

COMPANIES_URL = 'https://api.hubapi.com/companies/v2/companies/paged'
companies_downloaded_path = '/media/alxfed/toca/aa-crm/enrich/companies_downloaded.csv'

headers = {"Content-Type": "application/json"}

def make_parameters_string(offset, limit):
    par_string = 'hapikey='+API_KEY
    parameters_string = '{}{}&offset={}&limit={}'.format(par_string, parameters_substring,
                                                         offset, limit)
    return parameters_string

# company parameters
all_params = ['name', 'phone', 'phone_mobile', 'phone_voip',
              'phone_toll','phone_landline','phone_unidentified',
              'address','city','zip','state',
              'category','website']

parameters_substring = ''
for item in all_params:
    parameters_substring = '{}&properties={}'.format(parameters_substring, item)

# output
output_rows = []
output_columns = ['companyId', 'isDeleted', 'name', 'type',
                  'phone', 'phone_mobile', 'phone_voip',
                  'phone_toll','phone_landline','phone_unidentified',
                  'address','city','zip','state', 'category','website']

# prepare for the pagination
has_more = True
offset = 0
limit = 250  # 250 is a maximum

while has_more:
    api_url = '{}?{}'.format(COMPANIES_URL, make_parameters_string(offset, limit))
    response = requests.request("GET", url=api_url, headers=headers)
    if response.status_code == 200:
        res         = response.json()
        has_more    = res['has-more']
        offset      = res['offset']
        companies   = res['companies']
        for company in companies:
            row = {}
            row.update({"companyId": company["companyId"],
                        "isDeleted": company["isDeleted"]})
            co_properties = company['properties']
            for co_property in co_properties:
                if co_property not in output_columns:
                    output_columns.append(co_property)
                    print('Appending a property to output colunms list: ', co_property)
                row.update({co_property: co_properties[co_property]['value']})
            output_rows.append(row)
        print('offset: ', offset)
    else:
        print(response.status_code)

all_companies = DataFrame.from_records(data=output_rows, columns=output_columns)

with open(companies_downloaded_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(output_rows)

all_companies.to_csv('/media/alxfed/toca/aa-crm/enrich/companies_dataframe.csv', index=False)

print('ok')