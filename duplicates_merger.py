# Take 2 rows where 'Name' is identical and 'Unit No.' is 'Blank' or present in both datasets.
# Merge the datasets on 'Name' and 'Unit No.' columns.
# Keep the values where present and replace 'Blank' with the value from the other dataset in all the columns.
# Calculate values for all the columns after 'Name' column based on the values from both datasets
# Save the result to a CSV file.

import pandas as pd
from print_duplicates import find_multiples
from anomalies_discovery import find_anomalies
from load_and_clean_data import load_and_clean_data

def merge_anomalies(path_to_csv, output_directory):
    df = load_and_clean_data(path_to_csv)
    anomalies = find_anomalies(df)
    # merged_anomalies = anomalies.groupby(['Unit No.', 'Name'], as_index=False).agg('first')
    merged_anomalies = anomalies.groupby(['Name'], as_index=False).agg('first')

    return merged_anomalies

def merge_duplicates(path_to_csv, output_directory):
    df = load_and_clean_data(path_to_csv)
    duplicates = find_multiples(df)
    merged_duplicates = duplicates.groupby(['Unit No.', 'Name'], as_index=False).agg('first')
    return merged_duplicates


def print_merges(path_to_csv, output_directory):
    anomalies = merge_anomalies(path_to_csv, output_directory)
    duplicates = merge_duplicates(path_to_csv, output_directory)
    merged = pd.concat([anomalies, duplicates]).drop_duplicates()
    print("merged")
    print(merged)
    merged.to_csv(f"{output_directory}/merges.csv", index=False)
    print("hi")
