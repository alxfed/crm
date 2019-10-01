# -*- coding: utf-8 -*-
"""...
"""
from os import environ


api_key = environ['API_KEY']
portal_id = environ['PORTAL_ID']
parameters = {'hapikey': api_key}
header = {'Content-Type': 'application/json'}

COMPANY_CREATE_URL  = 'https://api.hubapi.com/companies/v2/companies'
COMPANY_DELETE_URL  = 'https://api.hubapi.com/companies/v2/companies/'
COMPANY_SEARCH_URL  = 'https://api.hubapi.com/companies/v2/domains/'


CONTACT_SEARCH_QUERY_URL = 'https://api.hubapi.com/contacts/v1/search/query?q='


def main():
    return


if __name__ == '__main__':
    main()
    print('main - done')