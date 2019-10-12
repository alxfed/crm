# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    contacts_file_path = '/media/alxfed/toca/aa-crm/work/all-contacts.csv'
    # emails are in the 'Email' column of contacts file
    contacts = pd.read_csv(contacts_file_path, dtype=object)
    known_contacts = set(contacts['Email'].unique())
    return


if __name__ == '__main__':
    main()
    print('main - done')