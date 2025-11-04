"""
stats_summary.py
Functions for summarizing datasets statistically.
"""

import pandas as pd


def summary(df):
    """Return general statistical summary (describe)."""
    return df.describe()


def missing_values(df):
    """Return count of missing values per column."""
    return df.isna().sum()


def data_shape(df):
    """Return the number of rows and columns."""
    return df.shape


def unique_counts(df):
    """Return the number of unique values in each column."""
    return df.nunique()