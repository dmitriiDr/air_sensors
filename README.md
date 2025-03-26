# Air Quality HDF5 Project

This project processes real air quality data in `.parquet` format (e.g. downloaded from the European Environment Agency or similar sources) and converts it into a structured, compressed HDF5 file using Python.

## Features

- Loads multiple `.parquet` files from a folder
- Combines them into a single `DataFrame`
- Converts the data to HDF5 format:
  - One group per station and pollutant
  - Datasets for timestamps and values
  - Metadata (units, country, aggregation type)
- Chunked and compressed for performance

---

## 🚀 How to Use

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```
### 2. Prepare Input Files

Put all your .parquet files in a folder, for example: data/

### 3. Run the Pipeline

```bash
python main.py --input_path data/ --output_path hdf5_data/air_quality_data.h5
```