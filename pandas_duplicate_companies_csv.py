# -*- coding: utf-8 -*-
import pandas as pd
import time


old_companies_file_path = '/media/alxfed/toca/aa-crm/preparation/hubspot-crm-exports-all-companies-2019-08-09.csv'
company_names = pd.read_csv(old_companies_file_path)

companies = company_names['Name']
seen = set()
duplicates = set()

for company in companies:
    if company not in seen:
        seen.add(company)
    else:
        duplicates.add(company)

print('ok')

'''
<class 'set'>: {'Apmw Developer Corporation', 'Gillen Enterprises Inc'}
'''