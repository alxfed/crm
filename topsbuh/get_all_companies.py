# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import csv


def main():
    DOWLOADED_CONTACTS_FILE_PATH = '/media/alxfed/toca/aa-crm/enrich/contacts_downloaded.csv'
    request_params = ['firstname', 'lastname', 'email', 'email_two',
                  'jobtitle', 'company', 'phone', 'mobilephone',
                  'city', 'zip', 'state', 'hs_lead_status']
    all_contacts_cdr, all_columns = hubspot.contacts.get_all_contacts(request_params)
    with open(DOWLOADED_CONTACTS_FILE_PATH, 'w') as f:
        f_csv = csv.DictWriter(f, fieldnames=all_columns)
        f_csv.writeheader()
        f_csv.writerows(all_contacts_cdr)
    return


if __name__ == '__main__':
    main()
    print('main - done')