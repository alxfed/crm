'''
template
'''

import pandas as pd

data = pd.read_csv('/media/alxfed/toca/aa-crm/enrich/sheet0.csv')

input_headers = ['Address', 'Probidder Status', 'Probidder Sold Date',
                 'Probidder Sales Price', 'MLS ID', 'MLS Status',
                 'MLS Sold/List Price', 'Owners Name', 'Owners Address',
                 'Listing Agent Name', 'Listing Agent ID',
                 'Listing Agent Phone', 'Listing Agent Email',
                 'Selling Agent Name', 'Selling Agent ID',
                 'Selling Agent Phone', 'Selling Agent Email']


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
# second file
output2['Agent Name'] = data['Selling Agent Name']
output2['Agent ID'] = data['Selling Agent ID']
output2['Agent Phone'] = data['Selling Agent Phone']
output2['Agent Email'] = data['Selling Agent Email']


output.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/enrich/sheet0_agents1.csv', index=False)
output.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/enrich/sheet0_agents2.csv', index=False)