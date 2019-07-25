# -*- coding: utf-8 -*-
import pandas as pd

#data = pd.read_csv('/media/alxfed/toca/aa-crm/old-deals-corrected.csv')
#cont = pd.read_csv('/media/alxfed/toca/aa-crm/contacts_csv_file_full_result.csv')


def DealStage(stage):
    """
    :type stage: str
    """
    probability = ''
    deal_won = ''
    deal_closed = ''
    if stage.startswith('Received layout - Make quote'):
        out_stage = 'Layout received'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Design / Estimate / Revisions'):
        out_stage = 'Layout received'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Design / Estimates Completed'):
        out_stage = 'Design completed/Quote ready'
        probability = '50'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Quote Read to be Sent'):
        out_stage = 'Design completed/Quote ready'
        probability = '50'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Quote sent out'):
        out_stage = 'Quote sent out - follow up'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Send Out To Measure'):
        out_stage = 'Quote sent out - follow up'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('To be Checked for Final Approval by Lead Designer'):
        out_stage = 'Quote sent out - follow up'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Approved by Lead Designer - Ready For Contract'):
        out_stage = 'Final review approved by lead designer'
        probability = '80'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Client Approved / Contract Send Out'):
        out_stage = 'Final review approved by lead designer'
        probability = '80'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Contract Signed'):
        out_stage = 'Final review approved by lead designer'
        probability = '95'
        deal_won = '0'
    elif stage.startswith('Deposit Collected'):
        out_stage = 'Contract signed/deposit collected'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Deposit Collected'):
        out_stage = 'Contract signed/deposit collected'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('In Production'):
        out_stage = 'In Production'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Production Finished / Ready For Delivery'):
        out_stage = 'In Production'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Balance Collected'):
        out_stage = 'Delivery/pickup scheduled'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Delivery'):
        out_stage = 'Delivery/pickup scheduled'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Pick Up'):
        out_stage = 'Delivery/pickup scheduled'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Closed / Delivered'):
        out_stage = 'Won'
        probability = '100'
        deal_won = '1'
        deal_closed = '0'
    elif stage.startswith('Lost / Never Ordered'):
        out_stage = 'Never Ordered'
        probability = '100'
        deal_won = '0'
        deal_closed = '1'
    elif stage.startswith('Unknown'):
        out_stage = 'Never Ordered'
        probability = '10'
        deal_won = '0'
        deal_closed = '1'
    return out_stage, probability, deal_won, deal_closed


def ContactEmail(contactid):
    contact_email = cont.loc[cont['Contact CRM ID'] == contactid]['Email Address'].values[0]
    return contact_email


def ContactOwnerEmail(contactid):
    owner_email = cont.loc[cont['Contact CRM ID'] == contactid]['Owner Email'].values[0]
    return owner_email


output = pd.DataFrame()

ds = DealStage('Design / Estimates Completed')

print('ok')

    # data['Deal Stage'].map(lambda x: DealStage(x))

# output.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/pandas_test.csv', index=False)