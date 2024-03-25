from helpers import convert_to_numeric, update_lost_names, load_and_clean_data
from anomalies_discovery import find_anomalies


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
    # Update the DataFrame with normalized names
    df = update_lost_names(df)

    sum_columns = ['Jan-24', 'Feb-24', 'Mar-24', 'Apr-24', 'May-24', 'Jun-24', 'Jul-24', 'Aug-24', 'Sep-24', 'Oct-24', 'Nov-24', 'Dec-24']
    first_columns = [col for col in df.columns if col not in sum_columns and col != 'Name']

    df[sum_columns] = df[sum_columns].map(convert_to_numeric)
    agg_dict = {**{col: 'sum' for col in sum_columns}, **{col: 'first' for col in first_columns}}

    merged_duplicates = df.groupby(['Name'], as_index=False).agg(agg_dict)[df.columns.tolist()]
    merged_duplicates.to_csv(f"{output_directory}/final_merge.csv", index=False)
    return merged_duplicates


