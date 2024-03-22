# Take 2 rows where 'Name' is identical and 'Unit No.' is 'Blank' or present in both datasets.
# Merge the datasets on 'Name' and 'Unit No.' columns.
# Keep the values where present and replace 'Blank' with the value from the other dataset in all the columns.
# Calculate values for all the columns after 'Name' column based on the values from both datasets
# Save the result to a CSV file.

import pandas as pd
from print_duplicates import find_duplicates
from anomalies_discovery import find_anomalies
from load_and_clean_data import load_and_clean_data


def convert_to_numeric(value):
    # First, check if the value is a string. If not, return the value as is.
    if isinstance(value, str):
        # If it's a string, check for parentheses and commas for conversion
        try:
            if value.startswith('(') and value.endswith(')'):
                # Remove parentheses, replace commas, and convert to negative float
                return -pd.to_numeric(value.strip('()').replace(',', ''), errors='coerce')
            else:
                # Replace commas and convert to float
                return pd.to_numeric(value.replace(',', ''), errors='coerce')
        except ValueError:
            # In case of a ValueError during conversion, return NaN to indicate failure
            return pd.np.nan
    else:
        # If the value is already numeric (int, float), return it as is
        return value


def merge_anomalies(path_to_csv, output_directory):
    df = load_and_clean_data(path_to_csv)
    anomalies = find_anomalies(df)
    merged_anomalies = anomalies.groupby(['Name'], as_index=False).agg('first')

    return merged_anomalies


def merge_duplicates(path_to_csv, output_directory):
    df = load_and_clean_data(path_to_csv)
    duplicates = find_duplicates(df)

    # Specify columns to sum and to take the first value of
    sum_columns = ['Jan-24', 'Feb-24', 'Mar-24', 'Apr-24', 'May-24', 'Jun-24',
                   'Jul-24', 'Aug-24', 'Sep-24', 'Oct-24', 'Nov-24', 'Dec-24']

    # Convert values in sum_columns, treating parentheses as negative
    for col in sum_columns:
        duplicates[col] = duplicates[col].apply(convert_to_numeric)

    first_columns = [col for col in duplicates.columns if col not in sum_columns and col != 'Name']

    # Define aggregation dictionary
    agg_dict = {col: 'sum' for col in sum_columns}
    agg_dict.update({col: 'first' for col in first_columns})

    # Apply grouping and aggregation
    merged_duplicates = duplicates.groupby(['Name'], as_index=False).agg(agg_dict)

    # Optionally, save the merged DataFrame to a CSV file
    merged_duplicates.to_csv(f"{output_directory}/merged_duplicates.csv", index=False)

    return merged_duplicates

def print_merges(path_to_csv, output_directory):
    anomalies = merge_anomalies(path_to_csv, output_directory)
    duplicates = merge_duplicates(path_to_csv, output_directory)
    merged = pd.concat([anomalies, duplicates]).drop_duplicates()
    print("merged")
    print(merged)
    merged.to_csv(f"{output_directory}/merges.csv", index=False)
    print("done")

