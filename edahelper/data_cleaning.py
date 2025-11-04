# data_cleaning.py
import pandas as pd
from typing import Optional

def fill_missing(df: pd.DataFrame, strategy: str = "mean", columns: Optional[list] = None, inplace: bool = False):
    """
    Fill missing values.
    strategy: 'mean', 'median', 'mode', or a scalar value.
    columns: list of columns to apply to (default all).
    Returns DataFrame (modified) or None if inplace=True.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if columns is None:
        columns = df.columns.tolist()

    if strategy == "mean":
        fill_values = df[columns].mean()
    elif strategy == "median":
        fill_values = df[columns].median()
    elif strategy == "mode":
        # mode may return multiple values; take first
        fill_values = df[columns].mode().iloc[0]
    else:
        # assume user provided a scalar or dict-like
        fill_values = strategy

    result = df.fillna(fill_values) if not inplace else df.fillna(fill_values, inplace=True)
    return None if inplace else result

def drop_duplicates(df: pd.DataFrame, subset: Optional[list] = None, keep: str = "first", inplace: bool = False):
    """
    Drop duplicate rows.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    result = df.drop_duplicates(subset=subset, keep=keep, inplace=inplace)
    return None if inplace else result

def convert_dtype(df: pd.DataFrame, column: str, dtype: str, inplace: bool = False):
    """
    Convert a column to a specified dtype (e.g., 'datetime', 'int', 'float', 'category').
    Returns DataFrame (modified) or None if inplace=True.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame")

    if dtype == "datetime":
        new_col = pd.to_datetime(df[column], errors="coerce")
    else:
        new_col = df[column].astype(dtype, errors="ignore")

    if inplace:
        df[column] = new_col
        return None
    else:
        out = df.copy()
        out[column] = new_col
        return out