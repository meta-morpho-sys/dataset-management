import pandas as pd


def load_and_clean_data(path_to_csv):
    df = pd.read_csv(path_to_csv)
    df.columns = df.columns.str.strip()
    df[['Unit No.', 'Name']] = df[['Unit No.', 'Name']].fillna('Blank')
    return df
