# """
# stats_summary.py
# Functions for summarizing datasets statistically.
# """

# import pandas as pd


# def summary(df):
#     """Return general statistical summary (describe)."""
#     return df.describe()


# def missing_values(df):
#     """Return count of missing values per column."""
#     return df.isna().sum()


# def data_shape(df):
#     """Return the number of rows and columns."""
#     return df.shape


# def unique_counts(df):
#     """Return the number of unique values in each column."""
#     return df.nunique()

"""
stats_summary.py
Functions for summarizing datasets statistically.
"""

import pandas as pd
from typing import Tuple


def summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return general statistical summary for numeric columns.

    Parameters:
        df (pd.DataFrame): The DataFrame to summarize.

    Returns:
        pd.DataFrame: Summary statistics (count, mean, std, min, 25%, 50%, 75%, max).

    Raises:
        TypeError: If df is not a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    if df.empty:
        print("DataFrame is empty. No summary to display.")
        return pd.DataFrame()

    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        print("No numeric columns found. Returning empty summary.")
        return pd.DataFrame()

    return numeric_df.describe().T


def missing_values(df: pd.DataFrame) -> pd.Series:
    """
    Return count of missing values per column.

    Parameters:
        df (pd.DataFrame): The DataFrame to check.

    Returns:
        pd.Series: Missing values per column (0 if none).
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    return df.isna().sum().sort_values(ascending=False)


def data_shape(df: pd.DataFrame) -> Tuple[int, int]:
    """
    Return the number of rows and columns in the DataFrame.

    Parameters:
        df (pd.DataFrame): The DataFrame to inspect.

    Returns:
        tuple: (rows, columns)
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    return df.shape


def unique_counts(df: pd.DataFrame) -> pd.Series:
    """
    Return the number of unique values in each column.

    Parameters:
        df (pd.DataFrame): The DataFrame to analyze.

    Returns:
        pd.Series: Number of unique values per column.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    if df.empty:
        print("DataFrame is empty. Returning empty Series.")
        return pd.Series(dtype=int)

    return df.nunique().sort_values(ascending=False)