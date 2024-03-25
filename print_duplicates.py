import os

from helpers import filter_unit_numbers_by_criteria, find_duplicates, load_and_clean_data


def output_new_df(df, path_to_output_file):
    df.to_csv(path_to_output_file, index=False)


def detect_non_standard_unit_nos(path_to_csv, output_directory):
    print(os.listdir(output_directory))
    path_to_output_file = f"{output_directory}/insights/non_standard_unit_nos.csv"
    df = load_and_clean_data(path_to_csv)
    multiples = filter_unit_numbers_by_criteria(df)
    output_new_df(multiples, path_to_output_file)


def print_duplicates(path_to_csv, output_directory):
    path_to_output_file = f"{output_directory}/insights/duplicates.csv"
    df = load_and_clean_data(path_to_csv)
    duplicates = find_duplicates(df)
    output_new_df(duplicates, path_to_output_file)