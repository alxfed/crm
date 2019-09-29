"""search
"""
import hubspot


domain = 'ethanalleninc.com'
paramlist = ['domain', 'createdate', 'name', 'hs_lastmodifieddate']

response = hubspot.search_for_company_by_domain(domain, paramlist)
if response:
    print(response)
else:
    print('nothing')
print('ok')