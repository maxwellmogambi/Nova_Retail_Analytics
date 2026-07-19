from pathlib import Path

def write_parquet(df, output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)