# data_overview.py
import pandas as pd

def quick_summary(df: pd.DataFrame, n: int = 5):
    """
    Print a quick overview: shape, dtypes, head, tail and top missing columns.
    Returns nothing (prints to console).
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    print("=== Quick Summary ===")
    print("Shape:", df.shape)
    print("\n--- dtypes ---")
    print(df.dtypes)
    print("\n--- Memory usage (bytes) ---")
    print(df.memory_usage(deep=True).sum())
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

def show_missing(df: pd.DataFrame, top: int = 10):
    """
    Print the columns with the largest missing value counts (top N).
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    miss = df.isnull().sum()
    miss_perc = (miss / len(df) * 100).round(2)
    miss_table = pd.DataFrame({"missing_count": miss, "missing_pct": miss_perc})
    miss_table = miss_table[miss_table["missing_count"] > 0].sort_values("missing_count", ascending=False)
    if miss_table.empty:
        print("No missing values in DataFrame.")
    else:
        print(miss_table.head(top))
    return miss_table

def numeric_overview(df: pd.DataFrame):
    """
    Return summary statistics for numeric columns (count, mean, std, min, 25%, 50%, 75%, max)
    and also show skewness and number of unique values.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    numeric = df.select_dtypes(include=["number"])
    if numeric.empty:
        print("No numeric columns found.")
        return pd.DataFrame()

    desc = numeric.describe().T
    desc["skew"] = numeric.skew()
    desc["unique"] = numeric.nunique()
    return desc