# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data = pd.read_csv('/media/alxfed/toca/aa-crm/uploads/Deals.csv')


def FillInThaBlanks(row):
    account_name = str(row['Account Name/Account CRM ID'])
    if account_name.startswith('nan'):
        account_name = 'No Account Provided'
    return account_name


input_headers = ['Account Name/Account CRM ID','Amount','Close Date',
                 'Create Date','Description','Opportunity CRM ID',
                 'Opportunity Name','Associated Contact IDs',
                 'Associated Contacts','Primary Contact CRM ID',
                 'Primary Contact Email Address/Contact CRM ID',
                 'Owner Email Address','Stage Name','Probability',
                 'Won','Closed']

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
output['Account Name/Account CRM ID'] = data.apply(FillInThaBlanks, axis=1)
output['Amount'] = data['Amount']
output['Close Date'] = data['Close Date']
output['Create Date'] = data['Create Date'] #
output['Description'] = data['Description'] # Deal Description
output['Opportunity CRM ID'] = data['Opportunity CRM ID']
output['Opportunity Name'] = data['Opportunity Name']
# not mandatory
output['Associated Contact IDs'] = data['Associated Contact IDs']
output['Associated Contacts'] = data['Associated Contacts']
# mandatory again
output['Primary Contact CRM ID'] = data['Primary Contact CRM ID']
output['Primary Contact Email Address/Contact CRM ID'] = data['Primary Contact Email Address/Contact CRM ID']
output['Owner Email Address'] = data['Owner Email Address']
output['Associated Contact IDs'] = data['Associated Contact IDs']
output['Stage Name'] = data['Stage Name']
output['Probability'] = data['Probability']
output['Won'] = data['Won']
output['Closed'] = data['Closed']

output.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/deals_with_no_account_provided.csv', index=False)
