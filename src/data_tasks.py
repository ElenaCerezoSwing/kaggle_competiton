import pandas as pd

def save_data(df, name):
    df.to_csv('../output_data/{}.csv'.format(name), index=False)

def load_train_data():
    return pd.read_csv('../data/cars_train.csv')

def load_test_data():
    return pd.read_csv('../data/cars_test.csv')


def load_submission_data():
    return pd.read_csv('../data/cars_sample_submission.csv.zip')

def get_dataframe_copy(df):
    return df.copy()