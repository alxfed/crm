# -*- coding: utf-8 -*-
"""...
"""
import requests
import os
import re
import csv
import json
import time


API_KEY = os.environ['API_KEY']

CONTACT_PROPERTIES_URL = 'https://api.hubapi.com/contacts/v1/contact/vid/'
SUFFIX = '/profile?hapikey='
associations_path = '/media/alxfed/toca/aa-crm/enrich/associations_downloaded.csv'


def main():
    # request data
    data = {"properties": [
        {
            "property": "company_index",
            "value": ""
        }
      ]
    }
    with open(associations_path) as f:
        f_csv = csv.DictReader(f, restkey='Rest', restval='')
        for row in f_csv:
            vid_list = json.loads(row['associations'])
            for ind, vid in enumerate(vid_list):
                data['properties'][0]['value'] = str(ind + 1)
                api_access = "{}{}/profile?hapikey={}".format(CONTACT_PROPERTIES_URL, str(vid), API_KEY)
                resp = requests.post(url=api_access, json=data)
                if resp.status_code != 204:
                    print('Not 204')
            print('Company index ', row['companyId'])
    return


if __name__ == '__main__':
    main()
    print('main - done')