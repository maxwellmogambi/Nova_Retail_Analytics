import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Engine


def load_dataframe(
    df: pd.DataFrame,
    table_name: str,
    engine: Engine,
    schema: str = "raw",
) -> None:
    """
    Load a DataFrame into a PostgreSQL table.

    If the table already exists, it is replaced.
    """

    with engine.begin() as conn:

        # Create schema if it doesn't exist
        conn.execute(
            text(f"CREATE SCHEMA IF NOT EXISTS {schema};")
        )

    df.to_sql(
        name=table_name,
        con=engine,
        schema=schema,
        if_exists="replace",
        index=False,
        method="multi",
        chunksize=1000,
    )

    print(
        f"✓ Loaded {len(df):,} rows into {schema}.{table_name}"
    )