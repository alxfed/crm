import requests
import os
import re
import csv
import json
import time
import pandas as pd
from collections import OrderedDict


API_KEY = os.environ['API_KEY']
COMPANIES_PROPERTIES_URL = 'https://api.hubapi.com/properties/v1/companies/properties'
CONTACT_CREATE_OR_UPDATE_URL = 'https://api.hubapi.com/contacts/v1/contact/createOrUpdate/email/'
companies_created_with_emails_path = '/media/alxfed/toca/aa-crm/uploads/companies_created_with_emails.csv'
contacts_created_path = '/media/alxfed/toca/aa-crm/uploads/contacts_created.csv'

headers = {"Content-Type": "application/json"}
querystring = {"hapikey": API_KEY}

input_columns = ['Name', 'Type', 'Phone Number', 'Phone Mobile',
                 'Phone VoIP', 'Phone Toll', 'Phone Landline',
                 'Phone Unidentified', 'Address', 'City',
                 'Zipcode', 'State', 'Category', 'Website',
                 'Facebook', 'Twitter', 'Google', 'Linkedin',
                 'companyId', 'emails']

# request data
data = {'properties':
    [
        {
          "property": "firstname",
          "value": ""
        },
        {
          "property": "lastname",
          "value": "Auto"
        },
        {
          "property": "company",
          "value": ""
        },
        {
          "property": "jobtitle",
          "value": "Architect & Designer employee"
        }
    ]
}

# output
output_rows = []
output_columns = ['Name', 'companyId', 'firstname', 'email', 'vid']
output_row = OrderedDict

with open(companies_created_with_emails_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        output_row.update({'Name': row['Name']})
        output_row.update({'companyId': row['companyId']})
        list_of_emails = row['emails'].split(' ')
        for email in list_of_emails:
            name, domain = email.split('@')
            output_row.update({'firstname'})
            data['properties'][0]['value'] = name
            data['properties'][2]['value'] = row['Name']
            req_url = '{}{}/'.format(CONTACT_CREATE_OR_UPDATE_URL, email)
            response = requests.request("POST", url=req_url, json=data,
                                        headers=headers, params=querystring)
        if response.status_code == 200:
            output_row.update({'companyId': response.json()['companyId']})
            output_rows.append(row)
            print('ok')
        else:
            print('not ok! ', response.status_code)


with open(contacts_created_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(output_rows)

print('ok')