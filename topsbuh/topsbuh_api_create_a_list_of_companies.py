import requests
import os
import re
import csv
import json
import time
from collections import OrderedDict


API_KEY = os.environ['API_KEY']
ME_URL = 'https://api.hubapi.com/integrations/v1/me'
COMPANIES_PROPERTIES_URL = 'https://api.hubapi.com/properties/v1/companies/properties'
COMPANIES_URL = 'https://api.hubapi.com/companies/v2/companies'
companies_to_create_path = '/media/alxfed/toca/aa-crm/uploads/companies_to_create.csv'
companies_created_path = '/media/alxfed/toca/aa-crm/uploads/companies_created.csv'

headers = {"Content-Type": "application/json"}
querystring = {"hapikey": API_KEY}

# mapping of fields
hubspot_mapping = {
    'Name': 'name',
    'Type': 'type',
    'Phone Number': 'phone',
    'Phone Mobile': 'phone_mobile',
    'Phone VoIP': 'phone_voip',
    'Phone Toll': 'phone_toll',
    'Phone Landline': 'phone_landline',
    'Phone Unidentified': 'phone_unidentified',
    'Address': 'address',
    'City': 'city',
    'Zipcode': 'zip',
    'State': 'state',
    'Category': 'category',
    'Website': 'website',
    'Facebook': 'facebook_company_page',
    'Twitter': 'twitterhandle',
    'Google': 'googleplus_page',
    'Linkedin': 'linkedin_company_page'
}

# request data
data = {"properties": []}

# output
output_rows = []
output_columns = ['Name', 'Type', 'Phone Number', 'Phone Mobile',
           'Phone VoIP', 'Phone Toll', 'Phone Landline',
           'Phone Unidentified', 'Address', 'City', 'Zipcode',
           'State', 'Category', 'Website', 'Facebook',
           'Twitter', 'Google', 'Linkedin', 'companyId']

with open(companies_to_create_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        list_of_properties = []
        for key in row:
            prop = {"name": hubspot_mapping[key],
                    "value": row[key]}
            list_of_properties.append(prop)
        data['properties'] = list_of_properties
        response = requests.request("POST", url=COMPANIES_URL, json=data,
                                    headers=headers, params=querystring)
        if response.status_code == 200:
            row.update({'companyId': response.json()['companyId']})
            output_rows.append(row)
            print('ok')
        else:
            print('not ok! ', response.status_code)

with open(companies_created_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(output_rows)

print('ok')