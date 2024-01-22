import pandas as pd
import pyarrow
import fastparquet

parquet_file_path = 'file.parquet'
df = pd.read_parquet(parquet_file_path, engine='pyarrow')
print("all:",df)

# ---
df = pd.read_parquet(parquet_file_path, engine='pyarrow',columns=['BRANCH', 'EFFECTIVE_DATE'])
print("cloumn:",df)