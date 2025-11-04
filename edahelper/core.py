# # # edahelper/core.py
# # """
# # Core cheat-sheet for edahelper.
# # Provides:
# #  - show()        : prints a grouped cheat-sheet of common EDA commands (pandas, numpy, seaborn, sklearn)
# #  - example(name) : prints a short code example and one-line explanation for the named command
# #  - topics()      : list available command names / groups
# #  - get_hint(key) : small offline hint engine
# # """

# # from typing import Dict, List
# # try:
# #     from rich.console import Console
# #     from rich.table import Table
# #     _HAS_RICH = True
# #     console = Console()
# # except Exception:
# #     _HAS_RICH = False
# #     console = None

# # # Curated cheat-sheet dictionary: group -> {label: snippet}
# # CHEAT_SHEET: Dict[str, Dict[str, str]] = {
# #     "Data Loading": {
# #         "Read CSV": "df = pd.read_csv('file.csv')  # load CSV into DataFrame",
# #         "Read Excel": "df = pd.read_excel('file.xlsx', sheet_name=0)",
# #         "Read Parquet": "df = pd.read_parquet('file.parquet')",
# #         "Read JSON": "df = pd.read_json('file.json')",
# #         "Read SQL": "df = pd.read_sql('SELECT * FROM table', connection)",
# #     },
# #     "Quick Overview": {
# #         "Head": "df.head()  # first 5 rows",
# #         "Tail": "df.tail()  # last 5 rows",
# #         "Info": "df.info()  # dtypes and non-null counts",
# #         "Describe": "df.describe()  # summary statistics",
# #         "Shape": "df.shape  # (rows, cols)",
# #         "Columns": "df.columns  # list column names",
# #         "Sample": "df.sample(5)  # random rows",
# #     },
# #     "Missing Values & Dtypes": {
# #         "Missing count": "df.isnull().sum()",
# #         "Missing percent": "(df.isnull().mean() * 100).round(2)",
# #         "Drop NA": "df.dropna()",
# #         "Fill NA": "df.fillna(value)",
# #         "Change dtype": "df['col'] = df['col'].astype('int')",
# #         "To datetime": "df['date'] = pd.to_datetime(df['date'])",
# #     },
# #     "Indexing & Selection": {
# #         "Select column": "df['col']",
# #         "Select rows": "df.loc[0] / df.iloc[0]",
# #         "Filter rows": "df[df['col'] > 10]",
# #         "Assign column": "df['new'] = df['a'] + df['b']",
# #     },
# #     "Aggregation & Grouping": {
# #         "Group + agg": "df.groupby('col').agg({'val': ['mean', 'sum']})",
# #         "Pivot table": "pd.pivot_table(df, index='col', values='val', aggfunc='mean')",
# #     },
# #     "Visualization (quick snippets)": {
# #         "Histogram": "df['col'].hist()  # matplotlib",
# #         "Seaborn countplot": "sns.countplot(x='col', data=df)",
# #         "Seaborn boxplot": "sns.boxplot(x='col', y='val', data=df)",
# #         "Scatter": "sns.scatterplot(data=df, x='a', y='b')",
# #         "Correlation heatmap": "sns.heatmap(df.select_dtypes('number').corr(), annot=True)",
# #     },
# #     "Feature Engineering (quick)": {
# #         "One-hot encode": "pd.get_dummies(df['cat'], prefix='cat')",
# #         "Label encode": "from sklearn.preprocessing import LabelEncoder",
# #         "Fill numeric with median": "df['num'] = df['num'].fillna(df['num'].median())",
# #         "Scale numeric": "from sklearn.preprocessing import StandardScaler",
# #     },
# #     "Quick NumPy & sklearn": {
# #         "NumPy array": "arr = df['col'].to_numpy()",
# #         "Train/test split": "from sklearn.model_selection import train_test_split",
# #     }
# # }

# # # Small builtin hints
# # _HINTS = {
# #     "describe": "After df.describe(), check df.isnull().sum() and df.dtypes.",
# #     "info": "Use df.memory_usage(deep=True) if DataFrame uses a lot of RAM.",
# #     "groupby": "Remember to reset_index() after aggregations if you want back a flat DF.",
# # }


# # def show():
# #     """Print the whole cheat-sheet in a readable form."""
# #     if _HAS_RICH:
# #         console.print("[bold magenta]EDA Helper — Cheat Sheet[/bold magenta]\n")
# #         for group, items in CHEAT_SHEET.items():
# #             table = Table(title=group, show_lines=False)
# #             table.add_column("Command / Concept", style="bold")
# #             table.add_column("Example / Syntax")
# #             for k, v in items.items():
# #                 table.add_row(k, v)
# #             console.print(table)
# #     else:
# #         print("EDA Helper — Cheat Sheet\n")
# #         for group, items in CHEAT_SHEET.items():
# #             print(f"== {group} ==")
# #             for k, v in items.items():
# #                 print(f"- {k}: {v}")
# #             print()


# # def example(name: str):
# #     """Show the snippet for a given command name (case-insensitive partial match)."""
# #     name_lower = name.strip().lower()
# #     matches = []
# #     for group, items in CHEAT_SHEET.items():
# #         for k, v in items.items():
# #             if name_lower in k.lower():
# #                 matches.append((group, k, v))
# #     if not matches:
# #         out = f"No example found for '{name}'. Try `eda.topics()` to view available commands."
# #         if _HAS_RICH:
# #             console.print(f"[red]{out}[/red]")
# #         else:
# #             print(out)
# #         return
# #     # print matches
# #     if _HAS_RICH:
# #         for group, k, v in matches:
# #             console.print(f"[cyan]{group}[/cyan] — [bold]{k}[/bold]\n  [green]{v}[/green]\n")
# #     else:
# #         for group, k, v in matches:
# #             print(f"{group} - {k}:\n    {v}\n")


# # def topics() -> List[str]:
# #     """Return a flat list of command names available in the cheat sheet."""
# #     names = []
# #     for items in CHEAT_SHEET.values():
# #         names.extend(list(items.keys()))
# #     return names


# # def get_hint(key: str):
# #     """Return a short offline hint for a key (case-insensitive)."""
# #     return _HINTS.get(key.lower(), None)

# # edahelper/core.py
# """
# Core cheat-sheet for edahelper.
# Provides:
#  - show()        : prints a grouped cheat-sheet of common EDA commands (pandas, numpy, seaborn, sklearn)
#  - example(name) : prints a short code example and one-line explanation for the named command
#  - topics()      : list available command names / groups
#  - get_hint(key) : small offline hint engine
# """

# from typing import Dict, List
# try:
#     from rich.console import Console
#     from rich.table import Table
#     _HAS_RICH = True
#     console = Console()
# except Exception:
#     _HAS_RICH = False
#     console = None


# # Curated cheat-sheet dictionary: group -> {label: {"syntax": str, "desc": str}}
# CHEAT_SHEET: Dict[str, Dict[str, Dict[str, str]]] = {
#     "Data Loading": {
#         "Read CSV": {
#             "syntax": "df = pd.read_csv('file.csv')",
#             "desc": "Loads a CSV file into a pandas DataFrame."
#         },
#         "Read Excel": {
#             "syntax": "df = pd.read_excel('file.xlsx', sheet_name=0)",
#             "desc": "Reads an Excel file into a pandas DataFrame."
#         },
#         "Read Parquet": {
#             "syntax": "df = pd.read_parquet('file.parquet')",
#             "desc": "Loads a Parquet file, often used for big data."
#         },
#         "Read JSON": {
#             "syntax": "df = pd.read_json('file.json')",
#             "desc": "Reads a JSON file into a pandas DataFrame."
#         },
#         "Read SQL": {
#             "syntax": "df = pd.read_sql('SELECT * FROM table', connection)",
#             "desc": "Reads data directly from a SQL database."
#         },
#     },

#     "Quick Overview": {
#         "Head": {"syntax": "df.head()", "desc": "Displays the first 5 rows of the dataset."},
#         "Tail": {"syntax": "df.tail()", "desc": "Displays the last 5 rows of the dataset."},
#         "Info": {"syntax": "df.info()", "desc": "Shows column names, data types, and null counts."},
#         "Describe": {"syntax": "df.describe()", "desc": "Displays summary statistics for numeric columns."},
#         "Shape": {"syntax": "df.shape", "desc": "Returns (rows, columns) of the dataset."},
#         "Columns": {"syntax": "df.columns", "desc": "Lists all column names."},
#         "Sample": {"syntax": "df.sample(5)", "desc": "Randomly samples rows from the dataset."},
#     },

#     "Missing Values & Dtypes": {
#         "Missing count": {"syntax": "df.isnull().sum()", "desc": "Counts missing values per column."},
#         "Missing percent": {"syntax": "(df.isnull().mean() * 100).round(2)", "desc": "Percentage of missing values per column."},
#         "Drop NA": {"syntax": "df.dropna()", "desc": "Removes rows with missing values."},
#         "Fill NA": {"syntax": "df.fillna(value)", "desc": "Fills missing values with specified value or method."},
#         "Change dtype": {"syntax": "df['col'] = df['col'].astype('int')", "desc": "Converts a column to another data type."},
#         "To datetime": {"syntax": "df['date'] = pd.to_datetime(df['date'])", "desc": "Converts text dates into datetime format."},
#     },

#     "Indexing & Selection": {
#         "Select column": {"syntax": "df['col']", "desc": "Selects a single column."},
#         "Select rows": {"syntax": "df.loc[0] / df.iloc[0]", "desc": "Selects rows by label or index."},
#         "Filter rows": {"syntax": "df[df['col'] > 10]", "desc": "Filters rows based on condition."},
#         "Assign column": {"syntax": "df['new'] = df['a'] + df['b']", "desc": "Creates or overwrites a column."},
#     },

#     "Aggregation & Grouping": {
#         "Group + agg": {"syntax": "df.groupby('col').agg({'val': ['mean', 'sum']})", "desc": "Aggregates data using groupby operations."},
#         "Pivot table": {"syntax": "pd.pivot_table(df, index='col', values='val', aggfunc='mean')", "desc": "Summarizes data into pivot tables."},
#     },

#     "Visualization (quick snippets)": {
#         "Histogram": {"syntax": "df['col'].hist()", "desc": "Plots a histogram using matplotlib."},
#         "Seaborn countplot": {"syntax": "sns.countplot(x='col', data=df)", "desc": "Shows count distribution of categorical column."},
#         "Seaborn boxplot": {"syntax": "sns.boxplot(x='col', y='val', data=df)", "desc": "Shows spread and outliers of data."},
#         "Scatter": {"syntax": "sns.scatterplot(data=df, x='a', y='b')", "desc": "Visualizes relationship between two variables."},
#         "Correlation heatmap": {"syntax": "sns.heatmap(df.select_dtypes('number').corr(), annot=True)", "desc": "Displays correlation between numeric features."},
#     },

#     "Feature Engineering (quick)": {
#         "One-hot encode": {"syntax": "pd.get_dummies(df['cat'], prefix='cat')", "desc": "Converts categorical variables to numeric dummy columns."},
#         "Label encode": {"syntax": "from sklearn.preprocessing import LabelEncoder", "desc": "Assigns integer labels to categorical values."},
#         "Fill numeric with median": {"syntax": "df['num'] = df['num'].fillna(df['num'].median())", "desc": "Replaces missing numeric values with median."},
#         "Scale numeric": {"syntax": "from sklearn.preprocessing import StandardScaler", "desc": "Standardizes features by removing mean and scaling to unit variance."},
#     },

#     "Quick NumPy & sklearn": {
#         "NumPy array": {"syntax": "arr = df['col'].to_numpy()", "desc": "Converts a pandas Series to NumPy array."},
#         "Train/test split": {"syntax": "from sklearn.model_selection import train_test_split", "desc": "Splits dataset into training and testing sets."},
#     }
# }


# _HINTS = {
#     "describe": "After df.describe(), check df.isnull().sum() and df.dtypes.",
#     "info": "Use df.memory_usage(deep=True) if DataFrame uses a lot of RAM.",
#     "groupby": "Remember to reset_index() after aggregations if you want back a flat DF.",
# }


# def show():
#     """Print the whole cheat-sheet in a readable table with descriptions."""
#     if _HAS_RICH:
#         console.print("[bold magenta]EDA Helper — Cheat Sheet[/bold magenta]\n")
#         for group, items in CHEAT_SHEET.items():
#             table = Table(title=group, show_lines=False)
#             table.add_column("Command / Concept", style="bold cyan")
#             table.add_column("Example / Syntax", style="green")
#             table.add_column("Description", style="white")
#             for k, v in items.items():
#                 table.add_row(k, v["syntax"], v["desc"])
#             console.print(table)
#     else:
#         print("EDA Helper — Cheat Sheet\n")
#         for group, items in CHEAT_SHEET.items():
#             print(f"== {group} ==")
#             for k, v in items.items():
#                 print(f"- {k}: {v['syntax']} — {v['desc']}")
#             print()


# def example(name: str):
#     """Show a single command’s syntax and description (case-insensitive)."""
#     name_lower = name.strip().lower()
#     matches = []
#     for group, items in CHEAT_SHEET.items():
#         for k, v in items.items():
#             if name_lower in k.lower():
#                 matches.append((group, k, v))
#     if not matches:
#         out = f"No example found for '{name}'. Try `eda.topics()` to view available commands."
#         if _HAS_RICH:
#             console.print(f"[red]{out}[/red]")
#         else:
#             print(out)
#         return
#     for group, k, v in matches:
#         if _HAS_RICH:
#             console.print(f"[cyan]{group}[/cyan] — [bold]{k}[/bold]\n  [green]{v['syntax']}[/green]\n  [dim]{v['desc']}[/dim]\n")
#         else:
#             print(f"{group} - {k}:\n  {v['syntax']}\n  {v['desc']}\n")


# def topics() -> List[str]:
#     """Return a flat list of command names available in the cheat sheet."""
#     return [k for items in CHEAT_SHEET.values() for k in items.keys()]


# def get_hint(key: str):
#     """Return a short offline hint for a key (case-insensitive)."""
#     return _HINTS.get(key.lower(), None)

# edahelper/core.py
"""
Core cheat-sheet for edahelper.
Provides:
 - show()        : prints a grouped cheat-sheet of common EDA commands (pandas, numpy, seaborn, sklearn)
 - example(name) : prints a short code example and one-line explanation for the named command
 - topics()      : list available command names / groups
 - get_hint(key) : small offline hint engine
"""

from typing import Dict, List
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.markdown import Markdown
    _HAS_RICH = True
    console = Console()
except Exception:
    _HAS_RICH = False
    console = None


# 🧠 Each command has: {label: {"code": "...", "desc": "..."}}
CHEAT_SHEET: Dict[str, Dict[str, Dict[str, str]]] = {
    "Data Loading": {
        "Read CSV": {
            "code": "df = pd.read_csv('file.csv')",
            "desc": "Loads a CSV file into a pandas DataFrame."
        },
        "Read Excel": {
            "code": "df = pd.read_excel('file.xlsx', sheet_name=0)",
            "desc": "Reads Excel files with optional sheet selection."
        },
        "Read Parquet": {
            "code": "df = pd.read_parquet('file.parquet')",
            "desc": "Loads columnar data stored in Parquet format."
        },
        "Read JSON": {
            "code": "df = pd.read_json('file.json')",
            "desc": "Reads JSON data into a DataFrame."
        },
        "Read SQL": {
            "code": "df = pd.read_sql('SELECT * FROM table', connection)",
            "desc": "Runs SQL query and loads the result into a DataFrame."
        },
    },

    "Quick Overview": {
        "Head": {"code": "df.head()", "desc": "Shows first 5 rows of your dataset."},
        "Tail": {"code": "df.tail()", "desc": "Shows last 5 rows of your dataset."},
        "Info": {"code": "df.info()", "desc": "Displays data types and missing values count."},
        "Describe": {"code": "df.describe()", "desc": "Generates summary statistics for numeric columns."},
        "Shape": {"code": "df.shape", "desc": "Shows total number of rows and columns."},
        "Columns": {"code": "df.columns", "desc": "Lists all column names in the DataFrame."},
        "Sample": {"code": "df.sample(5)", "desc": "Randomly displays 5 rows."},
    },

    "Missing Values & Dtypes": {
        "Missing count": {"code": "df.isnull().sum()", "desc": "Counts missing values per column."},
        "Missing percent": {"code": "(df.isnull().mean() * 100).round(2)", "desc": "Calculates percentage of missing values per column."},
        "Drop NA": {"code": "df.dropna()", "desc": "Removes rows with missing values."},
        "Fill NA": {"code": "df.fillna(value)", "desc": "Fills missing values with a given constant or method."},
        "Change dtype": {"code": "df['col'] = df['col'].astype('int')", "desc": "Converts column data type."},
        "To datetime": {"code": "df['date'] = pd.to_datetime(df['date'])", "desc": "Converts a column to datetime format."},
    },

    "Indexing & Selection": {
        "Select column": {"code": "df['col']", "desc": "Selects a single column from the DataFrame."},
        "Select rows": {"code": "df.loc[0] / df.iloc[0]", "desc": "Selects a row by label or integer position."},
        "Filter rows": {"code": "df[df['col'] > 10]", "desc": "Filters rows based on condition."},
        "Assign column": {"code": "df['new'] = df['a'] + df['b']", "desc": "Creates a new column based on existing ones."},
    },

    "Aggregation & Grouping": {
        "Group + agg": {"code": "df.groupby('col').agg({'val': ['mean', 'sum']})", "desc": "Groups data and applies multiple aggregations."},
        "Pivot table": {"code": "pd.pivot_table(df, index='col', values='val', aggfunc='mean')", "desc": "Creates pivot summary tables from data."},
    },

    "Visualization (quick snippets)": {
        "Histogram": {"code": "df['col'].hist()", "desc": "Plots frequency of a numeric column."},
        "Seaborn countplot": {"code": "sns.countplot(x='col', data=df)", "desc": "Shows counts of categorical values."},
        "Seaborn boxplot": {"code": "sns.boxplot(x='col', y='val', data=df)", "desc": "Visualizes data distribution and outliers."},
        "Scatter": {"code": "sns.scatterplot(data=df, x='a', y='b')", "desc": "Plots relationship between two numeric columns."},
        "Correlation heatmap": {"code": "sns.heatmap(df.select_dtypes('number').corr(), annot=True)", "desc": "Displays correlation among numeric features."},
    },

    "Feature Engineering (quick)": {
        "One-hot encode": {"code": "pd.get_dummies(df['cat'], prefix='cat')", "desc": "Converts categorical data to binary columns."},
        "Label encode": {"code": "from sklearn.preprocessing import LabelEncoder", "desc": "Encodes categorical values into numeric labels."},
        "Fill numeric with median": {"code": "df['num'] = df['num'].fillna(df['num'].median())", "desc": "Replaces missing numeric values with median."},
        "Scale numeric": {"code": "from sklearn.preprocessing import StandardScaler", "desc": "Standardizes numerical features for ML."},
    },

    "Quick NumPy & sklearn": {
        "NumPy array": {"code": "arr = df['col'].to_numpy()", "desc": "Converts a pandas column into a NumPy array."},
        "Train/test split": {"code": "from sklearn.model_selection import train_test_split", "desc": "Splits dataset into training and testing sets."},
    }
}


_HINTS = {
    "describe": "After df.describe(), check df.isnull().sum() and df.dtypes.",
    "info": "Use df.memory_usage(deep=True) if DataFrame uses a lot of RAM.",
    "groupby": "Remember to reset_index() after aggregations if you want back a flat DF.",
}


def show():
    """Display the entire EDA cheat-sheet neatly."""
    if _HAS_RICH:
        console.print("[bold magenta]✨ EDA Helper — Interactive Cheat Sheet ✨[/bold magenta]\n")
        for group, items in CHEAT_SHEET.items():
            md_text = ""
            for k, v in items.items():
                md_text += f"**{k}** — {v['desc']}\n\n```python\n{v['code']}\n```\n\n"
            # ✅ Safe for all rich versions
            try:
                panel = Panel.fit(Markdown(md_text), title=f"[bold cyan]{group}[/bold cyan]", expand=False)
            except TypeError:
                panel = Panel.fit(Markdown(md_text), title=f"[bold cyan]{group}[/bold cyan]")
            console.print(panel)
    else:
        print("EDA Helper — Cheat Sheet\n")
        for group, items in CHEAT_SHEET.items():
            print(f"== {group} ==")
            for k, v in items.items():
                print(f"- {k}: {v['code']}  # {v['desc']}")
            print()


def example(name: str):
    """Show the snippet for a given command name (case-insensitive partial match)."""
    name_lower = name.strip().lower()
    matches = []
    for group, items in CHEAT_SHEET.items():
        for k, v in items.items():
            if name_lower in k.lower():
                matches.append((group, k, v))
    if not matches:
        out = f"No example found for '{name}'. Try `eda.topics()` to view available commands."
        if _HAS_RICH:
            console.print(f"[red]{out}[/red]")
        else:
            print(out)
        return
    if _HAS_RICH:
        for group, k, v in matches:
            console.print(Panel.fit(f"[bold]{k}[/bold] — {v['desc']}\n\n[green]{v['code']}[/green]",
                                    title=f"[cyan]{group}[/cyan]", expand=False))
    else:
        for group, k, v in matches:
            print(f"{group} - {k}: {v['code']}  # {v['desc']}")


def topics() -> List[str]:
    """Return a flat list of command names available in the cheat sheet."""
    names = []
    for items in CHEAT_SHEET.values():
        names.extend(list(items.keys()))
    return names


def get_hint(key: str):
    """Return a short offline hint for a key (case-insensitive)."""
    return _HINTS.get(key.lower(), None)