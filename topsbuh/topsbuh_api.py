import requests
import os


API_KEY = os.environ['API_KEY']
ME_URL = 'https://api.hubapi.com/integrations/v1/me'
COMPANIES_PROPERTIES_URL = 'https://api.hubapi.com/properties/v1/companies/properties'


api_access = "{}?hapikey={}".format(ME_URL, API_KEY)
response = requests.get(url=api_access)

result = response.json()
print(result)