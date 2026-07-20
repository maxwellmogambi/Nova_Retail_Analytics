import pandas as pd


def standardize_dataframe(df, schema):

    df = df.copy()

    # Column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    # Trim strings
    object_cols = df.select_dtypes(include="object").columns

    for col in object_cols:
        df[col] = df[col].str.strip()

    # Datetime conversion
    for col in schema["datetime_columns"]:

        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

    # Numeric conversion
    for col in schema["numeric_columns"]:

        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # Remove duplicates
    df = df.drop_duplicates()

    return df