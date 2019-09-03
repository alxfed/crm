import requests
import os


API_KEY = os.environ['API_KEY']
GET_ALL_COMPANY_PROPERTIES_URL = 'https://api.hubapi.com/properties/v1/companies/properties'

headers = {"Content-Type": "application/json"}
querystring = {"hapikey": API_KEY}

parameter = {
    "name": "",
    "label": "",
    "description": "",
    "groupName": "",
    "type": "",
    "fieldType": "",
    "formField": "",
    "displayOrder": "",
    "options": ""
}

response = requests.request("GET", url=GET_ALL_COMPANY_PROPERTIES_URL, params=querystring)
if response.status_code == 200:
    res = response.json()
    for item in res:
        parameter = item
        pass
else:
    print('Error ', response.status_code)
print(res)
print('ok')