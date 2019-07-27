# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('/media/alxfed/toca/aa-crm/Old-deals-with-ids.csv')
cont = pd.read_csv('/media/alxfed/toca/aa-crm/Contacts_csv_file.csv')


def DealStage(row):
    """
    :type stage: str
    """
    probability = ''
    deal_won = ''
    deal_closed = ''
    out_stage =''
    stage = row['Deal Stage']
    if stage.startswith('Received layout - Make quote'):
        out_stage = 'Layout received'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Design / Estimate / Revisions'):
        out_stage = 'Layout received'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Design / Estimates Completed'):
        out_stage = 'Design completed/Quote ready'
        probability = '50'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Quote Read to be Sent'):
        out_stage = 'Design completed/Quote ready'
        probability = '50'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Quote sent out'):
        out_stage = 'Quote sent out - follow up'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Send Out To Measure'):
        out_stage = 'Quote sent out - follow up'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('To be Checked for Final Approval by Lead Designer'):
        out_stage = 'Quote sent out - follow up'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Approved by Lead Designer - Ready For Contract'):
        out_stage = 'Final review approved by lead designer'
        probability = '80'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Client Approved / Contract Send Out'):
        out_stage = 'Final review approved by lead designer'
        probability = '80'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Contract Signed'):
        out_stage = 'Final review approved by lead designer'
        probability = '95'
        deal_won = '0'
    elif stage.startswith('Deposit Collected'):
        out_stage = 'Contract signed/deposit collected'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Deposit Collected'):
        out_stage = 'Contract signed/deposit collected'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('In Production'):
        out_stage = 'In Production'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Production Finished / Ready For Delivery'):
        out_stage = 'In Production'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Balance Collected'):
        out_stage = 'Delivery/pickup scheduled'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Delivery'):
        out_stage = 'Delivery/pickup scheduled'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Pick Up'):
        out_stage = 'Delivery/pickup scheduled'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Closed / Delivered'):
        out_stage = 'Won'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Lost / Never Ordered'):
        out_stage = 'Never Ordered'
        probability = '100'
        deal_won = '0'
        deal_closed = '1'
    elif stage.startswith('Unknown'):
        out_stage = 'Never Ordered'
        probability = '10'
        deal_won = '0'
        deal_closed = '1'
    return pd.Series([out_stage, probability, deal_won, deal_closed])


def ExternalEmails(row):
    associated_ids = row['Associated Contact IDs']
    if isinstance(associated_ids, str):
        contact_ids = associated_ids.split(', ') # all the IDs in a list
        primary_contact_id = int(contact_ids[0])
    else:
        primary_contact_id = associated_ids
    if not pd.isnull(cont.loc[cont['Contact CRM ID'] == primary_contact_id]['Email Address'].values[0]):
        contact_email = cont.loc[cont['Contact CRM ID'] == primary_contact_id]['Email Address'].values[0]
    else:
        contact_email = 'nobody@marfacabinets.com'
    owner_email = OwnerEmail(row['Deal owner'])
    return pd.Series([contact_email, owner_email])


def OwnerEmail(owner):
    if owner.startswith('Melissa Conroy'):
        owner_email = 'mconroy@marfacabinets.com'
    elif owner.startswith('Douglas Sumner'):
        owner_email = 'dsumner@marfacabinets.com'
    elif owner.startswith('Ania Keller'):
        owner_email = 'imidari@marfacabinets.com'
    elif owner.startswith('Bjorn Berkmortel'):
        owner_email = 'bberkmortel@marfacabinets.com'
    elif owner.startswith('Alexander Doroshko'):
        owner_email = 'sashadoroshko@marfacabinets.com'
    else:
        owner_email = 'nobody@marfacabinets.com'
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
           'Owner Occupied Address'
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
output['Amount'] = data['Amount']
output['Close Date'] = data['Close Date']
output['Create Date'] = data['Create Date'] #
output['Description'] = data['Deal Description'] # Deal Description
output['Opportunity CRM ID'] = data['Deal ID']
output['Opportunity Name'] = data['Deal Name']
# not mandatory
output['Associated Contact IDs'] = data['Associated Contact IDs']
output['Associated Contacts'] = data['Associated Contacts']
# mandatory again
output['Primary Contact CRM ID'] = data['Associated Contact IDs'][0]
output[['Primary Contact Email Address/Contact CRM ID',
        'Owner Email Address']] = data.apply(ExternalEmails, axis=1) # email here
output[['Stage Name',
        'Probability',
        'Won', 'Closed']] = data.apply(DealStage, axis=1)

output.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/deals_csv_file_result.csv', index=False)
