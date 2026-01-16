"""
edahelper: Interactive EDA Assistant
------------------------------------
Provides guided Exploratory Data Analysis tools with step-by-step AI suggestions.
"""

# --- Core imports ---
from .show import show
from .core import example, topics, get_hint

# --- Import the AI EDA guide ---
from .nextstep import EdaGuide

# --- Import decision-oriented inspector ---
from .inspector import inspect, EDAInspector

# --- UI helpers ---
from .ui import summary

# --- Initialize interactive guide ---
_ai = EdaGuide()

# --- Public aliases (avoid shadowing built-ins) ---
next_step = _ai.next
inspect_df = inspect

# --- Exported names ---
__all__ = [
    "show",
    "example",
    "topics",
    "get_hint",
    "next_step",
    "EdaGuide",
    "inspect_df",
    "EDAInspector",
    "summary",
]
