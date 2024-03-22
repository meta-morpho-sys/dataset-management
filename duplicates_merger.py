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
    sum_columns = ['Jan-24', 'Feb-24', 'Mar-24', 'Apr-24', 'May-24', 'Jun-24', 'Jul-24', 'Aug-24', 'Sep-24', 'Oct-24', 'Nov-24', 'Dec-24']
    first_columns = [col for col in df.columns if col not in sum_columns and col != 'Name']

    df[sum_columns] = df[sum_columns].map(convert_to_numeric)
    agg_dict = {**{col: 'sum' for col in sum_columns}, **{col: 'first' for col in first_columns}}

    merged_duplicates = df.groupby(['Name'], as_index=False).agg(agg_dict)[df.columns.tolist()]
    merged_duplicates.to_csv(f"{output_directory}/final_merge.csv", index=False)
    return merged_duplicates


