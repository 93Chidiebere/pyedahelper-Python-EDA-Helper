# from .core import show, example
# from . import (
#     data_loading,
#     data_cleaning,
#     feature_engineering,
#     visualization,
#     stats_summary
# )

# __all__ = [
#     "show",
#     "example",
#     "data_loading",
#     "data_cleaning",
#     "feature_engineering",
#     "visualization",
#     "stats_summary"
# ]

# # edahelper/__init__.py
# from .core import show, example, topics, get_hint

# # Keep advanced tools available under a single namespace to avoid clutter.
# # Importing the whole module won't force many names into the top-level namespace.
# from . import data_loading as tools  # users can use eda.tools.load_csv if they want

# __all__ = ["show", "example", "topics", "get_hint", "tools"]

# from .show import show

# from .core import show as core_show, example, topics, get_hint
# # from . import tools
# from .show import show

# __all__ = ["show", "example", "topics", "get_hint", "tools"]

# from .nextstep import EdaGuide

# __init__.py
"""
edahelper: Interactive EDA Assistant
------------------------------------
Provides guided Exploratory Data Analysis tools with step-by-step AI suggestions.
"""

# --- Core imports (keep your existing ones) ---
from .show import show
from .core import show as core_show, example, topics, get_hint
# from . import tools  # Uncomment if tools module exists

# --- Import the AI EDA guide ---
from .nextstep import EdaGuide

# --- Initialize interactive guide ---
_ai = EdaGuide()

# --- Map simple user-friendly functions ---
show = show                   # keeps your normal show()
next = _ai.next               # lets users call eda.next("read_csv")

# --- Exported names ---
__all__ = [
    "show",
    "example",
    "topics",
    "get_hint",
    "next",
    "EdaGuide",
    # "tools"  # Uncomment if needed
]