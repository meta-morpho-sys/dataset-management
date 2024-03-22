import pandas as pd
import numpy as np


def convert_to_numeric(value):
    # First, check if the value is a string. If not, return the value as is.
    if isinstance(value, str):
        cleaned_value = value.replace(',', '')
        # Prepare to detect and handle negative numbers represented with parentheses
        is_negative = value.startswith('-')

        try:
            # Convert to numeric, applying negation if parentheses indicated a negative number
            numeric_value = pd.to_numeric(cleaned_value, errors='coerce')
            # numeric_value = pd.to_numeric(value)
            if is_negative:
                negative = -abs(numeric_value)
                return negative
            return numeric_value
        except ValueError:
            # In case of a ValueError during conversion, return NaN to indicate failure
            return np.nan
    else:
        # If the value is already numeric (int, float), return it as is
        return value
