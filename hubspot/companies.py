# -*- coding: utf-8 -*-
"""...
"""
import requests
from . import constants


def search_for_company_by_domain(domain, paramlist):
    payload = {
              "limit": 2,
              "requestOptions": {
                "properties": paramlist
                },
              "offset": {
                "isPrimary": True,
                "companyId": 0
                }
              }
    request_url = f'{constants. COMPANY_SEARCH_URL}{domain}/companies'
    response = requests.request('POST', url=request_url,
                                headers=constants.header,
                                json=payload,
                                params=constants.parameters)
    if response.status_code == 200:
        resp = response.json()
        return resp
    else:
        print(response.status_code)
        return


def main():
    return


if __name__ == '__main__':
    main()
    print('main - done')