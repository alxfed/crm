import requests
import os
import csv
from collections import OrderedDict


API_KEY = os.environ['API_KEY']
CONTACT_CREATE_OR_UPDATE_URL = 'https://api.hubapi.com/contacts/v1/contact/createOrUpdate/email/'
CONNECTION_CREATE_URL = 'https://api.hubapi.com/crm-associations/v1/associations'
companies_created_with_emails_path = '/media/alxfed/toca/aa-crm/kb-remodelers/upload/second_thousand_with_emails_one.csv'
contacts_created_path = '/media/alxfed/toca/aa-crm/kb-remodelers/upload/kitchen_and_bath_remodelers_second_thousand_contacts_created.csv'

headers = {"Content-Type": "application/json"}
querystring = {"hapikey": API_KEY}

input_columns = ['Name', 'Type', 'Phone Number', 'Phone Contact', 'Phone Mobile',
                 'Phone Voip', 'Phone Toll', 'Phone Landline',
                 'Phone Unknown', 'Address', 'City',
                 'Zipcode', 'State', 'Category', 'Website',
                 'Facebook', 'Twitter', 'Google', 'Linkedin',
                 'companyId', 'emails']

# contact create request data
data = {'properties':
    [
        {
          "property": "firstname",
          "value": ""
        },
        {
          "property": "lastname",
          "value": ""
        },
        {
          "property": "company",
          "value": ""
        },
        {
          "property": "jobtitle",
          "value": "Kitchen & Bath Designer employee"
        }
    ]
}

# connection data

connection_data = {
  "fromObjectId": '',
  "toObjectId": '',
  "category": "HUBSPOT_DEFINED",
  "definitionId": 2
}

# output
output_rows = []
output_columns = ['Name', 'companyId', 'firstname', 'lastname', 'email', 'vid', 'connected']
enu = 8300


with open(companies_created_with_emails_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        output_row = OrderedDict()
        output_row['Name'] = row['Name']
        companyId = row['companyId']
        output_row['companyId'] = companyId
        list_of_emails = row['emails'].split(' ')
        for email in list_of_emails:
            name, _ = email.split('@')
            lastname = 'Auto_' + str(enu+1)
            enu += 1
            output_row['firstname'] = name
            output_row['lastname'] = lastname
            output_row['email'] = email
            data['properties'][0]['value'] = name
            data['properties'][1]['value'] = lastname
            data['properties'][2]['value'] = row['Name']
            req_url = '{}{}/'.format(CONTACT_CREATE_OR_UPDATE_URL, email)
            response = requests.request("POST", url=req_url, json=data,
                                        headers=headers, params=querystring)
            if response.status_code == 200:
                vid = response.json()['vid']
                output_row['vid'] = vid
                connection_data['fromObjectId'] = companyId
                connection_data['toObjectId'] = vid
                resp = requests.request("PUT", url=CONNECTION_CREATE_URL, json=connection_data,
                                        headers=headers, params=querystring)
                if resp.status_code == 204:
                    output_row['connected'] = True
                else:
                    output_row['connected'] = False
            else:
                output_row['vid'] = ''
                output_row['connected'] = False
            output_rows.append(output_row)
            print(output_row, resp.status_code)

with open(contacts_created_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(output_rows)

print('Big OK')