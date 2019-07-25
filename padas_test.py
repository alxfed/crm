# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('/media/alxfed/toca/aa-crm/old-deals-corrected.csv')
cont = pd.read_csv('/media/alxfed/toca/aa-crm/contacts_csv_file_full_result.csv')


def DealStage(stage):
    probability = ''
    deal_won = ''
    deal_closed = ''
    if stage.startswith('Received layout - Make quote'):
        stage = 'Layout received'
        probability = '30'
        deal_won = '0'
        deal_closed = '0'
    elif stage.startswith('Design / Estimate / Revisions'):
        stage = 'Layout received'
        probability = '30'
        won = '0'
    elif stage.startswith('Design / Estimates Completed'):
        stage = 'Design completed/Quote ready'
        probability = '50'
        won = '0'
    elif stage.startswith('Quote Read to be Sent'):
        stage = 'Design completed/Quote ready'
        probability = '50'
        won = '0'
    elif stage.startswith('Quote sent out'):
        stage = 'Quote sent out - follow up'
        probability = '30'
        won = '0'
    elif stage.startswith('Send Out To Measure'):
        stage = 'Quote sent out - follow up'
        probability = '30'
        won = '0'
    elif stage.startswith('To be Checked for Final Approval by Lead Designer'):
        stage = 'Quote sent out - follow up'
        probability = '30'
        won = '0'
    elif stage.startswith('Approved by Lead Designer - Ready For Contract'):
        stage = 'Final review approved by lead designer'
        probability = '80'
        won = '0'
    elif stage.startswith('Client Approved / Contract Send Out'):
        stage = 'Final review approved by lead designer'
        probability = '80'
        won = '0'
    elif stage.startswith('Contract Signed'):
        stage = 'Final review approved by lead designer'
        probability = '95'
        won = '0'
    elif stage.startswith('Deposit Collected'):
        stage = 'Contract signed/deposit collected'
        probability = '100'
        won = '1'
    elif stage.startswith('Deposit Collected'):
        stage = 'Contract signed/deposit collected'
        probability = '100'
        won = '1'
    elif stage.startswith('In Production'):
        stage = 'In Production'
        probability = '100'
        won = '1'
    elif stage.startswith('Production Finished / Ready For Delivery'):
        stage = 'In Production'
        probability = '100'
        won = '1'
    elif stage.startswith('Balance Collected'):
        stage = 'Delivery/pickup scheduled'
        probability = '100'
        won = '1'
    elif stage.startswith('Delivery'):
        stage = 'Delivery/pickup scheduled'
        probability = '100'
        won = '1'
    elif stage.startswith('Pick Up'):
        stage = 'Delivery/pickup scheduled'
        probability = '100'
        won = '1'
    elif stage.startswith('Closed / Delivered'):
        stage = 'Won'
        probability = '100'
        won = '1'
    elif stage.startswith('Lost / Never Ordered'):
        stage = 'Never Ordered'
        probability = '100'
        won = '0'
    elif stage.startswith('Unknown'):
        stage = 'Never Ordered'
        probability = '10'
        won = '0'
        return stage #, probability, deal_won, deal_closed


def ContactEmail(contactid):
    contact_email = cont.loc[cont['Contact CRM ID'] == contactid]['Email Address'].values[0]
    return contact_email


def ContactOwnerEmail(contactid):
    owner_email = cont.loc[cont['Contact CRM ID'] == contactid]['Owner Email'].values[0]
    return owner_email


output = pd.DataFrame()

output['Deal Stage'] = data['Deal Stage'].map(DealStage)

output.to_csv(path_or_buf='/media/alxfed/toca/aa-crm/pandas_test.csv', index=False)