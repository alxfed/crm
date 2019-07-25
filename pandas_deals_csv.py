# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('/media/alxfed/toca/aa-crm/old-deals.csv')
cont = pd.read_csv('/media/alxfed/toca/aa-crm/contacts_csv_file_full_result.csv')


def DealStage(stage):
    probability = ''
    deal_won = ''
    deal_closed = ''
    if stage.startswith('Received layout - Make quote'):
        stage = 'Layout received'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Design / Estimate / Revisions'):
        stage = 'Layout received'
        probability = '30'
        won = '0'
    elif stage.startswith('Design / Estimates Completed'):
        stage = 'Design completed/Quote ready'
        probability = '50'
        won = '0'
    elif stage.startswith('Quote Read to be Sent'):
        stage = 'Design completed/Quote ready'
        probability = '50'
        won = '0'
    elif stage.startswith('Quote sent out'):
        stage = 'Quote sent out - follow up'
        probability = '30'
        won = '0'
    elif stage.startswith('Send Out To Measure'):
        stage = 'Quote sent out - follow up'
        probability = '30'
        won = '0'
    elif stage.startswith('To be Checked for Final Approval by Lead Designer'):
        stage = 'Quote sent out - follow up'
        probability = '30'
        won = '0'
    elif stage.startswith('Approved by Lead Designer - Ready For Contract'):
        stage = 'Final review approved by lead designer'
        probability = '80'
        won = '0'
    elif stage.startswith('Client Approved / Contract Send Out'):
        stage = 'Final review approved by lead designer'
        probability = '80'
        won = '0'
    elif stage.startswith('Contract Signed'):
        stage = 'Final review approved by lead designer'
        probability = '95'
        won = '0'
    elif stage.startswith('Deposit Collected'):
        stage = 'Contract signed/deposit collected'
        probability = '100'
        won = '1'
    elif stage.startswith('Deposit Collected'):
        stage = 'Contract signed/deposit collected'
        probability = '100'
        won = '1'
    elif stage.startswith('In Production'):
        stage = 'In Production'
        probability = '100'
        won = '1'
    elif stage.startswith('Production Finished / Ready For Delivery'):
        stage = 'In Production'
        probability = '100'
        won = '1'
    elif stage.startswith('Balance Collected'):
        stage = 'Delivery/pickup scheduled'
        probability = '100'
        won = '1'
    elif stage.startswith('Delivery'):
        stage = 'Delivery/pickup scheduled'
        probability = '100'
        won = '1'
    elif stage.startswith('Pick Up'):
        stage = 'Delivery/pickup scheduled'
        probability = '100'
        won = '1'
    elif stage.startswith('Closed / Delivered'):
        stage = 'Won'
        probability = '100'
        won = '1'
    elif stage.startswith('Lost / Never Ordered'):
        stage = 'Never Ordered'
        probability = '100'
        won = '0'
    elif stage.startswith('Unknown'):
        stage = 'Never Ordered'
        probability = '10'
        won = '0'
        return stage, probability, deal_won, deal_closed


def ContactEmail(contactid):
    contact_email = cont.loc[cont['Contact CRM ID'] == contactid]['Email Address'].values[0]
    return contact_email


def ContactOwnerEmail(contactid):
    owner_email = cont.loc[cont['Contact CRM ID'] == contactid]['Owner Email'].values[0]
    return owner_email


input_headers = ['Deal ID', 'Closed Won Reason', 'Owner Occupied Name', 'Expeditor Name',
               'Last Modified Date', 'Owner As Architect  Contractr Address',
               'Owner As General Contractor Address', 'Contractor Ventilation Phone',
               'Self Cert Architect Address', 'Pipeline', 'Masonry Contractor Address',
               'Permit #', 'Structural Engineer Address', 'Close Date', 'Deal Type',
               'Number of times contacted', 'Number of Sales Activities',
               'Contractor Ventilation Address', 'Contractor Plumber Plumbing Name',
               'Original Source Type', 'Contractor Refrigeration Name', 'Create Date',
               'Contractor General Contractor Address',
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
           'Contractor General Contractor Address',
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
output['Owner Email Address'] = data['Deal Stage'].map(owner_email)
output['Primary Contact CRM ID'] = data['Associated Contact IDs'][0]
# not in the file
output['Primary Contact Email Address/Contact CRM ID'] = contact_email # email here
deal_stage = data['Deal Stage']
#...
output['Stage Name'] = deal_stage
output['Probability'] = probability  # str(prob) # in %, 10, 90 ..
output['Won'] = won # 0 - lost, 1 - won

output.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/deals_csv_file_result.csv', index=False)
