from pathlib import Path
import pandas as pd

# Base directory
data_dir = Path(r"c:\Users\u\Desktop\Repositories\dbt\olist_dbt_project\data")

# Dataset paths
customer_path = data_dir / "olist_customers_dataset.csv"
orders_path = data_dir / "olist_orders_dataset.csv"
order_items_path = data_dir / "olist_order_items_dataset.csv"
payments_path = data_dir / "olist_order_payments_dataset.csv"
reviews_path = data_dir / "olist_order_reviews_dataset.csv"
products_path = data_dir / "olist_products_dataset.csv"
sellers_path = data_dir / "olist_sellers_dataset.csv"
translation_path = data_dir / "product_category_name_translation.csv"
geolocation_path = data_dir / "olist_geolocation_dataset.csv"

# Read datasets
df_1 = pd.read_csv(customer_path)
df_2 = pd.read_csv(orders_path)
df_3 = pd.read_csv(order_items_path)
df_4 = pd.read_csv(payments_path)
df_5 = pd.read_csv(reviews_path)
df_6 = pd.read_csv(products_path)
df_7 = pd.read_csv(sellers_path)
df_8 = pd.read_csv(translation_path)
df_9 = pd.read_csv(geolocation_path)

# Store DataFrames with their paths
datasets = [
    (df_1, customer_path),
    (df_2, orders_path),
    (df_3, order_items_path),
    (df_4, payments_path),
    (df_5, reviews_path),
    (df_6, products_path),
    (df_7, sellers_path),
    (df_8, translation_path),
    (df_9, geolocation_path),
]

# Print dataset name and columns
for df, path in datasets:
    print(f"\n{'='*60}")
    print(f"Dataset: {path.stem}")
    print(f"Rows: {len(df):,} | Columns: {df.shape[1]}")
    print("Columns:")
    for col in df.columns:
        print(f"  - {col}")