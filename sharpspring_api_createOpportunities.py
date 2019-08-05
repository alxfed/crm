"""
https://help.sharpspring.com/hc/en-us/articles/115001069228-Open-API-Overview#h_2972791201391518636377702
"""

import requests
import os
import uuid
import pandas as pd
# import numpy as np
import time


ACCOUNT_ID = os.environ['ACCOUNT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
uu = str(uuid.uuid4())
companies_file_path = '/media/alxfed/toca/aa-crm/preparation/accounts-export-0000-00-00-2019-08-05.csv'
permit_data = pd.read_csv('/media/alxfed/toca/aa-crm/preparation/Real-permits-to-load-with-general-contractor.csv')
# ids = company_data['id']
time.sleep(3)
companies_data = pd.read_csv(companies_file_path)

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

timest = str(pd.Timestamp(year=2019, month=12, day=4, hour=12, minute=12, second=0))
# alternative ts_input= '...'



for permit in permit_data:
        company = companies_data.loc(companies_data['Account Name'] == permit)
        accountID =
        amount =
        opportunityName =
        opportunity = {
                        'ownerID': '313468425',                 # mandatory
                        'dealStageID': '413160450',             # mandatory
                        'accountID': accountID,                # optional
                        'opportunityName': opportunityName,          # mandatory
                        'probability': '10',              # optional
                        'amount': amount,                   # optional
                        'isClosed': '0',                 # optional
                        'isWon': '0',                    # optional
                        'isActive': '1',                 # optional
                        'closeDate': timest                # mandatory
                        }

list_of_objects = []
list_of_objects.append(opportunity)

'''
for i in range(2, 412):
        list_of_objects.append(opportunity)
'''

data = {
        "method":"createOpportunities",
        "params":{"objects": list_of_objects},
        "id": uu
        }

api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
resp = requests.post(url=api_access, json=data).json()
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