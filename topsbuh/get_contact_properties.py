# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import csv


def main():
    DOWNLOADED_CONTACTS_FILE_PATH = '/media/alxfed/toca/aa-crm/enrich/contacts_downloaded.csv'
    vid = 858401
    out = dict()
    request_params = ['firstname', 'lastname',
                      'email', 'jobtitle', 'company',
                      'phone', 'mobilephone',
                      'associatedcompanyid', 'lastmodifieddate']

    properties = hubspot.contacts.get_contact_properties(vid, request_params)
    for key in properties.keys():
        out.update({key: properties[key]['value']})
    print('done')


if __name__ == '__main__':
    main()
    print('main - done')