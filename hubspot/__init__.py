# -*- coding: utf-8 -*-
"""hubspot utilities and a module
"""
from os import environ


api_key = environ['API_KEY']
parameters = {'hapikey': api_key}
header = {'Content-Type': 'application/json'}
COMPANY_SEARCH_URL = 'https://api.hubapi.com/companies/v2/domains/'


def main():
    print('main: ok')
    return


if __name__ == '__main__':
    main()
