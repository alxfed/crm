"""search
"""
import hubspot as hs


domain = 'ethanalleninc.com'
paramlist = ['domain', 'createdate', 'name', 'hs_lastmodifieddate']

response = hs.search_for_company_by_domain(domain, paramlist)
if response:
    print(response)
else:
    print('nothing')
print('ok')