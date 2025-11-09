import pytest
from src import merlin

def test_clean_basic():
    import pandas as pd
    df = pd.DataFrame({"A": [1, None, 3]})
    df_clean = merlin.clean(df)
    assert df_clean.isnull().sum().sum() == 0
