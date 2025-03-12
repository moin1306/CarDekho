import pytest
from modules.file_handler import load_csv

def test_load_csv():
    df, error = load_csv("data/housing_prices.csv")
    assert df is not None
    assert error is None
