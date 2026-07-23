from pathlib import Path
import pandas as pd


def validate_file_exists(file_path: Path) -> None:
    """
    Ensure the source file exists.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Source file not found: {file_path}")


def validate_not_empty(df: pd.DataFrame, dataset_name: str) -> None:
    """
    Ensure the dataset contains rows.
    """
    if df.empty:
        raise ValueError(f"{dataset_name} is empty.")


def validate_required_columns(
    df: pd.DataFrame,
    required_columns: list[str],
    dataset_name: str,
) -> None:
    """
    Ensure all expected columns are present.
    """
    missing = set(required_columns) - set(df.columns)

    if missing: 
        raise ValueError(
            f"{dataset_name} is missing required columns: "
            f"{sorted(missing)}"
        )


def validate_duplicate_columns(df: pd.DataFrame, dataset_name: str) -> None:
    """
    Detect duplicate column names.
    """
    duplicates = df.columns[df.columns.duplicated()].tolist()

    if duplicates:
        raise ValueError(
            f"{dataset_name} contains duplicate columns: {duplicates}"
        )


def validate_not_null_columns(df, columns, dataset_name):

    for col in columns:

        if df[col].isnull().any():
            raise ValueError(
                f"{dataset_name}: '{col}' contains NULL values."
            )


def validate_primary_key(df, primary_key, dataset_name):

    duplicates = df.duplicated(
        subset=primary_key
    )

    if duplicates.any():

        raise ValueError(
            f"{dataset_name}: duplicate primary key values detected."
        )

def validate(
    df: pd.DataFrame,
    dataset_name: str,
    schema: dict,
) -> None:
    """
    Run all validation checks for a dataset.
    """

    validate_not_empty(df, dataset_name)

    validate_duplicate_columns(df, dataset_name)

    validate_required_columns(
        df,
        schema["columns"],
        dataset_name,
    )

    validate_not_null_columns(
        df,
        schema.get("not_null", []),
        dataset_name,
    )

    validate_primary_key(
        df,
        schema.get("primary_key", []),
        dataset_name,
    )




