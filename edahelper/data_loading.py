"""
data_loading.py
Functions for importing data from various sources.
"""

import pandas as pd


def load_csv(filepath):
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(filepath)


def load_excel(filepath, sheet_name=0):
    """Load an Excel file into a pandas DataFrame."""
    return pd.read_excel(filepath, sheet_name=sheet_name)


def load_json(filepath):
    """Load a JSON file into a pandas DataFrame."""
    return pd.read_json(filepath)