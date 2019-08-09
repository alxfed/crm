"""
https://help.sharpspring.com/hc/en-us/articles/115001069228-Open-API-Overview#h_2972791201391518636377702
"""

import requests
import os
import uuid
import pandas as pd
# import numpy as np
import time
import json
import numpy as np


ACCOUNT_ID = os.environ['ACCOUNT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
uu = str(uuid.uuid4())

opportunities_path = '/media/alxfed/toca/aa-crm/preparation/opportunities_without_phones.csv'

permit_data = pd.read_csv('/media/alxfed/toca/aa-crm/preparation/Real-permits-to-load-with-general-contractor.csv')
# ids = company_data['id']
time.sleep(3)
opportunities_data = pd.read_csv(opportunities_path)

'''Opportunity Object
Name	                Type	        Length	        Is Required
id	                    int	            18	            Optional
ownerID	                int	            18	            Required
dealStageID	            int	            18	            Required
accountID	            int	            18	            Optional
campaignID	            int	            18	            Optional
opportunityName	        varchar	        255	            Required
probability	            double	        18	            Optional
amount	                double	        18	            Optional
isClosed	            tinyint	        1	            Optional
isWon	                tinyint	        1	            Optional
isActive	            tinyint	        1	            Optional
closeDate	            timestamp	    255	            Required
originatingLeadID	    int	            18	            Optional
primaryLeadID	        int	            18	            Optional
'''
'''
ARCHITECT Name
ARCHITECT Phone Landline
CONTRACTOR-GENERAL CONTRACTOR Phone Mobile
CONTRACTOR-GENERAL CONTRACTOR Phone Voip
CONTRACTOR-GENERAL CONTRACTOR Phone Toll	
CONTRACTOR-GENERAL CONTRACTOR Phone Landline	
CONTRACTOR-GENERAL CONTRACTOR Phone Undinined	
'''
# Alex Fedotov ID 313472547
# Alexander Doroshko ID 313468425
# Bjorn ID 313468789
# Nobody's in Charge ID 313473019
#
# Nobody Yet has ID 673342404610
# Votodef Xela has ID 673960213506

# Accounts
# No Account Provided ID 7391925250
# Marfa Cabinets ID 7264878594

# Deal Stages
# Permit obtained 413160450
# General Contractor has been contacted 413161474


opportunities = opportunities_data['Opp Name']
list_of_objects = []

for opp in opportunities:
    perm_row = permit_data[permit_data['Address'] == opp]
    opp_row = opportunities_data[opportunities_data['Opp Name'] == opp]
    phone_mobile = perm_row['CONTRACTOR-GENERAL CONTRACTOR Phone Mobile'].values[0]
    if pd.isna(phone_mobile):
        phone_mobile = ''
    phone_landline = perm_row['CONTRACTOR-GENERAL CONTRACTOR Phone Landline'].values[0]
    if pd.isna(phone_landline):
        phone_landline = ''
    phone_voip = perm_row['CONTRACTOR-GENERAL CONTRACTOR Phone Voip'].values[0]
    if pd.isna(phone_voip):
        phone_voip = ''
    phone_toll = perm_row['CONTRACTOR-GENERAL CONTRACTOR Phone Toll'].values[0]
    if pd.isna(phone_toll):
        phone_toll = ''
    architect_name = perm_row['ARCHITECT Name'].values[0]
    if pd.isna(architect_name):
        architect_name = ''
    architect_phone = perm_row['ARCHITECT Phone Landline'].values[0]
    if pd.isna(architect_phone):
        architect_phone = ''
    phone_unindentified = perm_row['CONTRACTOR-GENERAL CONTRACTOR Phone Undinined'].values[0]
    if pd.isna(phone_unindentified):
        phone_unindentified = ''
    opportunity = {
                    "id": str(opp_row['Opp ID'].values[0]),
                    "phone_mobile_5d49b26077fb6": phone_mobile,
                    "phone_landline_5d49b279dfb3e": phone_landline,
                    "phone_voip_5d49b28d269bf": phone_voip,
                    "phone_toll_5d49b30db0bce": phone_toll,
                    "architect_name_5d49b4819ce8b": architect_name,
                    "architect_phone_5d49b4e31d915": architect_phone,
                    "phone_unidentified_5d49b5bc86977": phone_unindentified
                    }
    list_of_objects.append(opportunity)

data = {
        "method":"updateOpportunities",
        "params":{"objects": list_of_objects},
        "id": uu
        }

data_json = json.dumps(data)
api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
resp = requests.post(url=api_access, json=data_json).json()
what_was_done = resp['result']
there_was_an_error = resp['error']

print('ok')

'''API errors
{
  "result":null,
  "error":{
    "code":205,
    "message":"Invalid parameters",
    "data":{
      "params":[
        {
          "param":"id",
          "message":"Expected data of type integer",
          "validFormat":{
            "type":"int",
            "length":11,
            "required":false
          }
        }
      ]
    }
  },
  "id":"<request ID>"
}
'''

'''Object level Errors
{
  "result":{
    "creates":[
      {
        "success":"false",
        "error":{
          "code":301,
          "message":"Entry already exists",
          "data":[]
        }
      }
    ]
  },
  "error":null,
  "id":"<request ID>"
}
'''