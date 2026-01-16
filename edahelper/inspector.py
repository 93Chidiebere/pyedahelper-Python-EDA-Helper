"""
inspector.py

Decision-oriented EDA diagnostics.
Focuses on issues that jeopardize modeling quality, joins, and deployment.
"""

from typing import Optional, Dict, Any, List, Tuple
import pandas as pd
import numpy as np

MAX_INDEX_SAMPLE = 15


class EDAInspector:
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("EDAInspector expects a pandas DataFrame")
        self.df = df

    # ==================================================
    # Public API
    # ==================================================

    def run(
        self,
        target: Optional[str] = None,
        time_col: Optional[str] = None
    ) -> Dict[str, Any]:

        report = {
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

        if target:
            report["target_leakage"] = self._target_leakage_checks(target)

        if time_col:
            report["temporal_checks"] = self._temporal_checks(time_col, target)

        report["warnings"] = self._compile_warnings(report)
        return report

    # ==================================================
    # 1. Missing values (row + column level)
    # ==================================================

    def _missing_diagnostics(self) -> Dict[str, Any]:
        column_summary = {}
        cell_locations: List[Tuple[int, str]] = []

        for col in self.df.columns:
            mask = self.df[col].isna()
            if mask.any():
                indices = self.df.index[mask].tolist()

                # capture explicit row-column locations
                for idx in indices[:MAX_INDEX_SAMPLE]:
                    cell_locations.append((idx, col))

                pct = mask.mean()

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
        indices = self.df.index[dup_mask].tolist()

        return {
            "duplicate_count": int(dup_mask.sum()),
            "duplicate_pct": round(dup_mask.mean(), 4),
            "row_indices_sample": indices[:MAX_INDEX_SAMPLE],
            "recommended_action": "deduplicate_rows" if dup_mask.any() else "none"
        }

    # ==================================================
    # 3. Constant & low-variance columns
    # ==================================================

    def _constant_and_low_variance(self) -> Dict[str, List[str]]:
        constant, low_variance = [], []

        for col in self.df.columns:
            nunique = self.df[col].nunique(dropna=False)
            if nunique <= 1:
                constant.append(col)
            elif nunique <= 3 and self.df[col].dtype != "object":
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
        issues = {}

        for col in self.df.columns:
            s = self.df[col]

            if s.dtype == "object":
                numeric_ratio = pd.to_numeric(s, errors="coerce").notna().mean()
                datetime_ratio = pd.to_datetime(s, errors="coerce").notna().mean()

                if numeric_ratio > 0.9:
                    issues[col] = {
                        "issue": "numeric_as_object",
                        "recommended_action": "cast_to_numeric"
                    }
                elif datetime_ratio > 0.9:
                    issues[col] = {
                        "issue": "datetime_as_object",
                        "recommended_action": "parse_to_datetime"
                    }

        return issues

    # ==================================================
    # 5. Outliers (numeric)
    # ==================================================

    def _outlier_summary(self) -> Dict[str, Any]:
        outliers = {}
        num_cols = self.df.select_dtypes(include=np.number).columns

        for col in num_cols:
            q1, q3 = self.df[col].quantile([0.25, 0.75])
            iqr = q3 - q1
            if iqr == 0:
                continue

            mask = (self.df[col] < q1 - 1.5 * iqr) | (self.df[col] > q3 + 1.5 * iqr)
            if mask.any():
                outliers[col] = {
                    "outlier_count": int(mask.sum()),
                    "row_indices_sample": self.df.index[mask].tolist()[:MAX_INDEX_SAMPLE],
                    "recommended_action": "cap_or_transform"
                }

        return outliers

    # ==================================================
    # 6. Cardinality risks
    # ==================================================

    def _cardinality_risks(self) -> Dict[str, Any]:
        risks = {}

        for col in self.df.select_dtypes(include="object"):
            ratio = self.df[col].nunique() / len(self.df)
            if ratio > 0.8:
                risks[col] = {
                    "unique_ratio": round(ratio, 4),
                    "risk": "id_like_or_high_cardinality",
                    "recommended_action": "drop_or_encode_carefully"
                }

        return risks

    # ==================================================
    # 7. Key & join integrity
    # ==================================================

    def _key_integrity_check(self) -> Dict[str, Any]:
        keys = {}

        for col in self.df.columns:
            ratio = self.df[col].nunique() / len(self.df)
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

        risks = {}
        y = self.df[target]

        for col in self.df.columns:
            if col == target:
                continue

            if self.df[col].equals(y):
                risks[col] = {
                    "risk": "identical_to_target",
                    "recommended_action": "drop_immediately"
                }

            if np.issubdtype(self.df[col].dtype, np.number):
                corr = self.df[col].corr(y)
                if corr is not None and abs(corr) > 0.95:
                    risks[col] = {
                        "risk": f"extremely_high_correlation ({round(corr,3)})",
                        "recommended_action": "review_for_leakage_or_drop"
                    }

        return risks

    # ==================================================
    # 9. Temporal checks
    # ==================================================

    def _temporal_checks(self, time_col: str, target: Optional[str]):
        s = pd.to_datetime(self.df[time_col], errors="coerce")

        result = {
            "parsed_as_datetime": s.notna().mean() > 0.9,
            "is_monotonic": s.is_monotonic_increasing,
            "recommended_action": "sort_by_time_before_split"
        }

        if target and target in self.df.columns:
            result["target_monotonic_with_time"] = (
                self.df.sort_values(time_col)[target].is_monotonic
            )

        return result

    # ==================================================
    # Warning synthesis
    # ==================================================

    def _compile_warnings(self, report: Dict[str, Any]) -> List[str]:
        warnings = []

        if report["missing_values"]["by_column"]:
            warnings.append("Missing values detected; imputation or dropping required.")

        if report["duplicates"]["duplicate_count"] > 0:
            warnings.append("Duplicate rows detected; deduplication recommended.")

        if report["target_leakage"]:
            warnings.append("Target leakage or dangerous correlation detected.")

        return warnings


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
