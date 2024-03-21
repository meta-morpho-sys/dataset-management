import pandas as pd

from load_and_clean_data import load_and_clean_data


def find_duplicates(df):
    unit_no_counts = df['Unit No.'].value_counts()
    multiple_unit_nos = unit_no_counts[unit_no_counts > 2].index.tolist()
    duplicates = df[df['Unit No.'].isin(multiple_unit_nos) & (df['Unit No.'] != 'Blank')]
    alphanumeric = df[df['Unit No.'].str.contains('[a-zA-Z]') & df['Unit No.'].str.contains('[0-9]')]
    alpha = df[df['Unit No.'].str.isalpha() & (df['Unit No.'] != 'Blank')]
    return pd.concat([duplicates, alphanumeric, alpha]).drop_duplicates()

def output_duplicates(df, path_to_output_file):
    df.to_csv(path_to_output_file, index=False)

def print_duplicates(path_to_csv, output_directory):
    path_to_output_file = f"{output_directory}/duplicates.csv"
    df = load_and_clean_data(path_to_csv)
    duplicates = find_duplicates(df)
    output_duplicates(duplicates, path_to_output_file)