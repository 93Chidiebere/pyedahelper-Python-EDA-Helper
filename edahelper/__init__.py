"""
edahelper: Interactive EDA Assistant
------------------------------------
Provides guided Exploratory Data Analysis tools with step-by-step AI suggestions.
"""

# --- Core imports ---
from .show import show
from .core import show as core_show, example, topics, get_hint
# from . import tools  # Uncomment if tools module exists

# --- Import the AI EDA guide ---
from .nextstep import EdaGuide

# --- Import decision-oriented inspector ---
from .inspector import inspect, EDAInspector

# --- Initialize interactive guide ---
_ai = EdaGuide()

# --- Map simple user-friendly functions ---
next = _ai.next  # lets users call eda.next("read_csv")

# --- Exported names ---
__all__ = [
    "show",
    "example",
    "topics",
    "get_hint",
    "next",
    "EdaGuide",
    "inspect",
    "EDAInspector",
    # "tools"  # Uncomment if needed
]
