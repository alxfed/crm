# -*- coding: utf-8 -*-
"""...
"""
import requests
from . import constants


def get_associations_of_object(object_id, association_type):
    """Get a list of associated objects for an object
    for a given type of association
    :param object_id:
    :param association_type:
    :return: list of ids of associated objects
    """
    authentication = 'hapikey=' + constants.api_key
    req_url = f'{constants.ASSOCIATIONS_URL}{object_id}/HUBSPOT_DEFINED/' \
              f'{association_type}?{authentication}'
    pass
    return list_of_associated_objects


def main():
    return


if __name__ == '__main__':
    main()
    print('main - done')