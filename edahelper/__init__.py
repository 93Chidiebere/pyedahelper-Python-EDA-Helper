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

from .show import show

from .core import show as core_show, example, topics, get_hint
# from . import tools
from .show import show

__all__ = ["show", "example", "topics", "get_hint", "tools"]
