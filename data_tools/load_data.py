import pandas as pd
import os
from pathlib import Path

def load_parquets(folder_path):
    """
    Load and concatenate all .parquet files in a given folder into a single DataFrame.

    Parameters:
        folder_path (str or Path): Path to the folder containing .parquet files.

    Returns:
        pd.DataFrame: Concatenated DataFrame containing data from all parquet files.
    """
    folder_path = Path(folder_path)
    parquet_files = list(folder_path.glob("*.parquet"))

    if not parquet_files:
        raise FileNotFoundError(f"No .parquet files found in {folder_path}")

    # print(f"Found {len(parquet_files)} parquet files. Loading...")

    df_list = []
    for file in parquet_files:
        # print(f"Reading: {file.name}")
        df = pd.read_parquet(file)
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)
    print(f"Combined DataFrame shape: {combined_df.shape}")

    return combined_df
