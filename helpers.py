import pandas as pd
import numpy as np

# The convert_to_numeric function is used to convert a string to a numeric value.
def convert_to_numeric(value):
    if isinstance(value, str):
        cleaned_value = value.replace(',', '')
        try:
            numeric_value = pd.to_numeric(cleaned_value, errors='coerce')
            return -abs(numeric_value) if value.startswith('-') else numeric_value
        except ValueError:
            return np.nan
    return value


def update_lost_names(df):
    # A helper function to extract the base name (without the "LOST ..." part)
    def base_name(name):
        if "LOST" in name:
            return name.split(" (LOST")[0]
        return name

    # Correcting the syntax and applying the helper function conditionally
    # based on 'Unit No.' values being the same for pairs with identical base names.
    df['BaseName'] = df['Name'].apply(base_name)

    # Create a mapping from (base name, Unit No.) to the full name with "LOST ..." if it exists
    lost_mapping = {(row['BaseName'], row['Unit No.']): row['Name'] for index, row in df.iterrows() if
                    "LOST" in row['Name']}

    # Function to update the name if there's a matching base name and unit number with "LOST ..."
    def update_name(row):
        key = (row['BaseName'], row['Unit No.'])
        return lost_mapping.get(key, row['Name'])

    # Applying the update_name function to each row
    df['Name'] = df.apply(update_name, axis=1)

    # Drop the helper column as it's no longer needed
    df.drop(columns=['BaseName'], inplace=True)

    return df


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


def load_and_clean_data(path_to_csv):
    df = pd.read_csv(path_to_csv)
    df.columns = df.columns.str.strip()
    df[['Unit No.', 'Name']] = df[['Unit No.', 'Name']].fillna('Blank')
    return df
