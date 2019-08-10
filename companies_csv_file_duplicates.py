# -*- coding: utf-8 -*-
import pandas as pd
import time


old_companies_file_path = '/media/alxfed/toca/aa-crm/preparation/hubspot-crm-exports-all-companies-2019-08-09-3.csv'
company_names = pd.read_csv(old_companies_file_path)

companies = company_names['Name']
seen = set()
duplicates = set()

for company in companies:
    if company in seen:
        duplicates.add(company)
    else:
        seen.add(company)

print('ok')

'''
<class 'set'>: {'Apmw Developer Corporation', 'Gillen Enterprises Inc'}

'Gillen Enterprises Inc', 'Linn-mathes Inc', 'Maris Construction Corporation', 
'United Chicago Builders Llc', 'Mc Carn Development Inc', 
'Sligo Construction, Incorporat', 'Apmw Developer Corporation', 
'Kasper Development Llc', 'Barrett Homes, Llc', 
'Walsh Construction Company Ii,', 'Wicklow Development Company, I'
'''