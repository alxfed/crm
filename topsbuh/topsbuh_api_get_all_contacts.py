import requests
import os
import re
import csv
import json
import time
from pandas import DataFrame


API_KEY = os.environ['API_KEY']

CONTACTS_URL = 'https://api.hubapi.com/contacts/v1/lists/all/contacts/all'
downloaded_contacts_path = '/media/alxfed/toca/aa-crm/enrich/contacts_downloaded.csv'

headers = {"Content-Type": "application/json"}

def make_parameters_string(params_list, vidOffset, count):
    parameters_string = 'hapikey='+API_KEY
    for item in params_list:
        parameters_string = '{}&property={}'.format(parameters_string, item)
    parameters_string = '{}&vidOffset={}&count={}'.format(parameters_string, vidOffset, count)
    return parameters_string

# contact parameters
req_params = ['firstname', 'lastname', 'email', 'email_two',
              'jobtitle', 'company', 'phone', 'mobilephone',
              'city','zip','state', 'hs_lead_status']

# output
output_rows = []
output_columns = ['vid', 'is_contact',
                  'firstname', 'lastname', 'email', 'email_two',
                  'jobtitle', 'company', 'phone', 'mobilephone',
                  'city','zip','state', 'hs_lead_status']

# prepare for the pagination
has_more = True
vidOffset = 0
count = 100           # max 100

while has_more:
    api_url = '{}?{}'.format(CONTACTS_URL, make_parameters_string(req_params, vidOffset, count))
    response = requests.request("GET", url=api_url, headers=headers)
    if response.status_code == 200:
        res         = response.json()
        has_more    = res['has-more']
        vidOffset   = res['vid-offset']
        contacts    = res['contacts']
        for contact in contacts:
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
    else:
        print(response.status_code)

all_contacts = DataFrame.from_records(data=output_rows, columns=output_columns)
with open(downloaded_contacts_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(output_rows)

all_contacts.to_csv('/media/alxfed/toca/aa-crm/enrich/contacts_dataframe.csv', index=False)

print('ok')