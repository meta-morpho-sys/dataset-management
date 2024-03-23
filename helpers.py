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


from load_and_clean_data import load_and_clean_data


def update_lost_names(df):
    # A helper function to extract the base name (without the "LOST ..." part)
    def base_name(name):
        if "LOST" in name:
            print(name)
            print(name.split(" (LOST")[0])
            return name.split(" (LOST")[0]
        return name

    # Apply the helper function to create a new column for base names
    df['BaseName'] = df['Name'].apply(base_name)

    # Find names with the "LOST ..." substring and create a mapping from base name to full name
    lost_mapping = {row['BaseName']: row['Name'] for index, row in df.iterrows() if "LOST" in row['Name']}
    print("lost_mapping")
    print(lost_mapping)

    # Ensure we apply the "LOST ..." part only to names missing it but have an equivalent base name with it
    def update_name_with_lost(base_name, name):
        # If the base name has a corresponding "LOST ..." version, update accordingly
        if base_name in lost_mapping and name == base_name:
            return lost_mapping[base_name]
        return name

    df['Name'] = df.apply(lambda row: update_name_with_lost(row['BaseName'], row['Name']), axis=1)

    # Drop the helper column as it's no longer needed
    df.drop(columns=['BaseName'], inplace=True)
    return df
