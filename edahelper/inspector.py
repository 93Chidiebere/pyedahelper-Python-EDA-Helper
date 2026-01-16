"""
inspector.py

Decision-oriented EDA diagnostics.
Focuses on issues that jeopardize modeling quality, joins, and deployment.
"""

from typing import Optional, Dict, Any, List, Tuple
import pandas as pd
import numpy as np
import warnings

MAX_INDEX_SAMPLE = 15


class EDAInspector:
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("EDAInspector expects a pandas DataFrame")
        if df.empty:
            raise ValueError("EDAInspector received an empty DataFrame")
        self.df = df.reset_index(drop=False)  # preserve original index safely

    # ==================================================
    # Public API
    # ==================================================

    def run(
        self,
        target: Optional[str] = None,
        time_col: Optional[str] = None
    ) -> Dict[str, Any]:

        report: Dict[str, Any] = {
            "dataset_shape": self.df.shape,
            "missing_values": self._missing_diagnostics(),
            "duplicates": self._duplicate_diagnostics(),
            "constant_columns": self._constant_and_low_variance(),
            "dtype_issues": self._dtype_mismatches(),
            "outliers": self._outlier_summary(),
            "cardinality": self._cardinality_risks(),
            "key_integrity": self._key_integrity_check(),
            "target_leakage": None,
            "temporal_checks": None,
            "warnings": []
        }

        if target is not None:
            report["target_leakage"] = self._target_leakage_checks(target)

        if time_col is not None:
            report["temporal_checks"] = self._temporal_checks(time_col, target)

        report["warnings"] = self._compile_warnings(report)
        return report

    # ==================================================
    # 1. Missing values
    # ==================================================

    def _missing_diagnostics(self) -> Dict[str, Any]:
        column_summary: Dict[str, Any] = {}
        cell_locations: List[Tuple[int, str]] = []

        for col in self.df.columns:
            mask = self.df[col].isna()
            if not mask.any():
                continue

            indices = self.df.loc[mask, "index"].tolist()
            pct = float(mask.mean())

            for idx in indices[:MAX_INDEX_SAMPLE]:
                cell_locations.append((idx, col))

            column_summary[col] = {
                "missing_count": int(mask.sum()),
                "missing_pct": round(pct, 4),
                "row_indices_sample": indices[:MAX_INDEX_SAMPLE],
                "severity": (
                    "high" if pct > 0.4 else
                    "moderate" if pct > 0.1 else
                    "low"
                ),
                "recommended_action": (
                    "drop_column" if pct > 0.6 else
                    "impute_or_flag" if pct > 0.1 else
                    "monitor"
                )
            }

        return {
            "by_column": column_summary,
            "cell_locations_sample": cell_locations
        }

    # ==================================================
    # 2. Duplicate rows
    # ==================================================

    def _duplicate_diagnostics(self) -> Dict[str, Any]:
        dup_mask = self.df.duplicated()
        indices = self.df.loc[dup_mask, "index"].tolist()

        return {
            "duplicate_count": int(dup_mask.sum()),
            "duplicate_pct": round(float(dup_mask.mean()), 4),
            "row_indices_sample": indices[:MAX_INDEX_SAMPLE],
            "recommended_action": "deduplicate_rows" if dup_mask.any() else "none"
        }

    # ==================================================
    # 3. Constant & low-variance columns
    # ==================================================

    def _constant_and_low_variance(self) -> Dict[str, Any]:
        constant: List[str] = []
        low_variance: List[str] = []

        for col in self.df.columns:
            if col == "index":
                continue

            nunique = self.df[col].nunique(dropna=False)

            if nunique <= 1:
                constant.append(col)
            elif (
                nunique <= 3
                and pd.api.types.is_numeric_dtype(self.df[col])
            ):
                low_variance.append(col)

        return {
            "constant": constant,
            "low_variance": low_variance,
            "recommended_action": "drop_constant_columns"
        }

    # ==================================================
    # 4. Dtype mismatches
    # ==================================================

    def _dtype_mismatches(self) -> Dict[str, Any]:
        issues: Dict[str, Any] = {}

        for col in self.df.columns:
            s = self.df[col]

            if s.dtype != "object":
                continue

            numeric_ratio = pd.to_numeric(s, errors="coerce").notna().mean()

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                datetime_ratio = pd.to_datetime(
                    s, errors="coerce"
                ).notna().mean()

            if numeric_ratio > 0.9:
                issues[col] = {
                    "issue": "numeric_stored_as_object",
                    "recommended_action": "cast_to_numeric"
                }
            elif datetime_ratio > 0.9:
                issues[col] = {
                    "issue": "datetime_stored_as_object",
                    "recommended_action": "parse_to_datetime"
                }

        return issues

    # ==================================================
    # 5. Outliers
    # ==================================================

    def _outlier_summary(self) -> Dict[str, Any]:
        outliers: Dict[str, Any] = {}
        num_cols = self.df.select_dtypes(include=np.number).columns
        n = len(self.df)

        for col in num_cols:
            if col == "index":
                continue

            s = self.df[col].dropna()
            if len(s) < 10:
                continue

            q1, q3 = s.quantile([0.25, 0.75])
            iqr = q3 - q1
            if iqr <= 0:
                continue

            mask = (s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)
            count = int(mask.sum())
            pct = count / n

            if count > 0:
                outliers[col] = {
                    "outlier_count": count,
                    "outlier_pct": round(pct, 4),
                    "severity": (
                        "high" if pct > 0.1 else
                        "moderate" if pct > 0.01 else
                        "low"
                    ),
                    "recommended_action": "review_distribution"
                }

        return outliers

    # ==================================================
    # 6. Cardinality risks
    # ==================================================

    def _cardinality_risks(self) -> Dict[str, Any]:
        risks: Dict[str, Any] = {}

        for col in self.df.select_dtypes(include="object"):
            ratio = self.df[col].nunique(dropna=True) / len(self.df)
            if ratio > 0.8:
                risks[col] = {
                    "unique_ratio": round(ratio, 4),
                    "risk": "high_cardinality_or_id_like",
                    "recommended_action": "drop_or_target_encode"
                }

        return risks

    # ==================================================
    # 7. Key integrity
    # ==================================================

    def _key_integrity_check(self) -> Dict[str, Any]:
        keys: Dict[str, Any] = {}

        for col in self.df.columns:
            ratio = self.df[col].nunique(dropna=False) / len(self.df)
            if ratio > 0.98:
                keys[col] = {
                    "uniqueness_ratio": round(ratio, 4),
                    "possible_primary_key": True,
                    "recommended_action": "exclude_from_features"
                }

        return keys

    # ==================================================
    # 8. Target leakage & correlation risks
    # ==================================================

    def _target_leakage_checks(self, target: str) -> Dict[str, Any]:
        if target not in self.df.columns:
            raise KeyError(f"Target '{target}' not found")

        risks: Dict[str, Any] = {}
        y = self.df[target]

        if not pd.api.types.is_numeric_dtype(y):
            return {"note": "Non-numeric target; correlation checks skipped"}

        for col in self.df.select_dtypes(include=np.number):
            if col == target:
                continue

            corr = self.df[col].corr(y)
            if corr is not None and not np.isnan(corr) and abs(corr) > 0.95:
                risks[col] = {
                    "risk": "extreme_correlation",
                    "correlation": round(float(corr), 4),
                    "recommended_action": "investigate_leakage_or_drop"
                }

        return risks

    # ==================================================
    # 9. Temporal checks
    # ==================================================

    def _temporal_checks(self, time_col: str, target: Optional[str]):
        if time_col not in self.df.columns:
            raise KeyError(f"Time column '{time_col}' not found")

        s = pd.to_datetime(self.df[time_col], errors="coerce")

        result: Dict[str, Any] = {
            "parsed_as_datetime": s.notna().mean() > 0.9,
            "is_monotonic": s.is_monotonic_increasing,
            "recommended_action": "sort_by_time_before_split"
        }

        if target and target in self.df.columns:
            result["target_sorted_by_time_monotonic"] = (
                self.df.assign(_t=s)
                .sort_values("_t")[target]
                .is_monotonic
            )

        return result

    # ==================================================
    # Warning synthesis
    # ==================================================

    def _compile_warnings(self, report: Dict[str, Any]) -> List[str]:
        warnings_out: List[str] = []

        if report["missing_values"]["by_column"]:
            warnings_out.append("Missing values detected.")

        if report["duplicates"]["duplicate_count"] > 0:
            warnings_out.append("Duplicate rows detected.")

        if report["target_leakage"]:
            warnings_out.append("Potential target leakage or extreme correlation detected.")

        return warnings_out


# ==================================================
# Functional API
# ==================================================

def inspect(
    df: pd.DataFrame,
    target: Optional[str] = None,
    time_col: Optional[str] = None
) -> Dict[str, Any]:
    """
    Quick inspection wrapper.
    """
    return EDAInspector(df).run(target=target, time_col=time_col)
