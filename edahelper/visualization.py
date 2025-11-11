import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Tuple

def plot_correlation(df: pd.DataFrame, figsize: Tuple[int, int] = (8, 6), annot: bool = True, cmap: str = "coolwarm"):
    """
    Plot correlation heatmap for numeric columns only.

    Parameters:
        df (pd.DataFrame): The DataFrame to analyze.
        figsize (tuple): Size of the heatmap figure.
        annot (bool): Whether to annotate the heatmap with correlation values.
        cmap (str): Colormap for the heatmap.

    Raises:
        TypeError: If df is not a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        print("No numeric columns available for correlation heatmap.")
        return

    corr = numeric_df.corr()
    if corr.isnull().all().all():
        print("Correlation matrix contains only NaN values. Nothing to plot.")
        return

    plt.figure(figsize=figsize)
    sns.heatmap(corr, annot=annot, cmap=cmap, fmt=".2f", square=True)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()


def plot_distribution(df: pd.DataFrame, column: str, bins: int = 30, kde: bool = True):
    """
    Plot distribution (histogram + optional KDE) for a column.

    Parameters:
        df (pd.DataFrame): The DataFrame.
        column (str): Column name to plot.
        bins (int): Number of histogram bins.
        kde (bool): Whether to include kernel density estimate.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if column not in df.columns:
        raise KeyError(f"Column `{column}` not found in DataFrame.")

    plt.figure(figsize=(8, 4))

    # Numeric column → histogram
    if pd.api.types.is_numeric_dtype(df[column]):
        sns.histplot(df[column].dropna(), bins=bins, kde=kde)
        plt.title(f"Distribution: {column}")
    else:
        # Non-numeric → bar chart of value counts
        value_counts = df[column].value_counts().head(20)  # limit to top 20 for readability
        sns.barplot(x=value_counts.index, y=value_counts.values)
        plt.xticks(rotation=45, ha="right")
        plt.title(f"Value counts (top 20): {column}")

    plt.tight_layout()
    plt.show()


def scatter(df: pd.DataFrame, x: str, y: str, hue: Optional[str] = None, alpha: float = 0.7):
    """
    Scatter plot between two columns, with optional hue for categorical separation.

    Parameters:
        df (pd.DataFrame): The DataFrame.
        x (str): Column for x-axis.
        y (str): Column for y-axis.
        hue (str, optional): Column for color grouping.
        alpha (float): Transparency of points (0–1).

    Raises:
        KeyError: If x or y (or hue, if given) are not found in DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    for col in [x, y]:
        if col not in df.columns:
            raise KeyError(f"Column `{col}` not found in DataFrame.")
    if hue and hue not in df.columns:
        raise KeyError(f"hue column `{hue}` not found in DataFrame.")

    plt.figure(figsize=(7, 5))
    sns.scatterplot(data=df, x=x, y=y, hue=hue, alpha=alpha)
    plt.title(f"Scatter: {x} vs {y}" + (f" by {hue}" if hue else ""))
    plt.tight_layout()
    plt.show()
    
def plot_two_columns(df, col1: str, col2: str, figsize=(8,5), max_cat_levels:int=30):
    """
    Adaptive two-column plotting:
      - numeric vs numeric  -> scatterplot (with optional regression line)
      - categorical vs numeric -> boxplot (category on x, numeric on y)
      - categorical vs categorical -> heatmap of counts (crosstab)

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.
    col1, col2 : str
        Column names to plot.
    figsize : tuple
        Figure size.
    max_cat_levels : int
        Maximum distinct levels for categorical plotting. If category has more levels,
        the function will plot the top `max_cat_levels` by frequency.
    """
   
    from pandas.api.types import is_numeric_dtype, is_string_dtype, is_categorical_dtype

    # validation
    if not hasattr(df, "columns"):
        raise TypeError("df must be a pandas DataFrame-like object")
    if col1 not in df.columns or col2 not in df.columns:
        missing = [c for c in (col1, col2) if c not in df.columns]
        raise KeyError(f"Column(s) not found in DataFrame: {missing}")

    # copy relevant data and drop rows where both are NaN (keep rows where at least one present)
    data = df[[col1, col2]].copy()
    data = data.dropna(how="all").reset_index(drop=True)
    if data.empty:
        print("No data available to plot after dropping all-NaN rows.")
        return

    col1_num = is_numeric_dtype(data[col1])
    col2_num = is_numeric_dtype(data[col2])

    plt.figure(figsize=figsize)

    # numeric vs numeric -> scatter + optional small jitter for identical points
    if col1_num and col2_num:
        sns.scatterplot(data=data, x=col1, y=col2)
        # add lightweight regression line if >= 3 points
        if len(data.dropna()) >= 3:
            try:
                sns.regplot(data=data, x=col1, y=col2, scatter=False, truncate=True, color="grey", line_kws={"alpha":0.6})
            except Exception:
                pass
        plt.title(f"Scatter: {col1} vs {col2}")
        plt.tight_layout()
        plt.show()
        return

    # one numeric, one categorical -> boxplot (category on x)
    if col1_num != col2_num:
        # identify numeric and categorical columns
        num_col = col1 if col1_num else col2
        cat_col = col2 if col1_num else col1

        # prepare category: limit to top levels for readability
        data[cat_col] = data[cat_col].astype("string").fillna("<NA>")
        top_levels = data[cat_col].value_counts().nlargest(max_cat_levels).index.tolist()
        if data[cat_col].nunique() > max_cat_levels:
            data = data[data[cat_col].isin(top_levels)].copy()
            print(f"Note: {cat_col} had many levels — plotting top {max_cat_levels} by frequency.")

        # if numeric column is all NaN after selecting, abort
        if data[num_col].dropna().empty:
            print(f"No numeric values found in `{num_col}` after filtering; nothing to plot.")
            return

        sns.boxplot(data=data, x=cat_col, y=num_col)
        plt.xticks(rotation=45, ha="right")
        plt.title(f"Boxplot: {num_col} by {cat_col}")
        plt.tight_layout()
        plt.show()
        return

    # categorical vs categorical -> heatmap of counts
    # convert to string categories and limit levels
    data[col1] = data[col1].astype("string").fillna("<NA>")
    data[col2] = data[col2].astype("string").fillna("<NA>")
    top1 = data[col1].value_counts().nlargest(max_cat_levels).index.tolist()
    top2 = data[col2].value_counts().nlargest(max_cat_levels).index.tolist()
    if data[col1].nunique() > max_cat_levels or data[col2].nunique() > max_cat_levels:
        data = data[data[col1].isin(top1) & data[col2].isin(top2)].copy()
        print(f"Note: One or both categorical columns had many levels — plotting top {max_cat_levels} levels for each.")

    ct = pd.crosstab(data[col1], data[col2])
    if ct.empty:
        print("No counts available to plot.")
        return

    # normalize option could be added; for now show raw counts with annotation
    plt.figure(figsize=figsize)
    sns.heatmap(ct, annot=True, fmt="d", cmap="Blues", cbar=True)
    plt.title(f"Counts heatmap: {col1} vs {col2}")
    plt.tight_layout()
    plt.show()