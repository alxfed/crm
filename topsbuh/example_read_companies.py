"""
example from hubspot documentation
"""
import requests
import json
import urllib


max_results = 500
hapikey = 'demo'
limit = 5
company_list = []
get_all_companies_url = "https://api.hubapi.com/companies/v2/companies/paged?"
parameter_dict = {'hapikey': hapikey, 'limit': limit}
headers = {}

# Paginate your request using offset
has_more = True
while has_more:
    parameters = urllib.urlencode(parameter_dict)
    get_url = get_all_companies_url + parameters
    r = requests.get(url=get_url, headers=headers)
    response_dict = json.loads(r.text)
    has_more = response_dict['has-more']
    company_list.extend(response_dict['companies'])
    parameter_dict['offset'] = response_dict['offset']
    if len(
            company_list) >= max_results:  # Exit pagination, based on whatever value you've set your max results variable to.
        print('maximum number of results exceeded')
        break

print('loop finished')

list_length = len(company_list)