# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import csv


def main():
    OBJECTID_FILE_PATH = '/media/alxfed/toca/aa-crm/enrich/companies_downloaded.csv'
    ASSOCIATIONS_FILE_PATH = '/media/alxfed/toca/aa-crm/enrich/associations_downloaded.csv'
    association_types = {'Contact to company': 1, 'Company to contact': 2,
                         'Deal to contact': 3, 'Contact to deal': 4,
                         }
    associations, all_columns = hubspot.companies.get_all_companies(request_params)
    with open(ASSOCIATIONS_FILE_PATH, 'w') as f:
        f_csv = csv.DictWriter(f, fieldnames=all_columns)
        f_csv.writeheader()
        f_csv.writerows(associations)
    return


if __name__ == '__main__':
    main()
    print('main - done')