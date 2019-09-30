"""search
"""
from hubspot.companies import search_for_company_by_domain


def main():
    domain = 'ethanalleninc.com'
    paramlist = ['domain', 'createdate', 'name', 'hs_lastmodifieddate']

    response = search_for_company_by_domain(domain, paramlist)
    if response:
        print(response)
    else:
        print('nothing')
    print('\n\nok\n\n')
    return


if __name__ == '__main__':
    main()
    print('main - done')