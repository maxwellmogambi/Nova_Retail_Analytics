from ingestion.config import SOURCE_FILES, SILVER_DIR
from ingestion.schemas import SCHEMAS
from ingestion.readers import read_csv
from ingestion.writers import write_parquet
from ingestion.transformers import standardize_dataframe
from ingestion.validators import (
    validate,
    validate_file_exists,
)


def load_historical_data(source_files, output_dir):

    for dataset_name, source_path in source_files.items():

        try:

            validate_file_exists(source_path)

            df = read_csv(source_path)

            schema = SCHEMAS[dataset_name]

            validate(
                df=df,
                dataset_name=dataset_name,
                required_columns=schema["columns"],
            )

            df = standardize_dataframe(
                df,
                schema,
            )
            output_path = output_dir / f"{dataset_name}.parquet"

            write_parquet(df, output_path)

            print(f"✓ {dataset_name} loaded successfully.")

        except Exception as e:

            print(f"✗ {dataset_name}: {e}")


def main():

    load_historical_data(
        SOURCE_FILES,
        SILVER_DIR,
    )


if __name__ == "__main__":
    main()