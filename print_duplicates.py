import pandas as pd

from load_and_clean_data import load_and_clean_data


def filter_unit_numbers_by_criteria(df):
    # Filter to include rows where 'Unit No.' is not 'Blank'
    df_filtered = df[df['Unit No.'] != 'Blank']
    # Find 'Unit No.' that appear more than twice
    multiple_unit_nos = df_filtered['Unit No.'].value_counts()[lambda x: x > 2].index

    # Filter rows based on 'Unit No.' criteria
    multiples = df_filtered[df_filtered['Unit No.'].isin(multiple_unit_nos)]
    alphanumeric = df_filtered[df_filtered['Unit No.'].str.contains('[a-zA-Z]') & df_filtered['Unit No.'].str.contains('[0-9]')]
    alpha = df_filtered[df_filtered['Unit No.'].str.isalpha()]
    return pd.concat([multiples, alphanumeric, alpha]).drop_duplicates()


def find_duplicates(df):
    unit_no_counts = df['Unit No.'].value_counts()
    duplicate_unit_nos = unit_no_counts[unit_no_counts == 2].index.tolist()
    duplicates = df[df['Unit No.'].isin(duplicate_unit_nos) & (df['Unit No.'] != 'Blank')]
    return duplicates


def output_new_df(df, path_to_output_file):
    df.to_csv(path_to_output_file, index=False)


def print_multiples(path_to_csv, output_directory):
    path_to_output_file = f"{output_directory}/non_standard_unit_nos.csv"
    df = load_and_clean_data(path_to_csv)
    multiples = filter_unit_numbers_by_criteria(df)
    output_new_df(multiples, path_to_output_file)

def print_duplicates(path_to_csv, output_directory):
    path_to_output_file = f"{output_directory}/duplicates.csv"
    df = load_and_clean_data(path_to_csv)
    duplicates = find_duplicates(df)
    output_new_df(duplicates, path_to_output_file)