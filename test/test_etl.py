import pandas as pd
import pytest
from elt import extract_data, transform_data,load_data

# Step 1: Extract
def test_extract_data():
    csv_data = StringIO("""id,name,age,city,salary
1,John Doe,28,New York,70000
2,Jane Smith,34,Los Angeles,80000
3,Bob Johnson,45,Chicago,90000
4,Alice Williams,29,San Francisco,85000
5,Charlie Brown,,Houston,65000
6,Eve Davis,38,Boston,95000
""")
df = pd.read_csv(csv_data)
    # Test de base : le DataFrame n'est pas vide
    assert df is not None
    # Vérifie qu'il y a 6 lignes
    assert len(df) == 6
    # Vérifie que les colonnes sont bien présentes
    expected_columns = ['id', 'name', 'age', 'city', 'salary']
    assert list(df.columns) == expected_columns

# # Step 2: Tarnsform
# def test_transform_data():
#     df_clean = df.dropna()
#     df
#     assert

# # Step 3: Load
# def test_load_data():
#     assert    

