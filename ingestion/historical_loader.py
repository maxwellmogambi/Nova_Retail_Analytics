from ingestion.config import SILVER_DIR, SOURCE_FILES
from ingestion.readers import read_csv
from ingestion.writers import write_parquet
import pyarrow
import fastparquet

def load_historical_data(source_files, output_dir):
    for dataset_name, source_path in source_files.items():
        # Read the CSV file
        df = read_csv(source_path)

        # Define the output path for the Parquet file
        output_path = output_dir / f"{dataset_name}.parquet"

        # Write the DataFrame to Parquet format
        write_parquet(df, output_path)

        print(f"Loaded {dataset_name} from {source_path} and saved to {output_path}")

def main():
    load_historical_data(SOURCE_FILES, SILVER_DIR)  

if __name__ == "__main__":
    main()
