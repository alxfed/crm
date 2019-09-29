# -*- coding: utf-8 -*-
"""...
"""
from os import environ


api_key = environ['API_KEY']
hbsp_param = {'hapikey': api_key}
hbsp_headr = {'Content-Type': 'application/json'}


def main():
    return


if __name__ == '__main__':
    main()
    print('main - done')