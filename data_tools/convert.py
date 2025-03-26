import h5py
import numpy as np

def save_df_to_hdf5(df, output_path, station_col="Samplingpoint", pollutant_col="Pollutant"):
    with h5py.File(output_path, "w") as h5f:
        grouped = df.groupby([station_col, pollutant_col])

        for (station, pollutant), group in grouped:
            group_name = f"{station}/{pollutant}"
            g = h5f.create_group(group_name)

            # Timestamps
            timestamps = group['Start'].astype(str).to_numpy()
            dt_dtype = h5py.string_dtype(encoding='utf-8')
            g.create_dataset("timestamps", data=timestamps, dtype=dt_dtype, compression="gzip", chunks=True)

            # Values
            values = group['Value'].to_numpy(dtype=np.float32)
            g.create_dataset("values", data=values, compression="gzip", chunks=True)

            # Metadata
            g.attrs["country"] = group["Samplingpoint"].iloc[0][:2]
            g.attrs["unit"] = group["Unit"].iloc[0]
            g.attrs["aggType"] = group["AggType"].iloc[0]

        print(f"Saved to {output_path}")