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

def MakeParametersString(params_list, offset, limit):
    parameters_string = 'hapikey='+API_KEY
    for item in params_list:
        parameters_string = '{}&properties={}'.format(parameters_string, item)
    parameters_string = '{}&offset={}&limit={}'.format(parameters_string, offset, limit)
    return parameters_string

# company properties
req_properties = ['name', 'phone', 'phone_mobile', 'phone_voip',
                  'phone_toll','phone_landline','phone_unidentified',
                  'address','city','zip','state',
                  'category','website']

'''The complete list:
['Company ID', 'Last Modified Date', 'Lead Status', 'Total Revenue', 'Postal Code', 
'Twitter Followers', 'Company Domain Name', 'Last Touch Converting Campaign', 
'First Touch Converting Campaign', 'Recent Deal Close Date', 'Number of Pageviews', 
'Number of Employees', 'Last Meeting Booked Campaign', 'Phone Unidentified', 
'Time of Last Session', 'Time of First Session', 'Close Date', 'Facebook Fans', 
'Associated Deals', 'Recent Deal Amount', 'Number of times contacted', 
'First Conversion Date', 'Original Source Type', 'First Deal Created Date', 
'Number of Form Submissions', 'Last Meeting Booked Medium', 'Facebook Company Page', 
'Create Date', 'LinkedIn Bio', 'First Conversion', 'Last Meeting Booked', 
'City', 'Name', 'Number of child companies', 'Phone Toll', 'Number of Sessions', 
'Phone Number', 'Company owner', 'Phone Contact', 'Phone Landline', 'About Us', 
'Last Activity Date', 'Next Activity Date', 'Last Meeting Booked Source', 
'Owner Assigned Date', 'State/Region', 'Phone VoIP', 'Email address', 
'LinkedIn Company Page', 'Total Money Raised', 'Phone Mobile', 'Associated Contacts', 
'Original Source Data 1', 'Target Account', 'Recent Conversion Date', 
'Original Source Data 2', 'Lifecycle Stage', 'Last Contacted', 'Street Address', 
'Recent Conversion', 'HubSpot Team', 'Twitter Bio', 'Web Technologies', 'Country', 
'First Contact Create Date', 'Time Zone', 'Time Last Seen', 'Time First Seen', 'Type', 
'Website URL', 'Year Founded', 'Twitter Handle', 'Google Plus Page', 'Days to Close', 
'Description', 'Annual Revenue', 'Parent Company', 'Category', 'Industry', 
'Street Address 2', 'Is Public', 'Associated Company ID', 'Associated Company']
'''

# output
output_rows = []
output_columns = ["companyId", "isDeleted"]

# prepare for the pagination
has_more = True
offset = 0
limit = 250

while has_more:
    api_url = '{}?{}'.format(COMPANIES_URL, MakeParametersString(req_properties, offset, limit))
    response = requests.request("GET", url=api_url, headers=headers)
    if response.status_code == 200:
        res         = response.json()
        has_more    = res['has-more']
        offset      = res['offset']
        companies   = res['companies']
        for company in companies:
            row = dict()
            row.update({"companyId": company["companyId"],
                        "isDeleted": company["isDeleted"]})
            co_properties = company['properties']
            for co_property in co_properties:
                if co_property not in output_columns:
                    output_columns.append(co_property)
                row.update({co_property: co_properties[co_property]['value']})
            output_rows.append(row)
        print('offset: ', offset)
    else:
        print('Error: ', response.status_code)

downloaded_companies = DataFrame.from_records(data=output_rows, columns=output_columns)
with open(companies_downloaded_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(output_rows)

print('ok')