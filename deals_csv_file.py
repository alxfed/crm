# -*- coding: utf-8 -*-
# import pandas as pd
from collections import OrderedDict
from scrapy.spiders import CSVFeedSpider


class CsvfeedSpider(CSVFeedSpider):
    name = 'deals'
    allowed_domains = ['google.com']
    start_urls = ['file:///media/alxfed/toca/aa-crm/old-deals.csv']
    headers = ['Deal ID', 'Closed Won Reason', 'Owner Occupied Name', 'Expeditor Name',
               'Last Modified Date', 'Owner As Architect  Contractr Address',
               'Owner As General Contractor Address', 'Contractor Ventilation Phone',
               'Self Cert Architect Address', 'Pipeline', 'Masonry Contractor Address',
               'Permit #', 'Structural Engineer Address', 'Close Date', 'Deal Type',
               'Number of times contacted', 'Number of Sales Activities',
               'Contractor Ventilation Address', 'Contractor Plumber Plumbing Name',
               'Original Source Type', 'Contractor Refrigeration Name', 'Create Date',
               'Contractor General Contractor Address', 'Deal Stage',
               'Residental Real Estate Dev Name', 'Closed Lost Reason',
               'Tent Contractor Phone', 'Tent Contractor Name', 'Residental Real Estate Dev Phone',
               'Zipcode', 'Design Date', 'Deal owner', 'Last Activity Date', 'Next Activity Date',
               'Construction Stage', 'Owner Assigned Date', 'Contractor Refrigeration Phone',
               'Contractor Plumber Plumbing Phone', 'Work Descrption', 'Tent Contractor Address',
               'Deal Stage', 'Number of Contacts', 'Original Source Data 1',
               'Original Source Data 2', 'Residental Real Estate Dev Address', 'Issue Date',
               'Last Contacted', 'HubSpot Team', 'Contractor Refrigeration Address',
               'Contractor Ventilation Name', 'Deal Name', 'Contractor Plumber Plumbing Address',
               'Amount', 'Permit Issue Date', 'Structural Engineer Name', 'Expeditor Phone',
               'Owner Occupied Phone', 'Permit', 'Masonry Contractor Name',
               'Owner As General Contractor Phone', 'Self Cert Architect Phone', 'Deal Description',
               'Owner As General Contractor Name', 'Self Cert Architect Name', 'Permit Type',
               'Masonry Contractor Phone', 'Deal Other Name', 'Amount in company currency',
               'Owner As Architect  Contractr Name', 'Expeditor Address', 'Permits Amount',
               'Owner Occupied Address', 'Associated Company ID', 'Associated Company',
               'Associated Contact IDs', 'Associated Contacts']
    delimiter = ','

    contacts_data = pd.read_csv('/media/alxfed/toca/aa-crm/contacts_stripped_csv_file_result.csv')

    ''' will not be used:
            'Closed Won Reason', 'Owner Occupied Name', 'Expeditor Name',
               'Last Modified Date', 'Owner As Architect  Contractr Address',
               'Owner As General Contractor Address', 'Contractor Ventilation Phone',
               'Self Cert Architect Address', 'Pipeline', 'Masonry Contractor Address',
               'Permit #', 'Structural Engineer Address', 'Deal Type',
               'Number of times contacted', 'Number of Sales Activities',
               'Contractor Ventilation Address', 'Contractor Plumber Plumbing Name',
               'Original Source Type', 'Contractor Refrigeration Name', 'Create Date',
               'Contractor General Contractor Address', 'Deal Stage',
               'Residental Real Estate Dev Name', 'Closed Lost Reason',
               'Tent Contractor Phone', 'Tent Contractor Name', 'Residental Real Estate Dev Phone',
               'Zipcode', 'Design Date', 'Deal owner', 'Last Activity Date', 'Next Activity Date',
               'Construction Stage', 'Owner Assigned Date', 'Contractor Refrigeration Phone',
               'Contractor Plumber Plumbing Phone', 'Work Descrption', 'Tent Contractor Address',
               'Deal Stage', 'Number of Contacts', 'Original Source Data 1',
               'Original Source Data 2', 'Residental Real Estate Dev Address', 'Issue Date',
               'Last Contacted', 'HubSpot Team', 'Contractor Refrigeration Address',
               'Contractor Ventilation Name', 'Contractor Plumber Plumbing Address',
               'Permit Issue Date', 'Structural Engineer Name', 'Expeditor Phone',
               'Owner Occupied Phone', 'Permit', 'Masonry Contractor Name',
               'Owner As General Contractor Phone', 'Self Cert Architect Phone', 'Deal Description',
               'Owner As General Contractor Name', 'Self Cert Architect Name', 'Permit Type',
               'Masonry Contractor Phone', 'Deal Other Name', 'Amount in company currency',
               'Owner As Architect  Contractr Name', 'Expeditor Address', 'Permits Amount',
               'Owner Occupied Address', 
               'Associated Contact IDs', 'Associated Contacts'
    '''
    '''Mandatory
        Account Name/Account CRM ID
        Amount
        Close Date
        Closed
        Opportunity CRM ID
        Opportunity Name
        Owner Email Address
        Primary Contact Email Address/Contact CRM ID
        Probability
        Stage Name
        Won
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
            # mandatory
            line.update({'Account CRM ID': row['Associated Company ID']})
            #line.update({'Account Name': row['Associated Company']})
            line.update({'Amount': row['Amount']})
            line.update({'Close Date': row['Close Date']})
            line.update({'Closed': ''}) # 0 or 1
            line.update({'Create Date': row['Create Date']}) #
            line.update({'Description': row['Deal Description']}) # Deal Description
            line.update({'Opportunity CRM ID': row['Deal ID']})
            line.update({'Opportunity Name': row['Deal Name']})
            # not in the file
            contact_ids = row['Associated Contact IDs']
            owner_email = self.contacts_data.loc[
                self.contacts_data['Contact CRM ID'] == contact_ids[0]]['Email Address'].values[0]
            line.update({'Owner Email Address': row['']})
            line.update({'Primary Contact CRM ID': contact_ids[0]})
            # not in the file
            contact_email = self.contacts_data.loc[
                self.contacts_data['Contact CRM ID'] == contact_ids[0]]['Email Address'].values[0]
            line.update({'Primary Contact Email Address/Contact CRM ID': contact_email})
            # probability calculated
            prob = pro(row['Deal Stage']) # function
            line.update({'Probability': str(prob)}) # in %, 10, 90 ...
            line.update({'Stage Name': row['Deal Stage']})
            won = wo()  # won or lost
            line.update({'Won': row['']}) # 0 - lost, 1 - won
            # optional
            line.update({'Other Contact CRM IDs': row['']})
            yield line
