# nextstep.py
"""
AI-style step-by-step workflow suggestion engine for beginners using pandas, seaborn, matplotlib, and scikit-learn.
"""

class EdaGuide:
    """
    EDAHelper AI Suggestion Guide
    Suggests the next logical action for data analysis, cleaning, visualization, or modeling.
    """

    def __init__(self):
        self.steps = [
            # === Basic EDA ===
            ("read_csv", "View first rows with `df.head()`"),
            ("head", "Check column names with `df.columns`"),
            ("columns", "See shape (rows, columns) using `df.shape`"),
            ("shape", "Get column data types with `df.info()`"),
            ("info", "Summarize numeric data with `df.describe()`"),
            ("describe", "Check for missing values using `df.isnull().sum()`"),
            ("isnull", "Get total missing values count using `df.isnull().sum()`"),
            ("sum", "Fill missing values using `df.fillna()` or drop with `df.dropna()`"),

            # === Missing Values Handling ===
            ("fillna", "Try filling missing values by data type: numeric, categorical, or datetime."),
            ("fill_numeric", "Fill numeric NaNs with `df['col'].fillna(df['col'].mean())`"),
            ("fill_categorical", "Fill categorical NaNs with `df['col'].fillna(df['col'].mode()[0])`"),
            ("fill_datetime", "Fill datetime NaNs with `df['col'].fillna(df['col'].median())`"),
            ("dropna", "Drop missing rows using `df.dropna()` if too many missing values exist."),

            # === Data Cleaning ===
            ("duplicated", "Check for duplicate rows using `df.duplicated().sum()`"),
            ("drop_duplicates", "Remove duplicates with `df.drop_duplicates(inplace=True)`"),
            ("replace", "Replace wrong entries with `df.replace({'old':'new'})`"),
            ("astype", "Convert columns to proper dtypes using `df.astype()`"),

            # === Visualization ===
            ("plot_distribution", "Plot column distributions using `sns.histplot(df['col'])`"),
            ("plot_correlation", "Visualize correlations using `sns.heatmap(df.corr())`"),
            ("scatterplot", "Scatter two numeric variables using `sns.scatterplot(x, y, data=df)`"),
            ("cat_num_plot", "Use `sns.boxplot(x='Category', y='Value', data=df)` for categorical-numerical plots."),
            ("cat_cat_plot", "Use `sns.countplot(x='Category1', hue='Category2', data=df)` for categorical-categorical plots."),
            ("num_num_plot", "Use `sns.jointplot(x='X', y='Y', data=df)` for numerical-numerical relationships."),

            # === Feature Engineering ===
            ("label_encode", "Label encode with `LabelEncoder()` for categorical columns."),
            ("onehot_encode", "Use `pd.get_dummies(df, columns=['col'])` for one-hot encoding."),
            ("scale_numeric", "Standardize numerical features using `StandardScaler().fit_transform()`"),

            # === Modeling ===
            ("train_test_split", "Split data using `train_test_split(X, y, test_size=0.2, random_state=42)`"),
            ("fit_model", "Train a model like `LogisticRegression().fit(X_train, y_train)`"),
            ("predict", "Predict outcomes with `model.predict(X_test)`"),
            ("classification_report", "Evaluate performance using `classification_report(y_test, y_pred)`"),
            ("confusion_matrix", "Plot confusion matrix with `sns.heatmap(confusion_matrix(...))`"),

            ("done", "🎉 Great job! You've completed the analysis pipeline!")
        ]
        self.step_keys = [k for k, _ in self.steps]
        self.current_index = None
        
    # def ai_suggest(self, step):
    #     """Manually get suggestion for any step without triggering next()."""
    #     suggestion = self.steps.get(step) # type: ignore
    #     if suggestion:
    #         print(f"💡 Suggestion after '{step}': {suggestion}")
    #     else:
    #         print("⚠️ No suggestion found for this step.")


    def show(self):
        """Show all available EDA workflow steps."""
        print("📘 EDAHelper AI Workflow Guide")
        print("=" * 40)
        for i, (key, desc) in enumerate(self.steps, start=1):
            print(f"{i:02d}. {key:20} → {desc}")
        print("\nStart the flow with:  eda.next('read_csv')")

    def next(self, step=None):
        """Suggest next logical command after a given step."""
        if step == "read_csv":
            self.current_index = 0
            print("✅ Dataset loaded! Try viewing the first few rows:\n👉 `df.head()`")
            return

        if step == "next" and self.current_index is not None:
            self.current_index += 1
        elif step:
            if step not in self.step_keys:
                print("⚠️ Step not recognized. Try `eda.show()` to see all options.")
                return
            self.current_index = self.step_keys.index(step)

        if self.current_index is None:
            print("ℹ️ Start with `eda.next('read_csv')` to begin suggestions.")
            return

        # Suggest next
        next_index = self.current_index + 1
        if next_index < len(self.steps):
            key, desc = self.steps[next_index]
            print(f"Next step: `{key}` → {desc}")
        else:
            print("🎉 End of AI guide — you’ve reached the modeling phase!")