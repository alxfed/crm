# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import csv


def main():
    OBJECTID_FILE_PATH = '/media/alxfed/toca/aa-crm/enrich/companies_downloaded.csv'
    ASSOCIATIONS_FILE_PATH = '/media/alxfed/toca/aa-crm/enrich/both_company_associations_downloaded.csv'
    association_types = {'Contact to company': 1, 'Company to contact': 2,
                         'Deal to contact': 3, 'Contact to deal': 4,
                         'Deal to company': 5, 'Company to deal': 6,
                         'Company to engagement': 7, 'Engagement to company': 8,
                         'Contact to engagement': 9, 'Engagement to contact': 10,
                         'Deal to engagement': 11, 'Engagement to deal': 12}
    # output
    output_rows = []
    output_columns = ['companyId', 'Contact to company', 'Company to contact']

    with open(OBJECTID_FILE_PATH) as f:
        f_csv = csv.DictReader(f, restkey='Rest', restval='')
        for row in f_csv:
            output_row = {}
            ass_one = ''
            assoc = hubspot.associations.get_associations_of_object(row['companyId'], 1)
            if assoc:
                ass_one = " ".join(['%s' % n for n in assoc])
            output_row.update({'companyId': row['companyId'],
                               'Contact to company': ass_one})
            ass_two = ''
            assoc = hubspot.associations.get_associations_of_object(row['companyId'], 2)
            if assoc:
                ass_two = " ".join(['%s' % n for n in assoc])
            output_row.update({'Company to contact': ass_two})
            print('Now storing: ', output_row)
            output_rows.append(output_row)

    with open(ASSOCIATIONS_FILE_PATH, 'w') as f:
        f_csv = csv.DictWriter(f, fieldnames=output_columns)
        f_csv.writeheader()
        f_csv.writerows(output_rows)
    return


if __name__ == '__main__':
    main()
    print('main - done')