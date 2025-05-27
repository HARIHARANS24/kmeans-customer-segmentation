def clean_data(df):
    return df.dropna().drop_duplicates()