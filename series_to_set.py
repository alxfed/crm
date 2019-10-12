# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    existing_contacts_path = '/media/alxfed/toca/aa-crm/work/all-contacts.csv'
    # emails are in the 'Email' column of contacts file
    existing_contacts = pd.read_csv(existing_contacts_path, dtype=object)
    known_contacts = existing_contacts['Email']
    known = known_contacts.unique()
    contacts = set(known_contacts)
    cont_list = known_contacts.tolist()
    return


if __name__ == '__main__':
    main()
    print('main - done')