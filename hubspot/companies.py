# -*- coding: utf-8 -*-
"""...
"""
import json
import requests
import hubspot


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
    request_url = f'{hubspot.COMPANY_SEARCH_URL}{domain}/companies'
    response = requests.request('POST', url=request_url,
                                headers=hubspot.header,
                                json=payload,
                                params=hubspot.parameters)
    if response.status_code == 200:
        res = response.json()
    else:
        print(response.status_code)


def main():
    return


if __name__ == '__main__':
    main()
    print('main - done')