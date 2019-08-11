import requests
import os
import json


API_KEY = os.environ['API_KEY']
ME_URL = 'https://api.hubapi.com/integrations/v1/me'
COMPANIES_PROPERTIES_URL = 'https://api.hubapi.com/properties/v1/companies/properties'
COMPANIES_URL = 'https://api.hubapi.com/companies/v2/companies/'

data = {
  "properties": [
    {
      "name": "phone",
      "value": "+1 (773) 370-6857"
    }
  ]
}

data_json = json.dumps(data)
company_id = ''
api_access = "{}{}?hapikey={}".format(COMPANIES_URL, company_id, API_KEY)
response = requests.put(url=api_access, json=data_json)

result = response.json()
print(result)