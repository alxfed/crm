'''
template
'''

import pandas as pd

data = pd.read_csv('/media/alxfed/toca/aa-crm/enrich/lag_emails.csv')

input_headers = ['Address', 'Probidder Status', 'Probidder Sold Date',
                 'Probidder Sales Price', 'MLS ID', 'MLS Status',
                 'MLS Sold/List Price', 'Owners Name', 'Owners Address',
                 'Listing Agent Name', 'Listing Agent ID', 'Listing Agent Phone',
                 'Listing Agent Email']


''' will not be used: 
               'Address', 'Probidder Status', 'Probidder Sold Date',
                 'Probidder Sales Price', 'MLS ID', 'MLS Status',
                 'MLS Sold/List Price', 'Owners Name', 'Owners Address',
'''

output = pd.DataFrame()
output2 = pd.DataFrame()

# first file:
output['Agent Name'] = data['Listing Agent Name']
output['Agent ID'] = data['Listing Agent ID']
output['Agent Phone'] = data['Listing Agent Phone']
output['Agent Email'] = data['Listing Agent Email']

output.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/enrich/lag_emails_agents1.csv', index=False)
