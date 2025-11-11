# data_cleaning.py
import pandas as pd
from typing import Optional

def fill_missing(df: pd.DataFrame, strategy: str = "mean", columns: Optional[list] = None, inplace: bool = False):
    """
    Fill missing values in the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame.
    strategy : str or scalar, default 'mean'
        Strategy to use for filling missing values. Options:
        'mean', 'median', 'mode', 'zero', 'ffill', 'bfill',
        or a scalar value (e.g. 0, "Unknown").
    columns : list, optional
        List of columns to apply the fill to. If None:
        - numeric columns are auto-selected for 'mean'/'median'
        - all columns are used for other strategies.
    inplace : bool, default False
        If True, modifies the original DataFrame in place.

    Returns
    -------
    pd.DataFrame or None
        Returns modified DataFrame if inplace=False, otherwise None.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    # Auto-select columns intelligently
    if columns is None:
        if strategy in ["mean", "median"]:
            columns = df.select_dtypes(include=["number"]).columns.tolist()
        else:
            columns = df.columns.tolist()

    # Determine fill values
    if strategy == "mean":
        fill_values = df[columns].mean()
    elif strategy == "median":
        fill_values = df[columns].median()
    elif strategy == "mode":
        fill_values = df[columns].mode().iloc[0]
    elif strategy == "zero":
        fill_values = {col: 0 for col in columns}
    elif strategy in ["ffill", "bfill"]:
        if inplace:
            df[columns].fillna(method=strategy, inplace=True) # type: ignore
            return None
        else:
            return df[columns].fillna(method=strategy) # type: ignore
    else:
        # scalar or dict provided directly
        fill_values = strategy

    if inplace:
        df[columns] = df[columns].fillna(fill_values)
        return None
    else:
        result = df.copy()
        result[columns] = result[columns].fillna(fill_values)
        return result




def drop_duplicates(df: pd.DataFrame, subset: Optional[list] = None, keep: str = "first", inplace: bool = False):
    """
    Drop duplicate rows.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    result = df.drop_duplicates(subset=subset, keep=keep, inplace=inplace) # type: ignore
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
        new_col = df[column].astype(dtype, errors="ignore") # type: ignore

    if inplace:
        df[column] = new_col
        return None
    else:
        out = df.copy()
        out[column] = new_col
        return out