import requests
import os
import uuid
import pandas as pd
import numpy as np


ACCOUNT_ID = os.environ['ACCOUNT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
uu = str(uuid.uuid4())
company_data = pd.read_csv('/media/alxfed/toca/aa-crm/uploads/new_permits.csv')
ids = company_data['id']

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

list_of_objects = []
for i in range(2, 412):
        list_of_objects.append({'id': str(ids[i])})

print('ok')
data = {
        "method":"deleteAccounts",
        "params":{"objects": list_of_objects},
        "id": uu
        }

print('ok')
api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
r = requests.post(url=api_access, json=data)

e = r.json()
#res = e['result']
print('ok')