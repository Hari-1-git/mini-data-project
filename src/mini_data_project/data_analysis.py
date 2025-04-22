from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# locate the CSV
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_CSV     = PROJECT_ROOT / "data" / "sales.csv"

def load_sales(path: Path) -> pd.DataFrame:
    """Load sales CSV into a DataFrame with parsed dates."""
    return pd.read_csv(path, parse_dates=["month"])

def total_sales(df: pd.DataFrame) -> float:
    """Return total sales."""
    return float(df["sales"].sum())

def average_sales(df: pd.DataFrame) -> float:
    """Return average monthly sales."""
    return float(df["sales"].mean())
def median_sales(df):
    """Return the median monthly sales."""
    return float(df["sales"].median())


def plot_sales(df: pd.DataFrame):
    """Plot monthly sales."""
    df2 = df.sort_values("month")
    plt.figure()
    plt.plot(df2["month"], df2["sales"])
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_sales(DATA_CSV)
    print(f"Total Sales: {total_sales(df):.2f}")
    print(f"Average Sales: {average_sales(df):.2f}")
    plot_sales(df)
