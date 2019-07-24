# -*- coding: utf-8 -*-
#import pandas as pd
from collections import OrderedDict
from scrapy.spiders import CSVFeedSpider


class CsvfeedSpider(CSVFeedSpider):
    name = 'contacts_csv_file'
    allowed_domains = ['google.com']
    start_urls = ['file:///media/alxfed/toca/aa-crm/old-contacts.csv']
    headers = ['Contact ID', 'First Name', 'Last Name',
               'Time registration email was sent', 'Last marketing email name',
               'Status', 'Registered At', 'Marketing emails opened', 'Lead Status',
               'Total Revenue', 'Gender', 'Postal Code', 'Last Contract Viewed Date',
               'Klout Score', 'IP City', 'Company size',
               'Last Touch Converting Campaign', 'First Touch Converting Campaign',
               'Recent Deal Close Date', 'Number of Pageviews',
               "Legal basis for processing contact's data",
               'Became a Marketing Qualified Lead Date', 'Military status',
               'Last Meeting Booked Campaign', 'Time of Last Visit',
               'Time of First Visit', 'Close Date', 'Do you have a showroom? ',
               'Field of study', 'Message', 'HelloSign Meta 30', 'Associated Deals',
               'HelloSign Meta 1', 'Recent Deal Amount',
               'Opted out of email: Marketing Information', 'HelloSign Meta 20',
               'Do you have a dedicated kitchen designer? ', 'Number of times contacted',
               'Number of Sales Activities', 'HelloSign Meta 2', 'First Conversion Date',
               'Date of birth', 'Recent Sales Email Clicked Date',
               'Recent Sales Email Opened Date', 'Original Source', 'HelloSign Meta 21',
               'HelloSign Meta 3', 'First Deal Created Date', 'HelloSign Meta 10',
               'Number of Form Submissions', 'HelloSign Meta 22',
               'Opted out of email: One to One', 'Currently in workflow',
               'HelloSign Meta 4', 'Last Meeting Booked Medium', 'Create Date',
               'LinkedIn Bio', 'First Conversion', 'Became a Sales Qualified Lead Date',
               'Last Meeting Booked', 'HelloSign Meta 11', 'HelloSign Meta 23',
               'First marketing email click date', 'HelloSign Meta 5', 'City',
               'Start date', 'How did you hear about Marfa Cabinets Inc? ',
               'HelloSign Meta 12', 'Preferred language', 'HelloSign Meta 24',
               'HelloSign Meta 6', 'Mobile Phone Number', 'Number of event completions',
               'Degree', 'HelloSign Meta 13', 'HelloSign Meta 25', 'Average Pageviews',
               'Marketing emails delivered', 'HelloSign Meta 7',
               'Number of Unique Forms Submitted', 'Email Confirmed', 'Last Modified Date',
               'HelloSign Meta 14', 'HelloSign Meta 26', 'Number of Visits', 'Work email',
               'IP Country Code', 'HelloSign Meta 8', 'Phone Number', 'Became a Subscriber Date',
               'HelloSign Meta 15', 'HelloSign Meta 27', 'HelloSign Meta 9',
               'Marketing email confirmation status', 'Contact owner', 'Event Revenue',
               'HelloSign Meta 16', 'HelloSign Meta 28', 'Last Activity Date',
               'Next Activity Date', 'HelloSign CC', 'Last Meeting Booked Source',
               'Owner Assigned Date', 'HelloSign Meta 17', 'HelloSign Meta 29',
               'State/Region', 'Became an Opportunity Date', 'Marketing emails clicked',
               'Follower Count', 'Last marketing email open date', 'HelloSign Meta 18',
               'Unsubscribed from all email', 'Membership Notes', 'HelloSign Meta 19',
               'Last Page Seen', 'First Page Seen', 'Original Source Drill-Down 1',
               'Last marketing email send date', 'IP State Code/Region Code',
               'Recent Conversion Date', 'Became an Other Lifecycle Date',
               'Dealer Registration Comments', 'Original Source Drill-Down 2',
               'Lifecycle Stage', 'School', 'Last Contacted', 'Street Address',
               'Recent Conversion', 'HubSpot Team', 'Twitter Bio', 'Not interested',
               'What other brands of kitchen cabinetry do you currently offer?',
               'Country', 'LinkedIn Connections', 'Last marketing email click date',
               'Persona', 'Salutation', 'Sends Since Last Engagement', 'Became a Customer Date',
               'Currently in Sequence', 'IP State/Region', 'Relationship Status', 'Time Last Seen',
               'Time First Seen', 'Job function', 'Became a Lead Date',
               'Recent Sales Email Replied Date', 'What design software do you use?',
               'Last Contract Signed Date', 'Website URL', 'Job Title', 'Email Domain',
               'HubSpot Score', 'Twitter Username', 'First Referring Site',
               'Last Referring Site', 'Twitter Profile Photo', 'Became an Evangelist Date',
               'Days To Close', 'Email', 'Company Name', 'Annual Revenue', 'Marital Status',
               'First marketing email open date', 'IP Timezone', 'Fax Number',
               'Pending Signature', 'IP Country', 'Seniority', 'Industry',
               'Domain to which registration email was sent', 'First marketing email send date',
               'Email Address Quarantined', 'Graduation date', 'Number of Employees',
               'Marketing emails bounced', 'Associated Company ID', 'Associated Company']
    delimiter = ','

    #owners_emails = pd.read_csv('/media/alxfed/toca/aa-crm/old-owners-emals.csv')

    ''' will not be used: 
               'Time registration email was sent', 'Last marketing email name', 
               'Status', 'Registered At', 'Marketing emails opened',  
               'Gender', 'Last Contract Viewed Date', 
               'Klout Score', 'IP City', 'Company size', 
               'Last Touch Converting Campaign', 'First Touch Converting Campaign', 
               'Number of Pageviews', 
               "Legal basis for processing contact's data", 
               'Became a Marketing Qualified Lead Date', 'Military status', 
               'Last Meeting Booked Campaign',  
               'Close Date', 'Do you have a showroom? ', 
               'Field of study', 'Message', 'HelloSign Meta 30', 'Associated Deals', 
               'HelloSign Meta 1', 
               'Opted out of email: Marketing Information', 'HelloSign Meta 20', 
               'Do you have a dedicated kitchen designer? ', 'Number of times contacted', 
               'Number of Sales Activities', 'HelloSign Meta 2', 
               'Date of birth', 'Recent Sales Email Clicked Date', 
               'Recent Sales Email Opened Date', 'Original Source', 'HelloSign Meta 21', 
               'HelloSign Meta 3', 'HelloSign Meta 10', 
               'Number of Form Submissions', 'HelloSign Meta 22', 
               'Opted out of email: One to One', 'Currently in workflow', 
               'HelloSign Meta 4', 'Last Meeting Booked Medium',  
               'LinkedIn Bio', 'First Conversion', 'Became a Sales Qualified Lead Date', 
               'Last Meeting Booked', 'HelloSign Meta 11', 'HelloSign Meta 23', 
               'First marketing email click date', 'HelloSign Meta 5', 
               'Start date', 'How did you hear about Marfa Cabinets Inc? ', 
               'HelloSign Meta 12', 'Preferred language', 'HelloSign Meta 24', 
               'HelloSign Meta 6', 'Number of event completions', 
               'Degree', 'HelloSign Meta 13', 'HelloSign Meta 25', 'Average Pageviews', 
               'Marketing emails delivered', 'HelloSign Meta 7', 
               'Number of Unique Forms Submitted', 'Email Confirmed', 
               'HelloSign Meta 14', 'HelloSign Meta 26', 'Number of Visits', 
               'IP Country Code', 'HelloSign Meta 8', 'Became a Subscriber Date', 
               'HelloSign Meta 15', 'HelloSign Meta 27', 'HelloSign Meta 9', 
               'Marketing email confirmation status', 'Event Revenue', 
               'HelloSign Meta 16', 'HelloSign Meta 28', 'Last Activity Date', 
               'Next Activity Date', 'HelloSign CC', 'Last Meeting Booked Source', 
               'Owner Assigned Date', 'HelloSign Meta 17', 'HelloSign Meta 29', 
               'Became an Opportunity Date', 'Marketing emails clicked', 
               'Follower Count', 'Last marketing email open date', 'HelloSign Meta 18', 
               'Membership Notes', 'HelloSign Meta 19', 
               'Last Page Seen', 'First Page Seen', 'Original Source Drill-Down 1', 
               'Last marketing email send date', 'IP State Code/Region Code', 
               'Recent Conversion Date', 'Became an Other Lifecycle Date', 
               'Dealer Registration Comments', 'Original Source Drill-Down 2', 
               'School', 'Last Contacted',
               'Recent Conversion', 'HubSpot Team', 'Twitter Bio', 'Not interested', 
               'What other brands of kitchen cabinetry do you currently offer?', 
               'LinkedIn Connections', 'Last marketing email click date', 
               'Persona', 'Salutation', 'Sends Since Last Engagement', 'Became a Customer Date', 
               'Currently in Sequence', 'IP State/Region', 'Relationship Status', 'Time Last Seen', 
               'Time First Seen', 'Became a Lead Date', 
               'Recent Sales Email Replied Date', 'What design software do you use?', 
               'Last Contract Signed Date', 
               'HubSpot Score', 'Twitter Username', 'First Referring Site', 
               'Last Referring Site', 'Twitter Profile Photo', 'Became an Evangelist Date', 
               'Days To Close', 'Annual Revenue', 'Marital Status', 
               'First marketing email open date', 'IP Timezone', 'Fax Number', 
               'Pending Signature', 'IP Country', 'Seniority', 
               'Domain to which registration email was sent', 'First marketing email send date', 
               'Email Address Quarantined', 'Graduation date', 'Number of Employees', 
               'Marketing emails bounced'
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
            # mandatory:
            line.update({'Account Name/Account CRM ID': row['Associated Company ID']})
            line.update({'Company Name': row['Company Name']})
            line.update({'Contact CRM ID': row['Contact ID']})
            line.update({'Email Address': row['Email']})
            line.update({'Is Unsubscribed': row['Unsubscribed from all email']})
            line.update({'First Name': row['First Name']})
            line.update({'Last Name': row['Last Name']})
            # optional about the person:
            line.update({'Job function': row['Job function']})
            line.update({'Job Title': row['Job Title']})
            line.update({'Lifecycle Stage': row['Lifecycle Stage']})
            line.update({'Lead Status': row['Lead Status']})
            line.update({'Create Date': row['Create Date']})
            line.update({'Close Date': row['Close Date']})
            line.update({'Last Modified Date': row['Last Modified Date']})
            line.update({'Phone': row['Phone Number']})
            line.update({'Mobile Phone Number': row['Mobile Phone Number']})
            line.update({'Time of Last Visit': row['Time of Last Visit']})
            line.update({'Time of First Visit': row['Time of First Visit']})
            line.update({'Last Activity Date': row['Last Activity Date']})
            line.update({'First Conversion': row['First Conversion']})
            line.update({'First Conversion Date': row['First Conversion Date']})
            owner = row['Contact owner']
            line.update({'Contact owner': owner})

            '''
            owner_email = self.owners_emails.loc[
                self.owners_emails['Owner'] == owner]['Owner Email'].values[0]
            line.update({'Owner Email': owner_email})
            '''
            # about the company:
            # line.update({'Street Address': row['Street Address']})
            # line.update({'City': row['City']})
            # line.update({'State/Region': row['State/Region']})
            # line.update({'Postal Code': row['Postal Code']})
            # line.update({'Country': row['Country']})
            line.update({'Website': row['Website URL']})
            line.update({'Email Domain': row['Email Domain']})
            line.update({'Work email': row['Work email']})
            # deals
            line.update({'Associated Deals': row['Recent Deal Close Date']})
            line.update({'Recent Deal Close Date': row['Recent Deal Close Date']})
            line.update({'Recent Deal Amount': row['Recent Deal Amount']})
            line.update({'First Deal Created Date': row['First Deal Created Date']})
            # money:
            line.update({'Total Revenue': row['Total Revenue']})
            yield line
