# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('/media/alxfed/toca/aa-crm/old-deals.csv')
cont = pd.read_csv('/media/alxfed/toca/aa-crm/contacts_csv_file_full_result.csv')

input_headers = ['Deal ID', 'Closed Won Reason', 'Owner Occupied Name', 'Expeditor Name',
               'Last Modified Date', 'Owner As Architect  Contractr Address',
               'Owner As General Contractor Address', 'Contractor Ventilation Phone',
               'Self Cert Architect Address', 'Pipeline', 'Masonry Contractor Address',
               'Permit #', 'Structural Engineer Address', 'Close Date', 'Deal Type',
               'Number of times contacted', 'Number of Sales Activities',
               'Contractor Ventilation Address', 'Contractor Plumber Plumbing Name',
               'Original Source Type', 'Contractor Refrigeration Name', 'Create Date',
               'Contractor General Contractor Address', 'Deal Stage',
               'Residental Real Estate Dev Name', 'Closed Lost Reason',
               'Tent Contractor Phone', 'Tent Contractor Name', 'Residental Real Estate Dev Phone',
               'Zipcode', 'Design Date', 'Deal owner', 'Last Activity Date', 'Next Activity Date',
               'Construction Stage', 'Owner Assigned Date', 'Contractor Refrigeration Phone',
               'Contractor Plumber Plumbing Phone', 'Work Descrption', 'Tent Contractor Address',
               'Deal Stage', 'Number of Contacts', 'Original Source Data 1',
               'Original Source Data 2', 'Residental Real Estate Dev Address', 'Issue Date',
               'Last Contacted', 'HubSpot Team', 'Contractor Refrigeration Address',
               'Contractor Ventilation Name', 'Deal Name', 'Contractor Plumber Plumbing Address',
               'Amount', 'Permit Issue Date', 'Structural Engineer Name', 'Expeditor Phone',
               'Owner Occupied Phone', 'Permit', 'Masonry Contractor Name',
               'Owner As General Contractor Phone', 'Self Cert Architect Phone', 'Deal Description',
               'Owner As General Contractor Name', 'Self Cert Architect Name', 'Permit Type',
               'Masonry Contractor Phone', 'Deal Other Name', 'Amount in company currency',
               'Owner As Architect  Contractr Name', 'Expeditor Address', 'Permits Amount',
               'Owner Occupied Address', 'Associated Company ID', 'Associated Company',
               'Associated Contact IDs', 'Associated Contacts']

''' will not be used:
        'Closed Won Reason', 'Owner Occupied Name', 'Expeditor Name',
           'Last Modified Date', 'Owner As Architect  Contractr Address',
           'Owner As General Contractor Address', 'Contractor Ventilation Phone',
           'Self Cert Architect Address', 'Pipeline', 'Masonry Contractor Address',
           'Permit #', 'Structural Engineer Address', 'Deal Type',
           'Number of times contacted', 'Number of Sales Activities',
           'Contractor Ventilation Address', 'Contractor Plumber Plumbing Name',
           'Original Source Type', 'Contractor Refrigeration Name', 'Create Date',
           'Contractor General Contractor Address', 'Deal Stage',
           'Residental Real Estate Dev Name', 'Closed Lost Reason',
           'Tent Contractor Phone', 'Tent Contractor Name', 'Residental Real Estate Dev Phone',
           'Zipcode', 'Design Date', 'Deal owner', 'Last Activity Date', 'Next Activity Date',
           'Construction Stage', 'Owner Assigned Date', 'Contractor Refrigeration Phone',
           'Contractor Plumber Plumbing Phone', 'Work Descrption', 'Tent Contractor Address',
           'Deal Stage', 'Number of Contacts', 'Original Source Data 1',
           'Original Source Data 2', 'Residental Real Estate Dev Address', 'Issue Date',
           'Last Contacted', 'HubSpot Team', 'Contractor Refrigeration Address',
           'Contractor Ventilation Name', 'Contractor Plumber Plumbing Address',
           'Permit Issue Date', 'Structural Engineer Name', 'Expeditor Phone',
           'Owner Occupied Phone', 'Permit', 'Masonry Contractor Name',
           'Owner As General Contractor Phone', 'Self Cert Architect Phone', 'Deal Description',
           'Owner As General Contractor Name', 'Self Cert Architect Name', 'Permit Type',
           'Masonry Contractor Phone', 'Deal Other Name', 'Amount in company currency',
           'Owner As Architect  Contractr Name', 'Expeditor Address', 'Permits Amount',
           'Owner Occupied Address', 
           'Associated Contact IDs', 'Associated Contacts'
'''

'''Mandatory
    Account Name/Account CRM ID
    Amount
    Close Date
    Closed
    Opportunity CRM ID
    Opportunity Name
    Owner Email Address
    Primary Contact Email Address/Contact CRM ID
    Probability
    Stage Name
    Won
'''
output = pd.DataFrame()
# mandatory
output['Account CRM ID'] = data['Associated Company ID']
#output['Account Name'] = data['Associated Company']
output['Amount'] = data['Amount']
output['Close Date'] = data['Close Date']
output['Closed'] = str(0) # 0 or 1
output['Create Date'] = data['Create Date'] #
output['Description'] = data['Deal Description'] # Deal Description
output['Opportunity CRM ID'] = data['Deal ID']
output['Opportunity Name'] = data['Deal Name']
# not in the file
contact_ids = data['Associated Contact IDs']
owner_email = cont.loc[cont['Contact CRM ID'] == contact_ids[0]]['Owner Email'].values[0]
output['Owner Email Address'] = owner_email
output['Primary Contact CRM ID'] = contact_ids[0]
# not in the file
contact_email = cont.loc[cont['Contact CRM ID'] == contact_ids[0]]['Email Address'].values[0]
output['Primary Contact Email Address/Contact CRM ID'] = contact_email # email here
deal_stage = data['Deal Stage']
output['Stage Name'] = deal_stage
# probability calculated
# prob = pro(row['Deal Stage']) # function
output['Probability'] = ''  # str(prob) # in %, 10, 90 ..

won = 1 # wo()  # won or lost
output['Won'] = data[''] # 0 - lost, 1 - won
# optional
output['Other Contact CRM IDs'] = data['Associated Contact IDs']

output.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/deals_csv_file_result.csv', index=False)
