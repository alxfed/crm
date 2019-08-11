import requests
import os


API_KEY = os.environ['API_KEY']
COMPANIES_PROPERTIES_URL = 'https://api.hubapi.com/properties/v1/companies/properties'


api_access = COMPANIES_PROPERTIES_URL + "?hapikey={}".format(API_KEY)
result = requests.get(url=api_access)


print(result)