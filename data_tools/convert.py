import h5py
import numpy as np
import pandas as pd

def save_df_to_hdf5(df, output_path, station_col="Samplingpoint", pollutant_col="Pollutant"):
    # Extract clean station name (before the last underscore)
    df = df.copy()
    df["station_clean"] = df[station_col].apply(lambda x: x.rsplit("_", 1)[0])

    with h5py.File(output_path, "w") as h5f:
        for (station, pollutant), group in df.groupby(["station_clean", pollutant_col]):
            group_name = f"{station}/{pollutant}"
            g = h5f.create_group(group_name)

            # Timestamps
            timestamps = pd.to_datetime(group["Start"]).astype(str).to_numpy()
            dt_dtype = h5py.string_dtype(encoding='utf-8')
            g.create_dataset("timestamps", data=timestamps, dtype=dt_dtype, compression="gzip", chunks=True)

            # Clean and filter values
            raw_values = pd.to_numeric(group["Value"], errors='coerce')
            cleaned_values = raw_values.mask(raw_values <= -900, np.nan).fillna(0.0).astype(np.float32)
            g.create_dataset("values", data=cleaned_values.to_numpy(), compression="gzip", chunks=True)

            # Metadata
            g.attrs["unit"] = str(group["Unit"].iloc[0])
            g.attrs["agg_type"] = str(group["AggType"].iloc[0])
            g.attrs["validity"] = int(group["Validity"].iloc[0])
            g.attrs["result_time"] = str(group["ResultTime"].iloc[0])

        print(f"Saved structured HDF5 to {output_path}")