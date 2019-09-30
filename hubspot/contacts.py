# -*- coding: utf-8 -*-
"""...
"""
import requests
from . import constants

def search_for_contacts(query_term):
    query = constants.CONTACT_SEARCH_QUERY_URL + query_term
    response = requests.get(url=query, params=constants.parameters)
    if response.status_code == 200:
        re = response.json()
    elif response.status_code > 200:
        re = None
    else:
        re = None
    return re

def main():
    return


if __name__ == '__main__':
    main()
    print('main - done')