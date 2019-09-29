import requests
import os
import csv
from collections import OrderedDict


API_KEY = os.environ['API_KEY']
COMPANY_DELETE_URL = 'https://api.hubapi.com/companies/v2/companies/'
companies_to_delete_path = '/home/alxfed/Documents/EthanAllen.csv'
delete_log_path = '/home/alxfed/Documents/EthanAllen_deleted_log.csv'


headers = {"Content-Type": "application/json"}
querystring = {"hapikey": API_KEY}

input_columns = ['Company ID', 'Last Modified Date', 'Lead Status', 'Total Revenue',
                 'Postal Code', 'Twitter Followers', 'Company Domain Name',
                 'Last Touch Converting Campaign', 'First Touch Converting Campaign',
                 'Recent Deal Close Date', 'Number of Pageviews',
                 'Number of Employees', 'Last Meeting Booked Campaign',
                 'Phone Unidentified', 'Time of Last Session', 'Time of First Visit',
                 'Close Date', 'Facebook Fans', 'Associated Deals',
                 'Recent Deal Amount', 'Number of times contacted',
                 'First Conversion Date', 'Original Source Type',
                 'First Deal Created Date', 'Number of Form Submissions',
                 'Last Meeting Booked Medium', 'Facebook Company Page', 'Create Date',
                 'LinkedIn Bio', 'First Conversion', 'Last Meeting Booked', 'City',
                 'Name', 'Number of child companies', 'Phone Toll', 'Number of Visits',
                 'Phone Number', 'Company owner', 'Phone Contact', 'Phone Landline',
                 'About Us', 'Last Activity Date', 'Next Activity Date',
                 'Last Meeting Booked Source', 'Owner Assigned Date', 'State/Region',
                 'Phone VoIP', 'Email address', 'LinkedIn Company Page',
                 'Total Money Raised', 'Phone Mobile', 'Associated Contacts',
                 'Original Source Data One', 'Target Account', 'Recent Conversion Date',
                 'Original Source Data Two', 'Lifecycle Stage', 'Last Contacted',
                 'Street Address', 'Recent Conversion', 'HubSpot Team', 'Twitter Bio',
                 'Web Technologies', 'Country', 'First Contact Create Date', 'Time Zone',
                 'Time Last Seen', 'Time First Seen', 'Type', 'Website URL',
                 'Year Founded', 'Twitter Handle', 'Google Plus Page', 'Days to Close',
                 'Description', 'Annual Revenue', 'Parent Company', 'Category',
                 'Industry', 'Street Address Two', 'Is Public', 'Associated Company ID',
                 'Associated Company']

# output - none
delete_log = []
output_columns = ['companyId', 'deleted', 'reason']


with open(companies_to_delete_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        id = row['Company ID']
        req_url = '{}{}'.format(COMPANY_DELETE_URL, id)
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

'''
with open(delete_log_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(delete_log)

'''

print('ok')