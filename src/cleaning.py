import pandas as pd
import numpy as np

from drop_and_fill import drop_and_fill


# function for removing cylinders string at field cylinders
def cylinders_to_string(s):
    if isinstance(s, str) and 'cylinders' in s:
        return int(s.split(' ')[0])
    else:
        return np.nan

# function for  changing strings into numbers
def get_transmission_values(s):
    if s =='automatic':
        return 1
    elif s =='manual':
        return 0
    else:
        return np.NaN

# get dummies function
def dummify(df):  
    df = pd.get_dummies(df, ['condition', 'fuel', 'size', 'type'])
    return df

def transform_string_values(df):
    df['cylinders'] = df['cylinders'].apply(cylinders_to_string)
    df['transmission'] = df['transmission'].apply(get_transmission_values)
    return df

def get_cleaner_data(df):
    df = transform_string_values(df)
    df = drop_and_fill(df)
    df = dummify(df)
    return df