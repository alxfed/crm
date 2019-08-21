import requests
import os
import csv
from collections import OrderedDict


API_KEY = os.environ['API_KEY']
CONTACT_CREATE_OR_UPDATE_URL = 'https://api.hubapi.com/contacts/v1/contact/createOrUpdate/email/'
contacts_to_create_path = '/media/alxfed/toca/aa-crm/enrich/all_agents.csv'
contacts_created_path = '/media/alxfed/toca/aa-crm/enrich/contacts_created.csv'

headers = {"Content-Type": "application/json"}
querystring = {"hapikey": API_KEY}

input_columns = ['Agent Name', 'Agent ID', 'Agent Phone', 'Agent Email']

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
          "property": "phone",
          "value": ""
        },
        {
          "property": "email_two",
          "value": ""
        },
        {
          "property": "external_id",
          "value": ""
        },
        {
          "property": "lifecyclestage",
          "value": "lead"
        },
        {
          "property": "jobtitle",
          "value": "Realtor"
        }
    ]
}

# output
output_rows = []
output_columns = ['firstname', 'lastname', 'phone', 'email', 'email_two', 'external_id', 'vid']


with open(contacts_to_create_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        output_row = OrderedDict()
        firstname, lastname = row['Agent Name'].split(' ')
        output_row['firstname']  = firstname
        output_row['lastname'] = lastname
        phone = row['Agent Phone']
        output_row['phone'] = phone
        list_of_emails = row['Agent Email'].split(';')
        if len(list_of_emails) > 1:
            email_two = list_of_emails[1]
        else:
            email_two = ''
        email = list_of_emails[0]
        output_row['email'] = email
        output_row['email_two'] = email_two
        external_id = row['Agent ID']
        output_row['external_id'] = external_id
        data['properties'][0]['value'] = firstname
        data['properties'][1]['value'] = lastname
        data['properties'][2]['value'] = phone
        data['properties'][3]['value'] = email_two
        data['properties'][4]['value'] = external_id
        req_url = '{}{}/'.format(CONTACT_CREATE_OR_UPDATE_URL, email)
        response = requests.request("POST", url=req_url, json=data,
                                    headers=headers, params=querystring)
        if response.status_code == 200:
            vid = response.json()['vid']
            output_row['vid'] = vid
        else:
            output_row['vid'] = ''
        output_rows.append(output_row)
        print(output_row, response.status_code)

with open(contacts_created_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(output_rows)

print('ok')