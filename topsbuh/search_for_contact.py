# -*- coding: utf-8 -*-
"""...
"""
import hubspot as hs


def main():
    string = 'kelli Auto_22669'
    response = hs.contacts.search_for_contacts(string)
    return


if __name__ == '__main__':
    main()
    print('main - done')