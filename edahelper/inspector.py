"""
inspector.py

Decision-oriented EDA diagnostics.
Surfaces issues that affect modeling readiness rather than only profiling.
"""

from typing import Optional, Dict, Any
import pandas as pd
import numpy as np


class EDAInspector:
    """
    Inspector for identifying modeling and data risks during EDA.

    This module does NOT modify data.
    It only inspects and reports potential issues.
    """

    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("EDAInspector expects a pandas DataFrame")
        self.df = df

    # --------------------------------------------------
    # Core Public API
    # --------------------------------------------------

    def run(self, target: Optional[str] = None, time_col: Optional[str] = None) -> Dict[str, Any]:
        """
        Run all inspections and return a structured report.

        Parameters
        ----------
        target : str, optional
            Target column name (for imbalance and leakage checks)
        time_col : str, optional
            Time column name (for temporal leakage checks)

        Returns
        -------
        dict
            Inspection results
        """
        report = {
            "dataset_shape": self.df.shape,
            "missing_values": self._missing_summary(),
            "duplicates": self._duplicate_summary(),
            "constant_columns": self._constant_columns(),
            "target_analysis": None,
            "temporal_leakage": None,
            "warnings": []
        }

        if target:
            report["target_analysis"] = self._target_inspection(target)

        if time_col:
            report["temporal_leakage"] = self._temporal_leakage_check(time_col, target)

        report["warnings"] = self._compile_warnings(report)
        return report

    # --------------------------------------------------
    # Inspection Methods
    # --------------------------------------------------

    def _missing_summary(self) -> Dict[str, Any]:
        miss = self.df.isna().mean().sort_values(ascending=False)
        high_missing = miss[miss > 0.4].index.tolist()
        return {
            "columns_with_missing": miss[miss > 0].to_dict(),
            "high_missing_columns": high_missing
        }

    def _duplicate_summary(self) -> Dict[str, Any]:
        dup_count = self.df.duplicated().sum()
        return {
            "duplicate_rows": int(dup_count),
            "duplicate_pct": round(dup_count / len(self.df), 4)
        }

    def _constant_columns(self):
        return [
            col for col in self.df.columns
            if self.df[col].nunique(dropna=False) <= 1
        ]

    def _target_inspection(self, target: str) -> Dict[str, Any]:
        if target not in self.df.columns:
            raise KeyError(f"Target column '{target}' not found")

        series = self.df[target]
        result = {
            "dtype": str(series.dtype),
            "unique_values": int(series.nunique()),
            "imbalance": None
        }

        # Classification imbalance
        if series.dtype == "object" or series.nunique() < 20:
            counts = series.value_counts(normalize=True)
            max_share = counts.max()
            result["imbalance"] = {
                "max_class_share": round(float(max_share), 4),
                "severe": bool(max_share > 0.8)
            }

        return result

    def _temporal_leakage_check(self, time_col: str, target: Optional[str]):
        if time_col not in self.df.columns:
            raise KeyError(f"Time column '{time_col}' not found")

        if not np.issubdtype(self.df[time_col].dtype, np.datetime64): # type: ignore
            return {"status": "time column not datetime"}

        sorted_df = self.df.sort_values(time_col)

        if target and target in sorted_df.columns:
            if sorted_df[target].is_monotonic:
                return {"risk": "target monotonic with time"}
        return {"risk": "no obvious temporal leakage"}

    # --------------------------------------------------
    # Warning Synthesis
    # --------------------------------------------------

    def _compile_warnings(self, report):
        warnings = []

        if report["missing_values"]["high_missing_columns"]:
            warnings.append(
                "Some columns have more than 40% missing values."
            )

        if report["duplicates"]["duplicate_rows"] > 0:
            warnings.append(
                "Duplicate rows detected; consider deduplication."
            )

        if report["constant_columns"]:
            warnings.append(
                "Constant-value columns detected; they add no predictive value."
            )

        if report.get("target_analysis"):
            imbalance = report["target_analysis"].get("imbalance")
            if imbalance and imbalance.get("severe"):
                warnings.append(
                    "Severe class imbalance detected in target variable."
                )

        return warnings


# --------------------------------------------------
# Convenience Functional API
# --------------------------------------------------

def inspect(
    df: pd.DataFrame,
    target: Optional[str] = None,
    time_col: Optional[str] = None
) -> Dict[str, Any]:
    """
    Functional wrapper for quick inspection.

    Example
    -------
    >>> import edahelper as eda
    >>> eda.inspect(df, target="label", time_col="date")
    """
    inspector = EDAInspector(df)
    return inspector.run(target=target, time_col=time_col)
