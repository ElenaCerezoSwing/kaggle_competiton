

# function to drop cols
def drop_cols(df):
    df = df.drop(['city', 'county_name', 'county_fips',
              'make', 'manufacturer', 'paint_color',
              'state_code', 'state_name', 'drive', 'title_status'], axis=1, inplace=True)
    return df

def fill_empty(df):
    df = df.fillna(method='bfill', inplace=True)
    return df

def drop_and_fill(df):
    drop_cols(df)
    fill_empty(df)
    return df