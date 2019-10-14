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


def get_all_contacts(request_parameters):
    '''Downloads the complete list of contacts from the portal
    :param request_parameters: list of Contact parameters
    :return all_contacts: list of dictionaries / CDR
    :return output_columns: list of output column names
    '''
    # prepare for output
    all_contacts    = []
    output_columns  = ['vid', 'is_contact']
    output_columns.extend(request_parameters)

    # prepare for the pagination
    has_more = True
    vidOffset = 0
    count = 100  # max 100

    return all_contacts, output_columns


def main():
    print("\nYou've launched the module as __main__\n")
    return


if __name__ == '__main__':
    main()
    print('main - done')