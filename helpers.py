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


def update_lost_names(path_to_csv, output_directory):
    path_to_output_file = f"{output_directory}/normalised_names.csv"
    df = load_and_clean_data(path_to_csv)
    # A helper function to extract the base name (without the "LOST ..." part)
    def base_name(name):
        if "LOST" in name:
            return name.split(" LOST")[0]
        return name

    # Apply the helper function to create a new column for base names
    df['BaseName'] = df['Name'].apply(base_name)

    # Find names with the "LOST ..." substring and create a mapping from base name to full name
    lost_mapping = {row['BaseName']: row['Name'] for index, row in df.iterrows() if "LOST" in row['Name']}
    print("lost_mapping")
    print(lost_mapping)

    # Update the 'Name' column based on the mapping
    df['Name'] = df['BaseName'].apply(lambda bn: lost_mapping.get(bn, bn))

    # Drop the helper column as it's no longer needed
    df.drop(columns=['BaseName'], inplace=True)
    df.to_csv(path_to_output_file, index=False)
    return df

# write a function which will compare identical names in the values of 'Name' column,
# will look for a substring (LOST ...) in the values
# and will add the substring to the value of where it doesn't exist.
# Example: 'Kings Gardens LOST 123' and 'Kings Gardens'
# should be converted to
# 'Kings Gardens LOST 123' and 'Kings Gardens LOST 123' respectively.
# The function should return a DataFrame with the updated values.