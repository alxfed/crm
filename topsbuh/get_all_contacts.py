# -*- coding: utf-8 -*-
"""...
"""
import hubspot


def main():
    DOWLOADED_CONTACTS_FILE_PATH = '/media/alxfed/toca/aa-crm/enrich/contacts_downloaded.csv'
    request_params = ['firstname', 'lastname', 'email', 'email_two',
                  'jobtitle', 'company', 'phone', 'mobilephone',
                  'city', 'zip', 'state', 'hs_lead_status']
    all_contacts_cdr = hubspot.contacts.get_all_contacts(request_params)
    return


if __name__ == '__main__':
    main()
    print('main - done')