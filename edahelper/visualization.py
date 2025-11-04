# visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation(df: pd.DataFrame, figsize=(8, 6), annot: bool = True):
    """
    Plot correlation heatmap for numeric columns only.
    """
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        print("No numeric columns for correlation.")
        return
    plt.figure(figsize=figsize)
    sns.heatmap(numeric_df.corr(), annot=annot)
    plt.title("Correlation Heatmap")
    plt.show()

def plot_distribution(df: pd.DataFrame, column: str, bins: int = 30, kde: bool = True):
    """
    Plot distribution (histogram + optional KDE) for a column.
    """
    if column not in df.columns:
        raise KeyError(f"{column} not found in DataFrame.")
    if not pd.api.types.is_numeric_dtype(df[column]):
        print(f"Column `{column}` is not numeric. Showing value counts instead.")
        plt.figure(figsize=(8, 4))
        df[column].value_counts().plot(kind="bar")
        plt.title(f"Value counts: {column}")
        plt.show()
        return

    plt.figure(figsize=(8, 4))
    sns.histplot(df[column].dropna(), bins=bins, kde=kde)
    plt.title(f"Distribution: {column}")
    plt.show()

def scatter(df: pd.DataFrame, x: str, y: str, hue: str = None):
    """
    Scatter plot between x and y. Optional hue for categorical separation.
    """
    if x not in df.columns or y not in df.columns:
        raise KeyError("x or y column not found in DataFrame.")
    plt.figure(figsize=(7, 5))
    if hue is None:
        sns.scatterplot(data=df, x=x, y=y)
    else:
        if hue not in df.columns:
            raise KeyError(f"hue column `{hue}` not found.")
        sns.scatterplot(data=df, x=x, y=y, hue=hue)
    plt.title(f"Scatter: {x} vs {y}")
    plt.show()