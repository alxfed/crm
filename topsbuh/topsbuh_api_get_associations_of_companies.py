import requests
import os
import re
import csv
import json
import time
from pandas import DataFrame


API_KEY = os.environ['API_KEY']

ASSOCIATIONS_URL = 'https://api.hubapi.com/crm-associations/v1/associations/'
ASSOCIATIONS_TYPE = '/HUBSPOT_DEFINED/1'
companies_path = '/media/alxfed/toca/aa-crm/enrich/companies_downloaded.csv'
downloaded_associations_path = '/media/alxfed/toca/aa-crm/enrich/associations_downloaded.csv'

headers = {"Content-Type": "application/json"}

def make_parameters_string(offset, limit):
    parameters_string = 'hapikey='+API_KEY
    parameters_string = '{}&offset={}&limit={}'.format(parameters_string, offset, limit)
    return parameters_string

# output
output_rows = []
output_columns = ['companyId', 'associations']

# prepare for the pagination
offset = 0
limit = 100           # max 100

with open(companies_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        has_more = True
        while has_more:
            api_url = '{}{}{}?{}'.format(ASSOCIATIONS_URL,
                                         row['companyId'],
                                         ASSOCIATIONS_TYPE,
                                         make_parameters_string(offset, limit))
            response = requests.request("GET", url=api_url, headers=headers)
            if response.status_code == 200:
                res         = response.json()
                has_more    = res['hasMore']
                offset   = res['offset']
                associations = res['results']
                if associations:
                    output_row = dict()
                    output_row.update({'companyId': row['companyId'],
                                       'associations': associations})
                    output_rows.append(output_row)
                    print('CompanyId:', row['companyId'], associations)
                '''
                for association in associations:
                    row = {}
                    row.update({"vid": contact["vid"],
                                "is_contact": contact["is-contact"]})
                    co_properties = contact['properties']
                    for co_property in co_properties:
                        if co_property not in output_columns:
                            output_columns.append(co_property)
                            print('Adding a property to colunms list: ', co_property)
                        row.update({co_property: co_properties[co_property]['value']})
                    output_rows.append(row)
                print('vidOffset: ', vidOffset)
                '''
            else:
                print('Error: ', response.status_code)

all_contacts = DataFrame.from_records(data=output_rows, columns=output_columns)
with open(downloaded_associations_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(output_rows)

all_contacts.to_csv('/media/alxfed/toca/aa-crm/enrich/contacts_dataframe.csv', index=False)

print('ok')