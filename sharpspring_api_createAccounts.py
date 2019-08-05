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
            if not (Mobile_Phone == ''):
                Phone = Mobile_Phone

            list_of_objects.append(
                    {'ownerID': '313468425',
                     'accountName': data['CONTRACTOR-GENERAL CONTRACTOR Name'].values[0],
                     'billingStreetAddress': data['CONTRACTOR-GENERAL CONTRACTOR Address'].values[0],
                     'phone': Phone
                     })

data = {
        "method":"createAccounts",
        "params":
            {"objects": list_of_objects},
        "id":uu
        }

print('ok')
data_json = json.dumps(data)
api_access = "https://api.sharpspring.com/pubapi/v1/?accountID={}&secretKey={}".format(ACCOUNT_ID, SECRET_KEY)
r = requests.post(url=api_access, json=data_json)

e = r.json()
#res = e['result']

print('ok')

'''
{
    "result": {
        "creates": [
            {
                "success": true,
                "error": null,
                "id": 7745591298
            },
            {
                "success": true,
                "error": null,
                "id": 7745592322
            },
            {
                "success": true,
                "error": null,
                "id": 7745593346
            },
            {
                "success": true,
                "error": null,
                "id": 7745594370
            },
            {
                "success": true,
                "error": null,
                "id": 7745595394
            },
            {
                "success": true,
                "error": null,
                "id": 7745596418
            },
            {
                "success": true,
                "error": null,
                "id": 7745597442
            },
            {
                "success": true,
                "error": null,
                "id": 7745598466
            },
            {
                "success": true,
                "error": null,
                "id": 7745599490
            },
            {
                "success": true,
                "error": null,
                "id": 7745600514
            },
            {
                "success": true,
                "error": null,
                "id": 7745601538
            },
            {
                "success": true,
                "error": null,
                "id": 7745602562
            },
            {
                "success": true,
                "error": null,
                "id": 7745603586
            },
            {
                "success": true,
                "error": null,
                "id": 7745604610
            },
            {
                "success": true,
                "error": null,
                "id": 7745605634
            },
            {
                "success": true,
                "error": null,
                "id": 7745606658
            },
            {
                "success": true,
                "error": null,
                "id": 7745607682
            },
            {
                "success": true,
                "error": null,
                "id": 7745608706
            },
            {
                "success": true,
                "error": null,
                "id": 7745609730
            },
            {
                "success": true,
                "error": null,
                "id": 7745610754
            },
            {
                "success": true,
                "error": null,
                "id": 7745611778
            },
            {
                "success": true,
                "error": null,
                "id": 7745612802
            },
            {
                "success": true,
                "error": null,
                "id": 7745613826
            },
            {
                "success": true,
                "error": null,
                "id": 7745614850
            },
            {
                "success": true,
                "error": null,
                "id": 7745615874
            },
            {
                "success": true,
                "error": null,
                "id": 7745616898
            },
            {
                "success": true,
                "error": null,
                "id": 7745617922
            },
            {
                "success": true,
                "error": null,
                "id": 7745618946
            },
            {
                "success": true,
                "error": null,
                "id": 7745619970
            },
            {
                "success": true,
                "error": null,
                "id": 7745620994
            },
            {
                "success": true,
                "error": null,
                "id": 7745622018
            },
            {
                "success": true,
                "error": null,
                "id": 7745623042
            },
            {
                "success": true,
                "error": null,
                "id": 7745624066
            },
            {
                "success": true,
                "error": null,
                "id": 7745625090
            },
            {
                "success": true,
                "error": null,
                "id": 7745626114
            },
            {
                "success": true,
                "error": null,
                "id": 7745627138
            },
            {
                "success": true,
                "error": null,
                "id": 7745628162
            },
            {
                "success": true,
                "error": null,
                "id": 7745629186
            },
            {
                "success": true,
                "error": null,
                "id": 7745630210
            },
            {
                "success": true,
                "error": null,
                "id": 7745631234
            },
            {
                "success": true,
                "error": null,
                "id": 7745632258
            },
            {
                "success": true,
                "error": null,
                "id": 7745633282
            },
            {
                "success": true,
                "error": null,
                "id": 7745634306
            },
            {
                "success": true,
                "error": null,
                "id": 7745635330
            },
            {
                "success": true,
                "error": null,
                "id": 7745636354
            },
            {
                "success": true,
                "error": null,
                "id": 7745637378
            },
            {
                "success": true,
                "error": null,
                "id": 7745638402
            },
            {
                "success": true,
                "error": null,
                "id": 7745639426
            },
            {
                "success": true,
                "error": null,
                "id": 7745640450
            },
            {
                "success": true,
                "error": null,
                "id": 7745641474
            },
            {
                "success": true,
                "error": null,
                "id": 7745642498
            },
            {
                "success": true,
                "error": null,
                "id": 7745643522
            },
            {
                "success": true,
                "error": null,
                "id": 7745644546
            },
            {
                "success": true,
                "error": null,
                "id": 7745645570
            },
            {
                "success": true,
                "error": null,
                "id": 7745646594
            },
            {
                "success": true,
                "error": null,
                "id": 7745647618
            },
            {
                "success": true,
                "error": null,
                "id": 7745648642
            },
            {
                "success": true,
                "error": null,
                "id": 7745649666
            },
            {
                "success": true,
                "error": null,
                "id": 7745650690
            },
            {
                "success": true,
                "error": null,
                "id": 7745651714
            },
            {
                "success": true,
                "error": null,
                "id": 7745652738
            },
            {
                "success": true,
                "error": null,
                "id": 7745653762
            },
            {
                "success": true,
                "error": null,
                "id": 7745654786
            },
            {
                "success": true,
                "error": null,
                "id": 7745655810
            },
            {
                "success": true,
                "error": null,
                "id": 7745656834
            },
            {
                "success": true,
                "error": null,
                "id": 7745657858
            },
            {
                "success": true,
                "error": null,
                "id": 7745658882
            },
            {
                "success": true,
                "error": null,
                "id": 7745659906
            },
            {
                "success": true,
                "error": null,
                "id": 7745660930
            },
            {
                "success": true,
                "error": null,
                "id": 7745661954
            },
            {
                "success": true,
                "error": null,
                "id": 7745662978
            },
            {
                "success": true,
                "error": null,
                "id": 7745664002
            },
            {
                "success": true,
                "error": null,
                "id": 7745665026
            },
            {
                "success": true,
                "error": null,
                "id": 7745666050
            },
            {
                "success": true,
                "error": null,
                "id": 7745667074
            },
            {
                "success": true,
                "error": null,
                "id": 7745668098
            },
            {
                "success": true,
                "error": null,
                "id": 7745669122
            },
            {
                "success": true,
                "error": null,
                "id": 7745670146
            },
            {
                "success": true,
                "error": null,
                "id": 7745671170
            },
            {
                "success": true,
                "error": null,
                "id": 7745672194
            },
            {
                "success": true,
                "error": null,
                "id": 7745673218
            },
            {
                "success": true,
                "error": null,
                "id": 7745674242
            }
        ]
    },
    "error": [],
    "id": "2f6534cb-a9e7-40e8-9f77-d09dca8825cf",
    "callCount": "4",
    "queryLimit": "5000"
'''