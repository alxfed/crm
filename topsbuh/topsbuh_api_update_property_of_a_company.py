import requests
import os
import csv
import json


API_KEY = os.environ['API_KEY']
ME_URL = 'https://api.hubapi.com/integrations/v1/me'
COMPANIES_PROPERTIES_URL = 'https://api.hubapi.com/properties/v1/companies/properties'
COMPANIES_URL = 'https://api.hubapi.com/companies/v2/companies/'
update_path = '/media/alxfed/toca/aa-crm/preparation/companies_to_update.csv'

data = {"properties": [
                        {
                          "name": "phone",
                          "value": ""
                        }
                      ]
        }

data['properties']['value'] = '+1 (708) 335-2413'
data_json = json.dumps(data)
company_id = ''
api_access = "{}{}?hapikey={}".format(COMPANIES_URL, company_id, API_KEY)
response = requests.put(url=api_access, json=data_json)

result = response.json()
print(result)