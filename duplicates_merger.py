# Take 2 rows where 'Name' is identical and 'Unit No.' is 'Blank' or present in both datasets.
# Merge the datasets on 'Name' and 'Unit No.' columns.
# Keep the values where present and replace 'Blank' with the value from the other dataset in all the columns.
# Calculate values for all the columns after 'Name' column based on the values from both datasets
# Save the result to a CSV file.

import pandas as pd

from helpers import convert_to_numeric
from anomalies_discovery import find_anomalies
from load_and_clean_data import load_and_clean_data


def merge_anomalies(path_to_csv, output_directory):
    df = load_and_clean_data(path_to_csv)
    anomalies = find_anomalies(df)
    original_columns = anomalies.columns.tolist()  # Store the original column order

    merged_anomalies = anomalies.groupby(['Name'], as_index=False).agg('first')
    # Re-order the DataFrame to match the original column order
    merged_anomalies = merged_anomalies[original_columns]

    return merged_anomalies


def merge_duplicates(path_to_csv, output_directory):
    df = load_and_clean_data(path_to_csv)

    # Store the original column order
    original_columns = df.columns.tolist()

    # Specify columns to sum and to take the first value of
    sum_columns = ['Jan-24', 'Feb-24', 'Mar-24', 'Apr-24', 'May-24', 'Jun-24',
                   'Jul-24', 'Aug-24', 'Sep-24', 'Oct-24', 'Nov-24', 'Dec-24']


    # Convert values in sum_columns to numeric
    for col in sum_columns:
        df.loc[:, col] = df.loc[:, col].apply(convert_to_numeric)

    df.to_csv(f"{output_directory}/converted_values_for_sum_columns.csv", index=False)

    first_columns = [col for col in df.columns if col not in sum_columns and col != 'Name']

    # Define aggregation dictionary
    agg_dict = {col: 'sum' for col in sum_columns}
    agg_dict.update({col: 'first' for col in first_columns})

    # Apply grouping and aggregation
    merged_duplicates = df.groupby(['Name'], as_index=False).agg(agg_dict)

    # Re-order the DataFrame to match the original column order
    merged_duplicates = merged_duplicates[original_columns]

    # Optionally, save the merged DataFrame to a CSV file
    merged_duplicates.to_csv(f"{output_directory}/final_merge.csv", index=False)
    return merged_duplicates


def print_merges(path_to_csv, output_directory):
    anomalies = merge_anomalies(path_to_csv, output_directory)
    duplicates = merge_duplicates(path_to_csv, output_directory)
    merged = pd.concat([anomalies, duplicates]).drop_duplicates()
    merged.to_csv(f"{output_directory}/merges.csv", index=False)
    print("done")

