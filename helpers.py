import pandas as pd
import numpy as np


def convert_to_numeric(value):
    if isinstance(value, str):
        cleaned_value = value.replace(',', '')
        try:
            numeric_value = pd.to_numeric(cleaned_value, errors='coerce')
            return -abs(numeric_value) if value.startswith('-') else numeric_value
        except ValueError:
            return np.nan
    return value
