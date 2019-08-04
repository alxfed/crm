# -*- coding: utf-8 -*-
import pandas as pd
import time


permits_file_path = '/media/alxfed/toca/aa-crm/preparation/permits-23-07-2019_Need_to_load_with_general_contractors.csv'
companies_file_path = '/media/alxfed/toca/aa-crm/preparation/accounts-export-0000-00-00-2019-08-03.csv'
permits = pd.read_csv(permits_file_path)
time.sleep(3)
companies = pd.read_csv(companies_file_path)

def TestCompany(row):
    company = str(row['CONTRACTOR-GENERAL CONTRACTOR Name'])
    company_name = companies.loc[companies['Account Name'] == company]['Account Name']
    company_name = company_name.values[0]
    if company_name:
        AccountID = companies.loc[companies['Account Name'] == company]['AccountID'].values[0]
        OwnerID = companies.loc[companies['Account Name'] == company]['OwnerID'].values[0]
    else:
        AccountID = ''
        OwnerID = 313468425
    return AccountID, OwnerID, company_name



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

#a = permits.iloc[:, 2]

output['Permit']            = permits['Permit']
output['Amount']            = permits.iloc[:, 2]
output['Issue Date']        = permits['Issue Date']
output['Address']           = permits['Address']
output[['AccountID', 'OwnerID', 'General Contractor Name']] = permits.apply(TestCompany, axis=1)
# output['Close Date'] = '2019-12-12 12:06:22'
output['Permit Type']       = permits['Permit Type']
output['Work Description']  = permits['Work Description']
'''
output['Description'] = permits['Deal Description'] # Deal Description
output['Opportunity CRM ID'] = permits['Deal ID']
output['Opportunity Name'] = permits['Deal Name']
# not mandatory
output['Associated Contact IDs'] = permits['Associated Contact IDs']
output['Associated Contacts'] = permits['Associated Contacts']
# mandatory again
# output['Primary Contact CRM ID'] = permits['Associated Contact IDs'][0]
output[['Primary Contact CRM ID', 'Primary Contact Email Address/Contact CRM ID',
        'Owner Email Address', 'Associated Contact IDs']] = permits.apply(ExternalEmails, axis=1) # email here
output[['Stage Name',
        'Probability',
        'Won', 'Closed']] = permits.apply(DealStage, axis=1)
'''

output.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/preparation/Permits_to_load_known_companies.csv', index=False)

'''
These are the fields that are required for your Notes for Accounts. Please ensure that your Notes for Accounts CSV contains these columns.

Account CRM ID
Create Date
Note Description
Owner Email Address
'''
'''
    if company.startswith('nan'):
        company_name = 'No Account Provided'
        AccountID = 7391925250
        OwnerID = 313468425
    else:
'''

'''
input_headers = ['Permit #', 'Permit Type', ' Permits Amount ',
                 'Issue Date', 'Work Description', 'Zipcode',
                 'Address', 'OWNER OCCUPIED Name', 'OWNER OCCUPIED Address',
                 'OWNER OCCUPIED Phone Mobile', 'OWNER OCCUPIED Phone Voip',
                 'OWNER OCCUPIED Phone Toll', 'OWNER OCCUPIED Phone Landline',
                 'OWNER OCCUPIED Phone Undinined', 'ARCHITECT Name',
                 'ARCHITECT Address', 'ARCHITECT Phone Mobile',
                 'ARCHITECT Phone Voip', 'ARCHITECT Phone Toll',
                 'ARCHITECT Phone Landline', 'ARCHITECT Phone Undinined',
                 'CONTRACTOR-ELECTRICAL Name', 'CONTRACTOR-ELECTRICAL Address',
                 'CONTRACTOR-ELECTRICAL Phone Mobile',
                 'CONTRACTOR-ELECTRICAL Phone Voip',
                 'CONTRACTOR-ELECTRICAL Phone Toll',
                 'CONTRACTOR-ELECTRICAL Phone Landline',
                 'CONTRACTOR-ELECTRICAL Phone Undinined',
                 'CONTRACTOR-GENERAL CONTRACTOR Name',
                 'CONTRACTOR-GENERAL CONTRACTOR Address',
                 'CONTRACTOR-GENERAL CONTRACTOR Phone Mobile',
                 'CONTRACTOR-GENERAL CONTRACTOR Phone Voip',
                 'CONTRACTOR-GENERAL CONTRACTOR Phone Toll',
                 'CONTRACTOR-GENERAL CONTRACTOR Phone Landline',
                 'CONTRACTOR-GENERAL CONTRACTOR Phone Undinined',
                 'MASONRY CONTRACTOR Name', 'MASONRY CONTRACTOR Address',
                 'MASONRY CONTRACTOR Phone Mobile', 'MASONRY CONTRACTOR Phone Voip',
                 'MASONRY CONTRACTOR Phone Toll', 'MASONRY CONTRACTOR Phone Landline',
                 'MASONRY CONTRACTOR Phone Undinined',
                 'CONTRACTOR-PLUMBER/PLUMBING Name',
                 'CONTRACTOR-PLUMBER/PLUMBING Address',
                 'CONTRACTOR-PLUMBER/PLUMBING Phone Mobile',
                 'CONTRACTOR-PLUMBER/PLUMBING Phone Voip',
                 'CONTRACTOR-PLUMBER/PLUMBING Phone Toll',
                 'CONTRACTOR-PLUMBER/PLUMBING Phone Landline',
                 'CONTRACTOR-PLUMBER/PLUMBING Phone Undinined',
                 'CONTRACTOR-REFRIGERATION Name',
                 'CONTRACTOR-REFRIGERATION Address',
                 'CONTRACTOR-REFRIGERATION Phone Mobile',
                 'CONTRACTOR-REFRIGERATION Phone Voip',
                 'CONTRACTOR-REFRIGERATION Phone Toll',
                 'CONTRACTOR-REFRIGERATION Phone Landline',
                 'CONTRACTOR-REFRIGERATION Phone Undinined',
                 'OWNER Name', 'OWNER Address', 'OWNER Phone Mobile',
                 'OWNER Phone Voip', 'OWNER Phone Toll',
                 'OWNER Phone Landline', 'OWNER Phone Undinined',
                 'EXPEDITOR Name', 'EXPEDITOR Address',
                 'EXPEDITOR Phone Mobile', 'EXPEDITOR Phone Voip',
                 'EXPEDITOR Phone Toll', 'EXPEDITOR Phone Landline',
                 'EXPEDITOR Phone Undinined', 'CONTRACTOR-VENTILATION Name',
                 'CONTRACTOR-VENTILATION Address',
                 'CONTRACTOR-VENTILATION Phone Mobile',
                 'CONTRACTOR-VENTILATION Phone Voip',
                 'CONTRACTOR-VENTILATION Phone Toll',
                 'CONTRACTOR-VENTILATION Phone Landline',
                 'CONTRACTOR-VENTILATION Phone Undinined',
                 'SELF CERT ARCHITECT Name', 'SELF CERT ARCHITECT Address',
                 'SELF CERT ARCHITECT Phone Mobile',
                 'SELF CERT ARCHITECT Phone Voip',
                 'SELF CERT ARCHITECT Phone Toll',
                 'SELF CERT ARCHITECT Phone Landline',
                 'SELF CERT ARCHITECT Phone Undinined',
                 'STRUCTURAL ENGINEER Name', 'STRUCTURAL ENGINEER Address',
                 'STRUCTURAL ENGINEER Phone Mobile',
                 'STRUCTURAL ENGINEER Phone Voip', 'STRUCTURAL ENGINEER Phone Toll',
                 'STRUCTURAL ENGINEER Phone Landline',
                 'STRUCTURAL ENGINEER Phone Undinined',
                 'RESIDENTAL REAL ESTATE DEV Name', 'RESIDENTAL REAL ESTATE DEV Address',
                 'RESIDENTAL REAL ESTATE DEV Phone Mobile',
                 'RESIDENTAL REAL ESTATE DEV Phone Voip',
                 'RESIDENTAL REAL ESTATE DEV Phone Toll',
                 'RESIDENTAL REAL ESTATE DEV Phone Landline',
                 'RESIDENTAL REAL ESTATE DEV Phone Undinined',
                 'OWNER AS GENERAL CONTRACTOR Name',
                 'OWNER AS GENERAL CONTRACTOR Address',
                 'OWNER AS GENERAL CONTRACTOR Phone Mobile',
                 'OWNER AS GENERAL CONTRACTOR Phone Voip',
                 'OWNER AS GENERAL CONTRACTOR Phone Toll',
                 'OWNER AS GENERAL CONTRACTOR Phone Landline',
                 'OWNER AS GENERAL CONTRACTOR Phone Undinined',
                 'TENT CONTRACTOR Name', 'TENT CONTRACTOR Address',
                 'TENT CONTRACTOR Phone Mobile', 'TENT CONTRACTOR Phone Voip',
                 'TENT CONTRACTOR Phone Toll', 'TENT CONTRACTOR Phone Landline',
                 'TENT CONTRACTOR Phone Undinined']
'''