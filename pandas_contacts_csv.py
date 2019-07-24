'''
template
'''

import pandas as pd

data = pd.read_csv('/media/alxfed/toca/aa-crm/old-contacts.csv')

input_headers = ['Contact ID', 'First Name', 'Last Name',
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

owner_to_email = {
    'Melissa Conroy':	'mconroy@marfacabinets.com',
    'Douglas Sumner':	'dsumner@marfacabinets.com',
    'Ania Keller':	'imidari@marfacabinets.com',
    'Bjorn Berkmortel':	'bberkmortel@marfacabinets.com',
    'Alexander Doroshko':	'sashadoroshko@marfacabinets.com',
    'Alexander Doroshko sashadoroshko@marfacabinets.com': 'sashadoroshko@marfacabinets.com',
    '': 'nobody@marfacabinets.com'
}

output = pd.DataFrame()

# mandatory:
output['Account Name/Account CRM ID'] = data['Associated Company ID']
output['Company Name'] = data['Company Name']
output['Contact CRM ID'] = data['Contact ID']
output['Email Address'] = data['Email']
output['Is Unsubscribed'] = data['Unsubscribed from all email']
output['First Name'] = data['First Name']
output['Last Name'] = data['Last Name']
# optional about the person:
output['Job function'] = data['Job function']
output['Job Title'] = data['Job Title']
output['Lifecycle Stage'] = data['Lifecycle Stage']
output['Lead Status'] = data['Lead Status']
output['Create Date'] = data['Create Date']
output['Close Date'] = data['Close Date']
output['Last Modified Date'] = data['Last Modified Date']
output['Phone'] = data['Phone Number']
output['Mobile Phone Number'] = data['Mobile Phone Number']
output['Time of Last Visit'] = data['Time of Last Visit']
output['Time of First Visit'] = data['Time of First Visit']
output['Last Activity Date'] = data['Last Activity Date']
output['First Conversion'] = data['First Conversion']
output['First Conversion Date'] = data['First Conversion Date']
output['Contact owner'] = data['Contact owner']
output['Owner Email'] = data['Contact owner'].map(owner_to_email)
output['Website'] = data['Website URL']
output['Email Domain'] = data['Email Domain']
output['Work email'] = data['Work email']
# deals
output['Associated Deals'] = data['Recent Deal Close Date']
output['Recent Deal Close Date'] = data['Recent Deal Close Date']
output['Recent Deal Amount'] = data['Recent Deal Amount']
output['First Deal Created Date'] = data['First Deal Created Date']
# money:
output['Total Revenue'] = data['Total Revenue']

output.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/contacts_csv_file_full_result.csv', index=False)