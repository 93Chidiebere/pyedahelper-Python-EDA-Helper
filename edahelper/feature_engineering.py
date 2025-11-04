# feature_engineering.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from typing import Optional

def encode_label(df: pd.DataFrame, column: str, inplace: bool = False):
    """
    Label-encode a single column. Returns modified DataFrame or None if inplace.
    """
    if column not in df.columns:
        raise KeyError(f"{column} not found in DataFrame.")
    le = LabelEncoder()
    new = le.fit_transform(df[column].astype(str))
    if inplace:
        df[column] = new
        return None
    out = df.copy()
    out[column] = new
    return out

def encode_onehot(df: pd.DataFrame, column: str, drop_original: bool = True):
    """
    One-hot encode a single column and return a new DataFrame with dummy columns.
    """
    if column not in df.columns:
        raise KeyError(f"{column} not found in DataFrame.")
    dummies = pd.get_dummies(df[column], prefix=column, dummy_na=False)
    out = pd.concat([df.reset_index(drop=True), dummies.reset_index(drop=True)], axis=1)
    if drop_original:
        out = out.drop(columns=[column])
    return out

def scale_numeric(df: pd.DataFrame, columns: Optional[list] = None, inplace: bool = False):
    """
    Standard scale numeric columns. By default scales all numeric columns.
    Returns scaled DataFrame or None if inplace.
    """
    numeric = df.select_dtypes(include=["number"]).columns.tolist() if columns is None else columns
    if not numeric:
        print("No numeric columns to scale.")
        return df.copy() if not inplace else None

    scaler = StandardScaler()
    out = df.copy()
    out[numeric] = scaler.fit_transform(out[numeric])

    if inplace:
        for col in numeric:
            df[col] = out[col]
        return None
    return out