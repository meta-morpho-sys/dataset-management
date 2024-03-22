from load_and_clean_data import load_and_clean_data


def find_anomalies(df):
    empty_unit_names = df[df['Unit No.'] == 'Blank']['Name'].unique()
    filtered_rows = df[df['Name'].isin(empty_unit_names)]
    duplicates_or_empty_unit_no = filtered_rows.duplicated(subset=['Name'], keep=False) | (filtered_rows['Unit No.'] == '')
    return filtered_rows[duplicates_or_empty_unit_no]


def output_anomalies(df, path_to_output_file):
    df.to_csv(path_to_output_file, index=False)


def visualise_anomalies(path_to_csv, output_directory):
    path_to_output_file = f"{output_directory}/names_with_blank_numbers.csv"
    df = load_and_clean_data(path_to_csv)
    anomalies = find_anomalies(df)
    output_anomalies(anomalies, path_to_output_file)