import requests
import os


API_KEY = os.environ['API_KEY']
ME_URL = 'https://api.hubapi.com/integrations/v1/me'
COMPANIES_PROPERTIES_URL = 'https://api.hubapi.com/properties/v1/companies/properties'
COMPANIES_URL = 'https://api.hubapi.com/companies/v2/companies/'

company_id = ''
api_access = "{}{}?hapikey={}".format(COMPANIES_URL, company_id, API_KEY)
response = requests.get(url=api_access)

result = response.json()
print(result)