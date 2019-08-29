import requests
import os
import csv
from collections import OrderedDict


API_KEY = os.environ['API_KEY']
CONTACT_DELETE_URL = 'https://api.hubapi.com/contacts/v1/contact/vid/'
contacts_to_delete_path = '/media/alxfed/toca/aa-crm/arch-des-employees/good_job_processed_rest_emails.csv'
delete_log_path = '/media/alxfed/toca/aa-crm/arch-des-employees/deleted_log.csv'



headers = {"Content-Type": "application/json"}
querystring = {"hapikey": API_KEY}

input_columns = ['Email Domain', 'Associated Company ID', 'Associated Company',
                 'Last Name', 'Lifecycle Stage', 'Job Title', 'First Name',
                 'email_class', 'Contact ID', 'Email', 'Company Name', 'Email Two']

# output - none
delete_log = []
output_columns = ['vid', 'deleted', 'reason']


with open(contacts_to_delete_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        if row['email_class'] == 'False':
            id = row['Contact ID']
            req_url = '{}{}'.format(CONTACT_DELETE_URL, id)
            response = requests.request("DELETE", url=req_url,
                                        headers=headers, params=querystring)
            if response.status_code == 200:
                res = response.json()
                delete_log.append(res)
                print(res, '200')
            else:
                res = response.json()
                delete_log.append(res)
                print(res, response.status_code)
        else:
            pass

'''
with open(delete_log_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(delete_log)

'''

print('ok')