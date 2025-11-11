# 🧠 pyedahelper - Simplify Your Exploratory Data Analysis (EDA)

**pyedahelper** is an educational and practical Python library designed to make **Exploratory Data Analysis (EDA)** simple, guided, and fast, especially for **data analysts, students, and early-career data scientists** who want to spend more time analyzing data and less time remembering syntax.

It's a lightweight, educational, and intelligent Python library that helps you perform Exploratory Data Analysis (EDA) faster — with guided suggestions, ready-to-use utilities, and clean visualizations.


🌟 Key Features:
- ⚡ A **smart EDA cheat sheet** (interactive and collapsible),
- 💬 AI-guided EDA assistant — suggests the next logical step (e.g., “View top rows with df.head()”).
- 🧩 A suite of **data tools** for real-world EDA tasks (loading, cleaning, feature engineering, visualization, and summaries),
- 💬 Handy **code hints and examples** you can copy directly into your notebook.

---

## 🌍 Why pyedahelper?

Performing EDA often involves the use of numerous syntaxes to understand the dataset, it forces the narrative that good data professionals are those who know all the *Python syntaxes* by heart rather than those who can interprete accurately, the output of each of the EDA steps. And more importantly, Data Analysts spend more than 80% of their analytics time on iterative *EDA*, some of these hours spent checking documentary and *Googling* stuffs.

`pyedahelper` solves this by combining **ready-to-use functions** for your data workflow, AI-powered guide with **inline learning** — you can *see, learn, and apply* the same steps.

---

## ⚙️ Installation

```bash

pip install pyedahelper==1.0.2

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

The AI-powered step recommender helps complete beginners know what to do next.

Example flow:
```python
eda.next("read_csv")   # Suggests df.head()
eda.next("head")       # Suggests df.columns
eda.next("columns")    # Suggests df.shape

```

It covers:

. Dataset overview (head, columns, shape, info, describe)

. Missing values (isnull, fillna, dropna)

. Data cleaning (duplicated, astype, replace)

. Visualization (plot_distribution, scatterplot, plot_correlation)

. Feature prep and modeling steps (label_encode, split, fit_model, predict)


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
