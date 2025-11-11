# 🧠 pyedahelper - Simplify Your Exploratory Data Analysis (EDA)

**pyedahelper** is an educational and practical Python library designed to make **Exploratory Data Analysis (EDA)** simple, guided, and fast, especially for **data analysts, students, and early-career data scientists** who want to spend more time analyzing data and less time remembering syntax.

It's a lightweight, educational, and intelligent Python library that helps you perform Exploratory Data Analysis (EDA) faster — with guided suggestions, ready-to-use utilities, and clean visualizations.


🌟 Key Features:
- ⚡ A **smart EDA cheat sheet** (interactive and collapsible),
- 💬 AI-guided EDA assistant — suggests the next logical step (e.g., “View top rows with df.head()”).
- 🧩 A suite of **data tools** for real-world EDA tasks (loading, cleaning, feature engineering, visualization, and summaries),
- 💬 Handy **code hints and examples** you can copy directly into your notebook.



## 🌍 Why pyedahelper?

Performing EDA often involves the use of numerous syntaxes to understand the dataset, it forces the narrative that good data professionals are those who know all the *Python syntaxes* by heart rather than those who can interprete accurately, the output of each of the EDA steps. And more importantly, Data Analysts spend more than 80% of their analytics time on iterative *EDA*, some of these hours spent checking documentary and *Googling* stuffs.

`pyedahelper` solves this by combining **ready-to-use functions** for your data workflow, AI-powered guide with **inline learning** — you can *see, learn, and apply* the same steps.



## ⚙️ Installation

```bash

pip install pyedahelper==1.0.4

```

## Upgrade

```bash

pip install --upgrade pyedahelper

```
## 🚀 Quick Start

``` python

import edahelper as eda
import pandas as pd

# Load your dataset
df = pd.read_csv("data.csv")

# 📚 Display the interactive EDA cheat-sheet
eda.show() -- for experienced analysts or
eda.core.show() -- for total newbies

# 🔍 Start guided suggestion
eda.next("read_csv")   # Suggests: "View first rows with df.head()"

# 💡 View an example command with short explanation
eda.core.example("describe")
```

From there, the assistant automatically continues:

```bash
df.head() → df.columns → df.shape → df.info() → df.describe() → ...

```
If you want to skip a suggestion, simply type "Next".


# 🔍 Modules Overview

1️⃣ EDA Guidance (AI Suggestion System)

The `next()` method in **pyedahelper** provides *contextual next-step suggestions* for your data analysis workflow.

Instead of remembering long commands, simply call:
```python
eda.next("read_csv")
```
…and it will suggest the next logical step in your EDA, cleaning, visualization, or modeling process.

Below is a list of common helper keywords and what next() will suggest for each stage of analysis:

## 🔹 Basic EDA

```ardiuno
| Keyword    | Suggestion                                                         |
| ---------- | ------------------------------------------------------------------ |
| `read_csv` | View first rows with `df.head()`                                   |
| `head`     | Check column names with `df.columns`                               |
| `columns`  | See shape (rows, columns) using `df.shape`                         |
| `shape`    | Get column data types with `df.info()`                             |
| `info`     | Summarize numeric data with `df.describe()`                        |
| `describe` | Check for missing values using `df.isnull().sum()`                 |
| `isnull`   | Get total missing values count using `df.isnull().sum()`           |
| `sum`      | Fill missing values using `df.fillna()` or drop with `df.dropna()` |

```

## 🔹 Missing Values Handling

```ardiuno
| Keyword            | Suggestion                                                                  |
| ------------------ | --------------------------------------------------------------------------- |
| `fillna`           | Try filling missing values by data type: numeric, categorical, or datetime. |
| `fill_numeric`     | Fill numeric NaNs with `df['col'].fillna(df['col'].mean())`                 |
| `fill_categorical` | Fill categorical NaNs with `df['col'].fillna(df['col'].mode()[0])`          |
| `fill_datetime`    | Fill datetime NaNs with `df['col'].fillna(df['col'].median())`              |
| `dropna`           | Drop missing rows using `df.dropna()` if too many missing values exist.     |

```

## 🔹 Data Cleaning

```ardiuno
| Keyword           | Suggestion                                                |
| ----------------- | --------------------------------------------------------- |
| `duplicated`      | Check for duplicate rows using `df.duplicated().sum()`    |
| `drop_duplicates` | Remove duplicates with `df.drop_duplicates(inplace=True)` |
| `replace`         | Replace wrong entries with `df.replace({'old':'new'})`    |
| `astype`          | Convert columns to proper data types using `df.astype()`  |

```
## 🔹 Visualization
```ardiuno
| Keyword             | Suggestion                                                                                      |
| ------------------- | ----------------------------------------------------------------------------------------------- |
| `plot_distribution` | Plot column distributions using `sns.histplot(df['col'])`                                       |
| `plot_correlation`  | Visualize correlations using `sns.heatmap(df.corr())`                                           |
| `scatterplot`       | Scatter two numeric variables using `sns.scatterplot(x, y, data=df)`                            |
| `cat_num_plot`      | Use `sns.boxplot(x='Category', y='Value', data=df)` for categorical-numerical plots.            |
| `cat_cat_plot`      | Use `sns.countplot(x='Category1', hue='Category2', data=df)` for categorical-categorical plots. |
| `num_num_plot`      | Use `sns.jointplot(x='X', y='Y', data=df)` for numerical-numerical relationships.               |

```
## 🔹 Feature Engineering
```ardiuno
| Keyword         | Suggestion                                                              |
| --------------- | ----------------------------------------------------------------------- |
| `label_encode`  | Label encode with `LabelEncoder()` for categorical columns.             |
| `onehot_encode` | Use `pd.get_dummies(df, columns=['col'])` for one-hot encoding.         |
| `scale_numeric` | Standardize numerical features using `StandardScaler().fit_transform()` |

```

## 🔹 Modeling

```ardiuno
| Keyword                 | Suggestion                                                                |
| ----------------------- | ------------------------------------------------------------------------- |
| `train_test_split`      | Split data using `train_test_split(X, y, test_size=0.2, random_state=42)` |
| `fit_model`             | Train a model like `LogisticRegression().fit(X_train, y_train)`           |
| `predict`               | Predict outcomes with `model.predict(X_test)`                             |
| `classification_report` | Evaluate performance using `classification_report(y_test, y_pred)`        |
| `confusion_matrix`      | Plot confusion matrix with `sns.heatmap(confusion_matrix(...))`           |

```

# This feature helps beginners and professionals alike stay productive and focused on insights rather than remembering syntax.


## 5️⃣ Visualization Module

Functions for exploring and visualizing data quickly.

``` python
from edahelper import visualization as vis

vis.plot_correlation(df)
vis.plot_distribution(df, "Age")
vis.scatter(df, "Age", "Income", hue="Gender")

```
🎨 _Uses matplotlib and seaborn under the hood for fast, clean plots._

# 📘 The Interactive Cheat-Sheet

When you forget a syntax, simply call:
``` python
eda.core.show() or
eda.core_show()

```

✨ Displays a colorful grouped guide of:

Data Loading
Overview
Missing Values
Indexing & Grouping
Visualization
Feature Engineering
NumPy & sklearn tips


## 🧑🏽‍💻 Example Workflow

```
import pyedahelper as eda
import pandas as pd

# Load data
df = pd.read_csv("sales.csv")

# Start guided mode
eda.next("read_csv")    # Suggests df.head()
eda.next('head')        # Suggests df.info()

```


## 📦 Project Structure

```ardiuno

pyedahelper/
│
├── __init__.py              # Main entrypoint
├── core.py                  # Cheat-sheet + examples
├── show.py                  # Display logic
├── stats_summary.py         # Dataset summary helpers
├── visualization.py         # Quick plots (hist, scatter, heatmap)
├── nextstep.py              # AI-guided EDA assistant (eda.next)
└── __init__.py              # Exports unified functions

```

# 🛠 Requirements

Python 3.8+
pandas
numpy
seaborn
scikit-learn
matplotlib
rich (for colored terminal output)

## 🧾 License

MIT License © 2025 Chidiebere Christopher
Feel free to fork, contribute, or use it in your analytics workflow!

## 🌟 Contributing

We welcome contributions — bug fixes, new EDA tools, or notebook examples.

1. Fork the repo
2. Create your feature branch (git checkout -b feature-name)
3. Commit your changes
4. Push and open a Pull Request 🎉

## 🔗 Links

📦 PyPI: https://pypi.org/project/pyedahelper/
💻 GitHub: https://github.com/93Chidiebere/pyedahelper-Python-EDA-Helper
✉️ Author: Chidiebere V. Christopher

🚀 _Learn. Explore. Analyze. Faster._
_pyedahelper — your friendly companion for every EDA project._
