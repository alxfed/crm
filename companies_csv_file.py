# -*- coding: utf-8 -*-
import pandas as pd
from collections import OrderedDict
from scrapy.spiders import CSVFeedSpider


class CsvfeedSpider(CSVFeedSpider):
    name = 'companies'
    allowed_domains = ['google.com']
    start_urls = ['file:///media/alxfed/toca/aa-crm/old-companies.csv']
    headers = ['Company ID', 'Last Modified Date', 'Lead Status', 'Total Revenue',
               'Postal Code', 'Twitter Followers', 'Company Domain Name',
               'Last Touch Converting Campaign', 'First Touch Converting Campaign',
               'Recent Deal Close Date', 'Number of Pageviews', 'Number of Employees',
               'Time of Last Session', 'Time of First Visit', 'Close Date',
               'Facebook Fans', 'Associated Deals', 'Recent Deal Amount',
               'Number of times contacted', 'Original Source Type',
               'First Deal Created Date', 'Facebook Company Page', 'Create Date',
               'LinkedIn Bio', 'City', 'Name', 'Number of child companies',
               'Number of Visits', 'Phone Number', 'Company owner', 'About Us',
               'Last Activity Date', 'Next Activity Date', 'Owner Assigned Date',
               'State/Region', 'Email address', 'LinkedIn Company Page',
               'Total Money Raised', 'Associated Contacts', 'Original Source Data 1',
               'Target Account', 'Original Source Data 2', 'Lifecycle Stage',
               'Last Contacted', 'Street Address', 'HubSpot Team', 'Twitter Bio',
               'Web Technologies', 'Country', 'First Contact Create Date',
               'Type Contractor', 'Time Zone', 'Time Last Seen', 'Time First Seen',
               'Type', 'Website URL', 'Year Founded', 'Twitter Handle',
               'Google Plus Page', 'Days to Close', 'Description', 'Annual Revenue',
               'Parent Company', 'Industry', 'Street Address 2', 'Is Public',
               'Associated Company ID', 'Associated Company']
    delimiter = ','

    # owners_emails = pd.read_csv('/media/alxfed/toca/aa-crm/old-owners-emals.csv')

    ''' will not be used:
    'Last Modified Date', 'Lead Status', 
               'Twitter Followers', 'Company Domain Name',
               'Last Touch Converting Campaign', 'First Touch Converting Campaign',
               'Recent Deal Close Date', 'Number of Pageviews', 'Number of Employees',
               'Time of Last Session', 'Time of First Visit', 'Close Date',
               'Facebook Fans', 'Associated Deals', 'Recent Deal Amount',
               'Number of times contacted', 'Original Source Type',
               'First Deal Created Date', 'Facebook Company Page', 
               'LinkedIn Bio', 'Number of child companies',
               'Number of Visits', 'Company owner', 'About Us',
               'Last Activity Date', 'Next Activity Date', 'Owner Assigned Date',
               'Email address', 'LinkedIn Company Page',
               'Total Money Raised', 'Original Source Data 1',
               'Target Account', 'Original Source Data 2', 'Lifecycle Stage',
               'Last Contacted', 'HubSpot Team', 'Twitter Bio',
               'Web Technologies', 'First Contact Create Date',
               'Type Contractor', 'Time Zone', 'Time Last Seen', 'Time First Seen',
               'Type', 'Year Founded', 'Twitter Handle',
               'Google Plus Page', 'Days to Close', 'Annual Revenue',
               'Parent Company', 'Industry', 'Is Public',
               'Associated Company ID', 'Associated Company'
    '''
    '''fields already in the system
    #Account CRM ID, #Account Description, #Account Name,
    #Create Date, #categories,
    Annual Revenue, Associated Company, Associated Company ID,
    #Associated Contacts,
    #Billing City, #Billing Country, #Billing State/Province, #Billing Street, #Billing Zip/Postal Code,
    #Company owner, #Owner Email Address,
    Days to Close, Description, Employees,
    Fax, 
    Industry,
    LindedIn Company Page, Number of Child Companies,
    Parent Company, #Phone,   
    Shipping City, Shipping Country, Shipping State/Province, Shipping Street, Shipping Zip/Postal Code,
    #Total Revenue, Twitter Handle, Twitter Followers, 
    #Website, 
    facebook_fans, facebook_page, twitter_page
    '''

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        line = OrderedDict()
        header_start = self.headers[0]
        if row[header_start].startswith(header_start):
            yield None
        else:
            # mandatory: Account CRM ID, Account Name
            line.update({'Account CRM ID': row['Company ID']})
            line.update({'Account Name': row['Name']})
            # optional, Company:
            line.update({'Account Description': row['Description']})
            line.update({'categories': row['Industry']})
            # in the system:
            line.update({'Create Date': row['Create Date']})
            # contacts
            line.update({'Associated Contacts': row['Associated Contacts']})
            line.update({'Total Revenue': row['Total Revenue']})
            # team work:
            if row['Company owner'].endswith('(Deactivated User)'):
                line.update({'Company former owner': row['Company owner']})
                line.update({'Company owner': ''})
                line.update({'Owner Email Address': 'deactivated@marfacabinets.com'})
            else:
                line.update({'Company owner': row['Company owner']})
                line.update({'Company former owner': ''})
            company_owner = row['Company owner']
            if company_owner.startswith('Melissa Conroy'):
                line.update({'Owner Email Address': 'mconroy@marfacabinets.com'})
            elif company_owner.startswith('Douglas Sumner'):
                line.update({'Owner Email Address': 'dsumner@marfacabinets.com'})
            elif company_owner.startswith('Ania Keller'):
                line.update({'Owner Email Address': 'imidari@marfacabinets.com'})
            elif company_owner.startswith('Bjorn Berkmortel'):
                line.update({'Owner Email Address': 'bberkmortel@marfacabinets.com'})
            elif company_owner.startswith('Alexander Doroshko'):
                line.update({'Company owner': 'Alexander Doroshko'})
                line.update({'Owner Email Address': 'sashadoroshko@marfacabinets.com'})
            else:
                line.update({'Owner Email Address': 'nobody@marfacabinets.com'})
            # company info
            line.update({'Website': row['Website URL']})
            line.update({'Phone': row['Phone Number']})
            line.update({'Billing Street': row['Street Address']+row['Street Address 2']})
            line.update({'Billing City': row['City']})
            line.update({'Billing State/Province': row['State/Region']})
            line.update({'Billing Zip/Postal Code': row['Postal Code']})
            line.update({'Billing Country': row['Country']})

            yield line
