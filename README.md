# 🧠 pyedahelper — Simplify Your Exploratory Data Analysis (EDA)

**pyedahelper** is an educational and practical Python library designed to make **Exploratory Data Analysis (EDA)** simple, guided, and fast — especially for **data analysts, students, and early-career data scientists**.

It combines:
- ⚡ A **smart EDA cheat sheet** (interactive and collapsible),
- 🧩 A suite of **data tools** for real-world EDA tasks (loading, cleaning, feature engineering, visualization, and summaries),
- 💬 Handy **code hints and examples** you can copy directly into your notebook.

---

## 🌍 Why pyedahelper?

Performing EDA often involves repeating the same code patterns, from loading data and checking for missing values to feature scaling and visualizing trends.

`pyedahelper` solves this by combining **ready-to-use functions** for your data workflow with **inline learning** — you can *see, learn, and apply* the same steps.

---

## ⚙️ Installation

```bash

pip install pyedahelper

```

## Upgrade

```bash

pip install --upgrade pyedahelper

```
## 🚀 Quick Start

``` python

import pyedahelper as eda

# 📚 Show the interactive EDA cheat-sheet
eda.core.show()

# 💡 View an example command with short explanation
eda.core.example("describe")

# 🔍 List all available EDA topics
eda.core.topics()
```

# 🧰 The Tools Module

pyedahelper.tools provides practical helper functions grouped into EDA phases.
Each can be imported individually or through the parent module.

## 1️⃣ Data Loading

Load data from CSV, Excel, JSON, SQL, or Parquet.

```python

from pyedahelper import tools as t

# Load a CSV file
df = t.data_loading.load_csv("data/sales.csv")

# Load from Excel
df = t.data_loading.load_excel("data/sales.xlsx", sheet_name="Sheet1")
```
## 2️⃣ Data Overview

Get an immediate feel of your dataset: missing values, data types, numeric summaries, etc.

```python

t.data_overview.quick_summary(df)
t.data_overview.show_missing(df)
t.data_overview.numeric_overview(df)

```
📊 _Returns insights such as top null columns, unique counts, and numeric distribution summaries_

## 3️⃣ Data Cleaning

Quick utilities for fixing missing data and inconsistent data types.

``` python

t.data_cleaning.fill_missing(df, strategy="mean")
t.data_cleaning.drop_duplicates(df)
t.data_cleaning.convert_dtype(df, "Date", "datetime")

```
💧 _Simple, consistent wrappers to keep cleaning code readable_.

## 4️⃣ Feature Engineering

Encode categorical data, scale numeric features, and prepare your dataset for modeling.

``` python

t.feature_engineering.encode_label(df, "Gender")
t.feature_engineering.encode_onehot(df, "City")
t.feature_engineering.scale_numeric(df)

```
⚙️ _Includes basic preprocessing using scikit-learn’s encoders and scalers_.

## 5️⃣ Visualization

Instant charts and quick patterns for EDA insights.

``` python
t.visualization.plot_correlation(df)
t.visualization.plot_distribution(df, "Age")
t.visualization.scatter(df, "Age", "Income", hue="Gender")

```
🎨 _Uses matplotlib and seaborn under the hood for fast, clean plots._

# 📘 The Interactive Cheat-Sheet

When you forget a syntax, simply call:
``` python
eda.core.show()

```

✨ Displays a colorful grouped guide of:

Data Loading
Overview
Missing Values
Indexing & Grouping
Visualization
Feature Engineering
NumPy & sklearn tips

You can also view specific examples:

``` python

eda.core.example("pivot")
```

Output

``` sql
Aggregation & Grouping — Pivot table
  pd.pivot_table(df, index='col', values='val', aggfunc='mean')

```

## 💬 Hints

A mini hint engine for quick reminders:

``` bash

eda.core.get_hint("describe")
# "After df.describe(), check df.isnull().sum() and df.dtypes."

```python

## 🧑🏽‍💻 Example Workflow

import pyedahelper as eda
from pyedahelper import tools as t

# Load your data
df = t.data_loading.load_csv("transactions.csv")

# Quick overview
t.data_overview.quick_summary(df)

# Clean
df = t.data_cleaning.fill_missing(df, "mean")

# Feature engineering
df = t.feature_engineering.encode_label(df, "AccountType")

# Visualize
t.visualization.plot_correlation(df)

# Learn syntax while you work
eda.core.example("groupby")

```

## 📦 Project Structure

```ardiuno
pyedahelper/
│
├── __init__.py
├── core.py              # cheat sheet + examples
├── show.py              # handles display logic
├── tools.py             # shared utilities
├── data_loading.py
├── data_overview.py
├── data_cleaning.py
├── feature_engineering.py
└── visualization.py
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
💻 GitHub: Coming soon
✉️ Author: Chidiebere V. Christopher

🚀 _Learn. Explore. Analyze. Faster._
_pyedahelper — your friendly companion for every EDA project._