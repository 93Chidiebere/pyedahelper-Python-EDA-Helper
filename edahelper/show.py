# edahelper/show.py
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

def _section(title, commands):
    """Helper: render a nice table section with commands."""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("Example Syntax", style="green")

    for cmd, example in commands:
        table.add_row(cmd, example)

    console.print(Panel.fit(table, title=f"[bold yellow]{title}", border_style="bright_blue"))

def show():
    """Display an educational cheat sheet for basic pandas-based data analysis."""
    console.rule("[bold red]📘 EDA Helper Cheat Sheet")
    console.print(Text("Simplify your exploratory data analysis with Python & pandas\n", style="italic cyan"))

    # 1️⃣ Data Loading
    _section("Data Loading", [
        ("Read CSV", "pd.read_csv('file.csv')"),
        ("Read Excel", "pd.read_excel('file.xlsx')"),
        ("Read JSON", "pd.read_json('file.json')"),
        ("Read SQL", "pd.read_sql(query, connection)")
    ])

    # 2️⃣ Data Overview
    _section("Data Overview", [
        ("Head", "df.head()"),
        ("Tail", "df.tail()"),
        ("Info", "df.info()"),
        ("Describe", "df.describe()"),
        ("Shape", "df.shape"),
        ("Columns", "df.columns")
    ])

    # 3️⃣ Data Cleaning
    _section("Data Cleaning", [
        ("Drop NaN", "df.dropna()"),
        ("Fill NaN", "df.fillna(value)"),
        ("Rename Columns", "df.rename(columns={'old':'new'})"),
        ("Replace Values", "df.replace({'old':'new'})"),
        ("Drop Duplicates", "df.drop_duplicates()")
    ])

    # 4️⃣ Feature Engineering
    _section("Feature Engineering", [
        ("Create New Column", "df['new'] = df['A'] + df['B']"),
        ("Map Values", "df['Gender'] = df['Gender'].map({'M':1, 'F':0})"),
        ("Binning", "pd.cut(df['Age'], bins=[0,18,35,60,100])"),
        ("Datetime Conversion", "pd.to_datetime(df['date'])")
    ])

    # 5️⃣ Visualization
    _section("Visualization", [
        ("Histogram", "df['col'].hist()"),
        ("Boxplot", "df.boxplot(column='col')"),
        ("Scatter Plot", "df.plot.scatter('x','y')"),
        ("Correlation Heatmap", "sns.heatmap(df.corr())")
    ])

    # 6️⃣ Summarization
    _section("Summarization", [
        ("Value Counts", "df['col'].value_counts()"),
        ("Unique Values", "df['col'].unique()"),
        ("Group By", "df.groupby('col').mean()"),
        ("Pivot Table", "pd.pivot_table(df, index='A', values='B')")
    ])

    console.rule("[bold green]💡 Tip: Use edahelper.show() anytime you need a quick reminder!")