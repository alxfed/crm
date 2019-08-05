import requests
import os
import uuid
import pandas as pd
import numpy as np
import time
import json


accounts_data_path = '/media/alxfed/toca/aa-crm/preparation/Permits_to_load_result_unknown_companies.csv'
#all_permits_data_path = '/media/alxfed/toca/aa-crm/preparation/Real-permits-to-load.csv'
permits_file_path = '/media/alxfed/toca/aa-crm/preparation/Real-permits-to-load-with-general-contractor.csv'
# new_companies_file_path = '/media/alxfed/toca/aa-crm/preparation/Permits_to_load_result_unknown_companies.csv'

ACCOUNT_ID = os.environ['ACCOUNT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
uu = str(uuid.uuid4())

new_accounts = pd.read_csv(accounts_data_path)
time.sleep(3)
all_permits = pd.read_csv(permits_file_path)
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
pool = set()
for permit in permits:
        data = all_permits[all_permits['Permit #'] == permit]
        co = str(data['CONTRACTOR-GENERAL CONTRACTOR Name'].values[0])
        if co not in pool:
            pool.add(co)
            if not pd.isna(data['CONTRACTOR-GENERAL CONTRACTOR Phone Landline'].values[0]):
                Phone = data['CONTRACTOR-GENERAL CONTRACTOR Phone Landline'].values[0]
            else:
                Phone = ''
            if not pd.isna(data['CONTRACTOR-GENERAL CONTRACTOR Phone Mobile'].values[0]):
                Mobile_Phone = data['CONTRACTOR-GENERAL CONTRACTOR Phone Mobile'].values[0]
            else:
                Mobile_Phone = ''
            list_of_objects.append(
                    {'ownerID': '313468425',
                     'accountName': data['CONTRACTOR-GENERAL CONTRACTOR Name'].values[0],
                     'billingStreetAddress': data['CONTRACTOR-GENERAL CONTRACTOR Address'].values[0],
                     'phone': Phone,
                     'mobilePhoneNumber': Mobile_Phone,
                     })

data = {
        "method":"createAccounts",
        "params":
            {"objects": list_of_objects
             },
        "id":uu
        }

print('ok')
data_json = json.dumps(data)
api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
r = requests.post(url=api_access, json=data_json)

e = r.json()
#res = e['result']

print('ok')