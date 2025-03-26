from data_tools.load_data import load_parquets
from data_tools.convert import save_df_to_hdf5
import argparse
from pathlib import Path

def main(input_path, output_path):
    df = load_parquets(input_path)
    save_df_to_hdf5(df, output_path)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert Parquet air quality data to HDF5 format.")
    parser.add_argument("--input_path", type=str, required=True, help="Path to the folder containing .parquet files.")
    parser.add_argument("--output_path", type=str, required=True, help="Path to save the resulting .h5 file.")

    args = parser.parse_args()

    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input path {input_path} does not exist.")
    if not input_path.is_dir():
        raise NotADirectoryError(f"Input path {input_path} is not a directory.")
    if not output_path.parent.exists():
        output_path.parent.mkdir(parents=True, exist_ok=True)

    main(input_path, output_path)