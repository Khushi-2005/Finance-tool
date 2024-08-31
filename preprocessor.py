import re
import pandas as pd
import calendar

def preprocess(df):
    df.rename(columns={"Transaction Statement for 8540015748": "Datetime"}, inplace=True)
    df.rename(columns={"Unnamed: 1": "Name"}, inplace=True)
    df.rename(columns={"Unnamed: 2": "Type"}, inplace=True)
    df.rename(columns={"Unnamed: 3": "Amount"}, inplace=True)
    # print(df)
    df = df.dropna()
    df['Amount'] = df['Amount'].str.replace('₹', '')
    df = df[df['Amount'] != 'Amount']
    df = df[df['Type'] != 'Type']
    df['Datetime'] = pd.to_datetime(df['Datetime'], format='%b %d, %Y', errors='coerce')
    df = df[df['Name'] != 'Paid to']
    df = df[df['Name'] != 'Received from']
    df = df.dropna(subset=['Datetime'])
    def extract_name(row):
        if row['Type'] == 'DEBIT':
            return row['Name'].split('Paid to ')[-1]
        elif row['Type'] == 'CREDIT':
            return row['Name'].split('Received from ')[-1]
        else:
            return row['Name']
    df["Name"] = df.apply(extract_name, axis=1)
    df['Year'] = df['Datetime'].dt.year
    df['Month'] = df['Datetime'].dt.month
    df['Month'] = df['Month'].apply(lambda x: calendar.month_name[int(x)])
    df['Date'] = df['Datetime'].dt.day
    df['Day_of_Week'] = df['Datetime'].dt.day_name()    

    def extract_amount(row):
        if '.' in row['Amount']:
            return row['Amount'].split('.')[0]
        else:
            return row['Amount']
    df['Amount'] = df.apply(extract_amount, axis=1)
    df['Amount'] = df['Amount'].str.replace(',', '').astype(int)
    
    
    return df
