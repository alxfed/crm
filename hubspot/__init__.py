# -*- coding: utf-8 -*-
"""hubspot utilities and a module
"""
from os import environ
import json
import requests


api_key = environ['API_KEY']
parameters = {'hapikey': api_key}
header = {'Content-Type': 'application/json'}
COMPANY_SEARCH_URL = 'https://api.hubapi.com/companies/v2/domains/'


def search_for_company_by_domain(domain, paramlist):
    payload = json.loads({
        "limit": 2,
        "requestOptions": {
            "properties": []
            },
        "offset": {
            "isPrimary": True,
            "companyId": 0
        }
    })
    payload['properties'] = paramlist
    request_url = f'{COMPANY_SEARCH_URL}{domain}/companies'
    response = requests.request('POST', url=request_url,
                                headers=header,
                                json=payload,
                                params=parameters)
    if response.status_code == 200:
        resp = response.json()
        return resp
    else:
        print(response.status_code)
        return


def main():
    print('main: ok')
    return


if __name__ == '__main__':
    main()
