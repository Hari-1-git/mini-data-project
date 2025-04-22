import pytest
import pandas as pd
from mini_data_project.data_analysis import load_sales, total_sales, average_sales, median_sales


@pytest.fixture
def sample_df(tmp_path):
    p = tmp_path / "test.csv"
    p.write_text("month,sales\n2025-01,10\n2025-02,20\n")
    return load_sales(p)

def test_load_sales_parses_date(sample_df):
    assert "month" in sample_df.columns
    assert pd.api.types.is_datetime64_any_dtype(sample_df["month"])

def test_total_sales(sample_df):
    assert total_sales(sample_df) == 30

def test_average_sales(sample_df):
    assert average_sales(sample_df) == 15
def test_median_sales(sample_df):
    # sample_df has [10,20] → median is 15
    assert median_sales(sample_df) == 15

