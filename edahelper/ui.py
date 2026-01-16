def summary(report: dict) -> None:
    print("\nEDA SUMMARY")
    print("───────────")

    rows, cols = report["dataset_shape"]
    print(f"Dataset shape: {rows} rows × {cols} columns\n")

    # -----------------------
    # Data quality
    # -----------------------
    print("DATA QUALITY")

    if report["missing_values"]["by_column"]:
        print("• Missing values detected")
    else:
        print("• Missing values: None detected")

    dup = report["duplicates"]["duplicate_count"]
    print(f"• Duplicate rows: {dup}")

    constants = report["constant_columns"]["constant"]
    if constants:
        print(f"• Constant columns: {', '.join(constants)}")

    low_var = report["constant_columns"]["low_variance"]
    if low_var:
        print(f"• Low-variance columns: {', '.join(low_var)}")

    # -----------------------
    # Outliers
    # -----------------------
    if report["outliers"]:
        print("\nFEATURE RISKS")
        print(f"• Outliers detected in {len(report['outliers'])} numeric columns")

        for col, v in report["outliers"].items():
            print(f"  - {col} ({v['outlier_pct']*100:.1f}% of rows)")

    # -----------------------
    # Cardinality
    # -----------------------
    if report["cardinality"]:
        print("\nENCODING & KEYS")
        print("• High-cardinality columns:")
        for col in report["cardinality"]:
            print(f"  - {col} (likely ID)")

    # -----------------------
    # Keys
    # -----------------------
    keys = report["key_integrity"]
    if keys:
        print("• Possible primary keys:")
        for col in keys:
            print(f"  - {col}")

    # -----------------------
    # Actions
    # -----------------------
    print("\nACTIONABLE NEXT STEPS")
    step = 1

    if constants:
        print(f"{step}. Drop constant columns: {', '.join(constants)}")
        step += 1

    if report["cardinality"]:
        print(f"{step}. Exclude ID-like columns from modeling")
        step += 1

    if report["outliers"]:
        print(f"{step}. Review skewed numeric features before modeling")
