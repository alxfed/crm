import requests
import os
import uuid
import pandas as pd
import numpy as np
import time


accounts_data_path = '/media/alxfed/toca/aa-crm/preparation/Permits_to_load_result_unknown_companies.csv'
all_permits_data_path = '/media/alxfed/toca/aa-crm/preparation/Real-permits-to-load-with-general-contractor.csv'

ACCOUNT_ID = os.environ['ACCOUNT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
uu = str(uuid.uuid4())

new_accounts = pd.read_csv(accounts_data_path)
time.sleep(3)
all_permits = pd.read_csv(all_permits_data_path)
list_of_objects = []

'''
Name	                Type	        Length	        Is Required
id	                    int	            18	            Optional
ownerID	                int	            18	            Optional
accountName	            varchar	        255	            Required
industry	            varchar	        255	            Optional
phone	                varchar	        255	            Optional
annualRevenue	        int	            18	            Optional
numberOfEmployees	    int	            18	            Optional
website	                varchar	        255	            Optional
yearStarted	            int	            18	            Optional
fax	                    varchar	        255	            Optional
billingCity	            varchar	        255	            Optional
billingCountry	        varchar	        255	            Optional
billingPostalCode	    varchar	        50	            Optional
billingState	        varchar	        255	            Optional
billingStreetAddress	varchar	        255	            Optional
shippingCity	        varchar	        255	            Optional
shippingCountry	        varchar	        255	            Optional
shippingPostalCode	    varchar         50	            Optional
shippingState	        varchar	        255	            Optional
shippingStreetAddress	varchar	        255	            Optional
'''

permits = new_accounts['Permit']
for permit in permits:
        data = all_permits[all_permits['Permit #'] == permit]
        list_of_objects.append(
                {'ownerID': '313468425',
                 'accountName': data['CONTRACTOR-GENERAL CONTRACTOR Name'].values[0],
                 'phone': data['']
                 }
        )

print('ok')

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
'''
print('ok')