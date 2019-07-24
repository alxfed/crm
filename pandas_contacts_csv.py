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

owner_to_email = {
    'Melissa Conroy':	'mconroy@marfacabinets.com',
    'Douglas Sumner':	'dsumner@marfacabinets.com',
    'Ania Keller':	'imidari@marfacabinets.com',
    'Bjorn Berkmortel':	'bberkmortel@marfacabinets.com',
    'Alexander Doroshko':	'sashadoroshko@marfacabinets.com',
    '': 'nobody@marfacabinets.com'
}

output = pd.DataFrame()

# mandatory:
output['Account Name/Account CRM ID'] = data['Associated Company ID']
output['Company Name'] = data['Company Name']
output['Contact CRM ID'] = data['Contact ID']
output['Email Address'] = data['Email']
output['Is Unsubscribed'] = data['Unsubscribed from all email']
output['First Name'] = data['First Name']
output['Last Name'] = data['Last Name']
# optional about the person:
output['Job function'] = data['Job function']
output['Job Title'] = data['Job Title']
output['Lifecycle Stage'] = data['Lifecycle Stage']
output['Lead Status'] = data['Lead Status']
output['Create Date'] = data['Create Date']
output['Close Date'] = data['Close Date']
output['Last Modified Date'] = data['Last Modified Date']
output['Phone'] = data['Phone Number']
output['Mobile Phone Number'] = data['Mobile Phone Number']
output['Time of Last Visit'] = data['Time of Last Visit']
output['Time of First Visit'] = data['Time of First Visit']
output['Last Activity Date'] = data['Last Activity Date']
output['First Conversion'] = data['First Conversion']
output['First Conversion Date'] = data['First Conversion Date']
#owner = row['Contact owner']
output['Contact owner'] = 0
# about the company:
# output['Street Address'] = data['Street Address']
# output['City'] = data['City']
# output['State/Region'] = data['State/Region']
# output['Postal Code'] = data['Postal Code']
# output['Country'] = data['Country']
output['Website'] = data['Website URL']
output['Email Domain'] = data['Email Domain']
output['Work email'] = data['Work email']
# deals
output['Associated Deals'] = data['Recent Deal Close Date']
output['Recent Deal Close Date'] = data['Recent Deal Close Date']
output['Recent Deal Amount'] = data['Recent Deal Amount']
output['First Deal Created Date'] = data['First Deal Created Date']
# money:
output['Total Revenue'] = data['Total Revenue']



'''
output_headers = ['','']

output = pd.DataFrame()

email = contacts_data.loc[contacts_data['Contact CRM ID']==crm_id]['Email Address'].values[0]
'''

print(output)