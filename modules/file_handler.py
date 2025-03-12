"""
Handles CSV file uploading and validation.
"""

import pandas as pd

def load_csv(file):
    try:
        df = pd.read_csv(file.name)
        return df, None
    except Exception as e:
        return None, str(e)
