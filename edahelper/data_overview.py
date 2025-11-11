# # data_overview.py
# import pandas as pd

# def quick_summary(df: pd.DataFrame, n: int = 5):
#     """
#     Print a quick overview: shape, dtypes, head, tail and top missing columns.
#     Returns nothing (prints to console).
#     """
#     if not isinstance(df, pd.DataFrame):
#         raise TypeError("df must be a pandas DataFrame")

#     print("=== Quick Summary ===")
#     print("Shape:", df.shape)
#     print("\n--- dtypes ---")
#     print(df.dtypes)
#     print("\n--- Memory usage (bytes) ---")
#     print(df.memory_usage(deep=True).sum())
#     print(f"\n--- Head (first {n} rows) ---")
#     print(df.head(n))
#     print(f"\n--- Tail (last {n} rows) ---")
#     print(df.tail(n))

#     missing = df.isnull().sum()
#     missing = missing[missing > 0].sort_values(ascending=False)
#     print("\n--- Columns with missing values ---")
#     if missing.empty:
#         print("No missing values detected.")
#     else:
#         print(missing)

# def show_missing(df: pd.DataFrame, top: int = 10):
#     """
#     Print the columns with the largest missing value counts (top N).
#     """
#     if not isinstance(df, pd.DataFrame):
#         raise TypeError("df must be a pandas DataFrame")

#     miss = df.isnull().sum()
#     miss_perc = (miss / len(df) * 100).round(2)
#     miss_table = pd.DataFrame({"missing_count": miss, "missing_pct": miss_perc})
#     miss_table = miss_table[miss_table["missing_count"] > 0].sort_values("missing_count", ascending=False)
#     if miss_table.empty:
#         print("No missing values in DataFrame.")
#     else:
#         print(miss_table.head(top))
#     return miss_table

# def numeric_overview(df: pd.DataFrame):
#     """
#     Return summary statistics for numeric columns (count, mean, std, min, 25%, 50%, 75%, max)
#     and also show skewness and number of unique values.
#     """
#     if not isinstance(df, pd.DataFrame):
#         raise TypeError("df must be a pandas DataFrame")

#     numeric = df.select_dtypes(include=["number"])
#     if numeric.empty:
#         print("No numeric columns found.")
#         return pd.DataFrame()

#     desc = numeric.describe().T
#     desc["skew"] = numeric.skew()
#     desc["unique"] = numeric.nunique()
#     return desc

# data_overview.py
import pandas as pd
import numpy as np

def quick_summary(df: pd.DataFrame, n: int = 5):
    """
    Print a concise summary of the DataFrame:
      • shape, dtypes, memory usage
      • head/tail preview
      • top missing-value columns

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.
    n : int, optional
        Number of rows to show for head/tail. Default is 5.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if df.empty:
        print("⚠️ The DataFrame is empty.")
        return

    print("=" * 50)
    print("📊 QUICK SUMMARY")
    print("=" * 50)
    print(f"Shape: {df.shape}")
    print("\n--- dtypes ---")
    print(df.dtypes.to_string())
    print("\n--- Memory usage (bytes) ---")
    print(f"{df.memory_usage(deep=True).sum():,}")

    print(f"\n--- Head (first {n} rows) ---")
    print(df.head(n))
    print(f"\n--- Tail (last {n} rows) ---")
    print(df.tail(n))

    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    print("\n--- Columns with missing values ---")
    if missing.empty:
        print("No missing values detected.")
    else:
        print(missing)
    print("=" * 50)


def show_missing(df: pd.DataFrame, top: int = 10):
    """
    Display columns with the most missing values (top N).

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.
    top : int, optional
        Number of top columns to display. Default is 10.

    Returns
    -------
    pd.DataFrame
        Missing count and percentage table.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if df.empty:
        print("⚠️ The DataFrame is empty.")
        return pd.DataFrame()

    miss = df.isnull().sum()
    miss_perc = (miss / len(df) * 100).round(2)
    miss_table = pd.DataFrame({
        "missing_count": miss,
        "missing_pct": miss_perc
    }).sort_values("missing_count", ascending=False)
    miss_table = miss_table[miss_table["missing_count"] > 0]

    if miss_table.empty:
        print("No missing values in DataFrame.")
    else:
        print("\n=== Missing Value Summary ===")
        print(miss_table.head(top).to_string())
    return miss_table


def numeric_overview(df: pd.DataFrame, round_to: int = 3):
    """
    Return summary statistics for numeric columns:
      count, mean, std, min, 25%, 50%, 75%, max, skew, unique

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.
    round_to : int, optional
        Decimal precision for numeric outputs.

    Returns
    -------
    pd.DataFrame
        Statistical overview of numeric columns.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if df.empty:
        print("⚠️ The DataFrame is empty.")
        return pd.DataFrame()

    numeric = df.select_dtypes(include=["number"])
    if numeric.empty:
        print("No numeric columns found.")
        return pd.DataFrame()

    desc = numeric.describe().T
    # handle skew errors safely
    with np.errstate(all='ignore'):
        desc["skew"] = numeric.apply(lambda x: x.skew(skipna=True))
    desc["unique"] = numeric.nunique()
    return desc.round(round_to)