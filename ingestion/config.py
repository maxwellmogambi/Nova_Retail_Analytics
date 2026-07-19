from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"

BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"

# Source datasets (Historical)
SOURCE_FILES = {
    "customers": BRONZE_DIR / "olist_customers_dataset.csv",
    "orders": BRONZE_DIR / "olist_orders_dataset.csv",
    "order_items": BRONZE_DIR / "olist_order_items_dataset.csv",
    "payments": BRONZE_DIR / "olist_order_payments_dataset.csv",
    "reviews": BRONZE_DIR / "olist_order_reviews_dataset.csv",
    "products": BRONZE_DIR / "olist_products_dataset.csv",
    "sellers": BRONZE_DIR / "olist_sellers_dataset.csv",
    "geolocation": BRONZE_DIR / "olist_geolocation_dataset.csv",
    "category_translation": BRONZE_DIR / "product_category_name_translation.csv",
}