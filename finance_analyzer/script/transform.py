import pandas as pd
import datetime
import numpy as np

def categorize(description):
    if 'starbucks' in description.lower():
        return 'Coffee'
    elif 'salary' in description.lower():
        return 'Income'
    elif 'fruit' in description.lower():
        return 'Food'
    elif 'food' in description.lower():
        return 'Food'
    elif 'uber' in description.lower():
        return 'Transport'
    else:
        return 'Other'

def transform_data(df):
    df['Category'] = df['Description'].apply(categorize)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    df = df.apply(clean_value)

    return df

def clean_value(val):
    # making data compatible with sqlite
    if isinstance(val, (datetime.datetime, datetime.date)):
        return val.isoformat()
    elif isinstance(val, float) and np.isnan(val):
        return None
    elif isinstance(val, (np.int64, np.float64)):
        return val.item()
    elif isinstance(val, (dict, list)):
        return str(val)
    return val


def get_monthly_spending(transformed_df):
    return transformed_df[transformed_df['Type'].str.strip() != 'Debit'].groupby('Month')['Amount'].sum().to_frame()


def get_data_by_category(transformed_df):
    return transformed_df.groupby('Category')['Amount'].sum().to_frame()
