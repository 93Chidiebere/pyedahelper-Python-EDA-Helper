# feature_engineering.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from typing import Optional, List

def encode_label(df: pd.DataFrame, column: str, inplace: bool = False):
    """
    Label-encode a single categorical column.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.
    column : str
        The column to encode.
    inplace : bool, optional
        If True, modify DataFrame in place. Default is False.

    Returns
    -------
    pd.DataFrame or None
        Encoded DataFrame if inplace=False, else None.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty.")
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame.")

    # Apply LabelEncoder safely
    le = LabelEncoder()
    try:
        encoded = le.fit_transform(df[column].astype(str))
    except Exception as e:
        raise ValueError(f"Error encoding column '{column}': {e}")

    if inplace:
        df[column] = encoded
        return None

    out = df.copy()
    out[column] = encoded
    return out


def encode_onehot(df: pd.DataFrame, column: str, drop_original: bool = True):
    """
    One-hot encode a single categorical column.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.
    column : str
        The column to one-hot encode.
    drop_original : bool, optional
        Drop the original column after encoding. Default is True.

    Returns
    -------
    pd.DataFrame
        New DataFrame with one-hot encoded columns added.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty.")
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame.")

    dummies = pd.get_dummies(df[column], prefix=column, dummy_na=False)
    out = pd.concat([df.reset_index(drop=True), dummies.reset_index(drop=True)], axis=1)

    if drop_original:
        out.drop(columns=[column], inplace=True)
    return out


def scale_numeric(df: pd.DataFrame, columns: Optional[List[str]] = None, inplace: bool = False):
    """
    Standardize numeric columns using z-score scaling.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.
    columns : list, optional
        Specific columns to scale. If None, all numeric columns are scaled.
    inplace : bool, optional
        If True, modifies the DataFrame directly. Default is False.

    Returns
    -------
    pd.DataFrame or None
        Scaled DataFrame if inplace=False, else None.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty.")

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if columns is not None:
        # Verify selected columns exist and are numeric
        invalid = [col for col in columns if col not in numeric_cols]
        if invalid:
            raise ValueError(f"Columns not numeric or not found: {invalid}")
        numeric_cols = columns

    if not numeric_cols:
        print("⚠️ No numeric columns to scale.")
        return df.copy() if not inplace else None

    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(df[numeric_cols])
    out = df.copy()
    out[numeric_cols] = scaled_values

    if inplace:
        for col in numeric_cols:
            df[col] = out[col]
        return None
    return out