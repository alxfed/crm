'''
template
'''

import pandas as pd

data = pd.read_csv('/media/alxfed/toca/aa-crm/old-contacts.csv')

input_headers = ['Company ID', 'Last Modified Date', 'Lead Status', 'Total Revenue',
               'Postal Code', 'Twitter Followers', 'Company Domain Name',
               'Last Touch Converting Campaign', 'First Touch Converting Campaign',
               'Recent Deal Close Date', 'Number of Pageviews', 'Number of Employees',
               'Time of Last Session', 'Time of First Visit', 'Close Date',
               'Facebook Fans', 'Associated Deals', 'Recent Deal Amount',
               'Number of times contacted', 'Original Source Type',
               'First Deal Created Date', 'Facebook Company Page', 'Create Date',
               'LinkedIn Bio', 'City', 'Name', 'Number of child companies',
               'Number of Visits', 'Phone Number', 'Company owner', 'About Us',
               'Last Activity Date', 'Next Activity Date', 'Owner Assigned Date',
               'State/Region', 'Email address', 'LinkedIn Company Page',
               'Total Money Raised', 'Associated Contacts', 'Original Source Data 1',
               'Target Account', 'Original Source Data 2', 'Lifecycle Stage',
               'Last Contacted', 'Street Address', 'HubSpot Team', 'Twitter Bio',
               'Web Technologies', 'Country', 'First Contact Create Date',
               'Type Contractor', 'Time Zone', 'Time Last Seen', 'Time First Seen',
               'Type', 'Website URL', 'Year Founded', 'Twitter Handle',
               'Google Plus Page', 'Days to Close', 'Description', 'Annual Revenue',
               'Parent Company', 'Industry', 'Street Address 2', 'Is Public',
               'Associated Company ID', 'Associated Company']

''' will not be used:
           'Last Modified Date', 'Lead Status', 
           'Twitter Followers', 'Company Domain Name',
           'Last Touch Converting Campaign', 'First Touch Converting Campaign',
           'Recent Deal Close Date', 'Number of Pageviews', 'Number of Employees',
           'Time of Last Session', 'Time of First Visit', 'Close Date',
           'Facebook Fans', 'Associated Deals', 'Recent Deal Amount',
           'Number of times contacted', 'Original Source Type',
           'First Deal Created Date', 'Facebook Company Page', 
           'LinkedIn Bio', 'Number of child companies',
           'Number of Visits', 'Company owner', 'About Us',
           'Last Activity Date', 'Next Activity Date', 'Owner Assigned Date',
           'Email address', 'LinkedIn Company Page',
           'Total Money Raised', 'Original Source Data 1',
           'Target Account', 'Original Source Data 2', 'Lifecycle Stage',
           'Last Contacted', 'HubSpot Team', 'Twitter Bio',
           'Web Technologies', 'First Contact Create Date',
           'Type Contractor', 'Time Zone', 'Time Last Seen', 'Time First Seen',
           'Type', 'Year Founded', 'Twitter Handle',
           'Google Plus Page', 'Days to Close', 'Annual Revenue',
           'Parent Company', 'Industry', 'Is Public',
           'Associated Company ID', 'Associated Company'
'''

mapping = {}

output_headers = ['','']

output = pd.DataFrame()

email = contacts_data.loc[contacts_data['Contact CRM ID']==crm_id]['Email Address'].values[0]


print(contacts_data_frame)