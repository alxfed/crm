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
        print('The query: ', query_term, ' didnt work')
        re = None
    else:
        print('The query: ', query_term, ' returned something weird')
        re = None
    return re


def main():
    print('\nYou launched the module as main\n')
    return


if __name__ == '__main__':
    main()
    print('main - done')