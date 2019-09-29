"""search
"""
import hubspot


domain = 'ethanalleninc.com'
paramlist = ['domain', 'createdate', 'name', 'hs_lastmodifieddate']
c = hubspot.companies_function(domain)
ra = hubspot.e

response = hubspot.search_for_company_by_domain(domain, paramlist)
if response:
    print(response)
else:
    print('nothing')
print('ok')