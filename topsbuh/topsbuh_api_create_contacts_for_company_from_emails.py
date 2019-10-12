import requests
import os
import csv
from collections import OrderedDict
from random import randint


API_KEY = os.environ['API_KEY']
CONTACT_CREATE_OR_UPDATE_URL = 'https://api.hubapi.com/contacts/v1/contact/createOrUpdate/email/'
companies_created_with_emails_path = '/media/alxfed/toca/aa-crm/kb-designers/upload/kitchen_and_bath_designers_created_with_emails.csv'
existing_contacts_url = '/media/alxfed/toca/aa-crm/work/all-contacts.csv'
contacts_created_path = '/media/alxfed/toca/aa-crm/kb-designers/upload/kitchen_and_bath_designers_contacts_created.csv'

headers = {"Content-Type": "application/json"}
querystring = {"hapikey": API_KEY}

input_columns = ['Name', 'Type', 'Phone Number', 'Phone Mobile',
                 'Phone VoIP', 'Phone Toll', 'Phone Landline',
                 'Phone Unidentified', 'Address', 'City',
                 'Zipcode', 'State', 'Category', 'Website',
                 'Facebook', 'Twitter', 'Google', 'Linkedin',
                 'companyId', 'emails']

contact_columns = ['Contact ID', 'First Name', 'Last Name', 'Broadcast Clicks',
                   'Time registration email was sent', 'Last marketing email name',
                   'Status', 'Registered At', 'Marketing emails opened',
                   'Lead Status', 'Guest Type', 'Total Revenue', 'Gender',
                   'Postal Code', 'Mobile', 'Last Contract Viewed Date',
                   'Klout Score', 'IP City', 'Company size', 'NPS Comment',
                   'Last Touch Converting Campaign', 'First Touch Converting Campaign',
                   'Recent Deal Close Date', 'Number of Pageviews',
                   'Legal basis for processing contacts data',
                   'Became a Marketing Qualified Lead Date', 'Military status',
                   'Last Meeting Booked Campaign', 'Time of Last Session',
                   'Time of First Session', 'Facebook Clicks', 'Close Date',
                   'Do you have a showroom? ', 'Field of study', 'Message',
                   'HelloSign Meta 30', 'Associated Deals', 'HelloSign Meta 1',
                   'Address 2', 'Recent Deal Amount',
                   'Opted out of email: Marketing Information', 'HelloSign Meta 20',
                   'Do you have a dedicated kitchen designer? ',
                   'Number of times contacted', 'Number of Sales Activities',
                   'Google Plus Clicks', 'HelloSign Meta 2', 'First Conversion Date',
                   'Date of birth', 'Recent Sales Email Clicked Date',
                   'Recent Sales Email Opened Date', 'Address 3', 'Original Source',
                   'HelloSign Meta 21', 'HelloSign Meta 3', 'Email Two',
                   'First Deal Created Date', 'HelloSign Meta 10',
                   'Number of Form Submissions', 'HelloSign Meta 22',
                   'Opted out of email: One to One', 'unknown ', 'NPS Date',
                   'Currently in workflow', 'HelloSign Meta 4', 'Last Meeting Booked Medium',
                   'Most Recent Social Click', 'Create Date', 'LinkedIn Bio',
                   'First Conversion', 'Became a Sales Qualified Lead Date',
                   'Last Meeting Booked', 'HelloSign Meta 11', 'HelloSign Meta 23',
                   'First marketing email click date',
                   'Opted out of email: Marfa Cabinets Blog Subscription',
                   'HelloSign Meta 5', 'City', 'Start date',
                   'How did you hear about Marfa Cabinets Inc? ', 'HelloSign Meta 12',
                   'Preferred language', 'HelloSign Meta 24', 'Scanner Name', 'HelloSign Meta 6',
                   'Mobile Phone Number', 'Number of event completions', 'Degree',
                   'HelloSign Meta 13', 'HelloSign Meta 25', 'Average Pageviews',
                   'Marketing emails delivered', 'HelloSign Meta 7',
                   'Number of Unique Forms Submitted', 'Email Confirmed', 'Last Modified Date',
                   'HelloSign Meta 14', 'HelloSign Meta 26', 'Number of Sessions',
                   'Work email', 'IP Country Code', 'HelloSign Meta 8', 'Phone Number',
                   'Became a Subscriber Date', 'LinkedIn Clicks', 'HelloSign Meta 15',
                   'HelloSign Meta 27', 'HelloSign Meta 9', 'Marketing email confirmation status',
                   'Contact owner', 'External ID', 'Event Revenue', 'HelloSign Meta 16',
                   'HelloSign Meta 28', 'Scan Date', 'Last Activity Date', 'Next Activity Date',
                   'HelloSign CC', 'Last Meeting Booked Source', 'Owner Assigned Date',
                   'Company Index', 'HelloSign Meta 17', 'HelloSign Meta 29', 'State/Region',
                   'Became an Opportunity Date', 'Marketing emails clicked', 'Follower Count',
                   'Last marketing email open date', 'HelloSign Meta 18',
                   'Opted out of email: Architects, Designers and Remodelers',
                   'Unsubscribed from all email', 'Membership Notes', 'HelloSign Meta 19',
                   'Last Page Seen', 'First Page Seen', 'Original Source Drill-Down 1',
                   'Last marketing email send date', 'IP State Code/Region Code',
                   'Recent Conversion Date', 'Became an Other Lifecycle Date',
                   'Dealer Registration Comments', 'Original Source Drill-Down 2',
                   'Lifecycle Stage', 'School', 'Last Contacted', 'Street Address',
                   'Recent Conversion', 'HubSpot Team', 'Twitter Bio', 'Twitter Clicks',
                   'Not interested', 'When would you like to visit our showroom?',
                   'NPS Score', 'What other brands of kitchen cabinetry do you currently offer?',
                   'Scheduled Showroom visit', 'Country', 'NPS Segment', 'LinkedIn Connections',
                   'Last marketing email click date', 'Persona', 'Salutation',
                   'Sends Since Last Engagement', 'Became a Customer Date',
                   'Currently in Sequence', 'IP State/Region', 'Relationship Status',
                   'Time Last Seen', 'Time First Seen', 'Show Description', 'Job function',
                   'Became a Lead Date', 'Recent Sales Email Replied Date',
                   'What design software do you use?', 'Street address2',
                   'Last Contract Signed Date', 'Website URL', 'Job Title', 'Surname',
                   'Marfa Cabinets Blog Email Subscription', 'Email Domain', 'HubSpot Score',
                   'Twitter Username', 'First Referring Site', 'Last Referring Site',
                   'Twitter Profile Photo', 'Became an Evangelist Date', 'Days To Close',
                   'Exhibitor', 'Country2', 'Email', 'Company Name', 'Annual Revenue',
                   'Marital Status', 'First marketing email open date', 'IP Timezone',
                   'Fax Number', 'Pending Signature', 'IP Country', 'Seniority', 'Industry',
                   'NPS Tag', 'Domain to which registration email was sent',
                   'First marketing email send date', 'Email Address Quarantined',
                   'Graduation date', 'Number of Employees', 'Marketing emails bounced',
                   'Associated Company ID', 'Associated Company']

# emails are in the 'Email' column

# contact create request data
data = {'properties':
    [
        {
          "property": "firstname",
          "value": ""
        },
        {
          "property": "lastname",
          "value": ""
        },
        {
          "property": "company",
          "value": ""
        },
        {
          "property": "company_index",
          "value": ""
        },
        {
          "property": "jobtitle",
          "value": "Kitchen & Bath Designer employee"
        }
    ]
}


# output
output_rows = []
output_columns = ['Name', 'companyId', 'firstname', 'lastname', 'email', 'vid']


with open(companies_created_with_emails_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        output_row = OrderedDict()
        output_row['Name'] = row['Name']
        output_row['companyId'] = row['companyId']
        list_of_emails = row['emails'].split(' ')
        for index, email in enumerate(list_of_emails):
            name, _ = email.split('@')
            lastname = 'Auto_' + str(randint(1, 999999))
            output_row['firstname'] = name
            output_row['lastname'] = lastname
            output_row['email'] = email
            data['properties'][0]['value'] = name
            data['properties'][1]['value'] = lastname
            data['properties'][2]['value'] = row['Name']
            if name.startswith('info'):
                ind = '0'
            else:
                ind = str(index+1)
            data['properties'][3]['value'] = ind
            req_url = '{}{}/'.format(CONTACT_CREATE_OR_UPDATE_URL, email)
            response = requests.request("POST", url=req_url, json=data,
                                        headers=headers, params=querystring)
            if response.status_code == 200:
                output_row['vid'] = response.json()['vid']
            else:
                output_row['vid'] = ''
            output_rows.append(output_row)
            print(output_row, response.status_code)

with open(contacts_created_path,'w') as f:
    f_csv = csv.DictWriter(f, output_columns)
    f_csv.writeheader()
    f_csv.writerows(output_rows)

print('ok')