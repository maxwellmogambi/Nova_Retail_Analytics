from ingestion.config import SOURCE_FILES, SILVER_DIR
from ingestion.schemas import SCHEMAS
from ingestion.readers import read_csv
from ingestion.writers import write_parquet
from ingestion.transformers import standardize_dataframe
from ingestion.db import get_engine
from ingestion.postgres_loader import load_dataframe
from ingestion.validators import (
    validate,
    validate_file_exists,
    validate_not_null_columns,
    validate_primary_key,

)


def load_historical_data(source_files, output_dir):

    engine = get_engine()

    for dataset_name, source_path in source_files.items():

        try:
            schema = SCHEMAS[dataset_name]

            validate_file_exists(source_path)

            df = read_csv(source_path)

            validate(
                df=df,
                dataset_name=dataset_name,
                schema=schema,
            )

            df = standardize_dataframe(
                df=df,
                schema=schema,
            )

            output_path = output_dir / f"{dataset_name}.parquet"

            write_parquet(
                df=df,
                output_path=output_path,
            )

            load_dataframe(
                df=df,
                table_name=dataset_name,
                engine=engine,
            )

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