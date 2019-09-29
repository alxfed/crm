import requests
import os
import csv
from collections import OrderedDict
import hubspot


domain = 'ethanalleninc.com'

response = search_for_company_by_domain(domain, paramlist)

if response.status_code == 200:
    res = response.json()
else:
    print(response.status_code)
print('ok')