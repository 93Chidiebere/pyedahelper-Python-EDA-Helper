import pandas as pd
from edahelper.data_loading import load_data

def test_csv_load(tmp_path):
    # Create sample CSV
    data = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    file = tmp_path / "test.csv"
    data.to_csv(file, index=False)

    df = load_data(file)
    assert df.shape == (2, 2)