"""Load Olist tables and validate basic data quality."""
from pathlib import Path
import pandas as pd

FILES = {
    "items": "olist_order_items_dataset.csv", "orders": "olist_orders_dataset.csv",
    "products": "olist_products_dataset.csv", "sellers": "olist_sellers_dataset.csv",
    "customers": "olist_customers_dataset.csv", "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv", "geolocation": "olist_geolocation_dataset.csv",
    "translations": "product_category_name_translation.csv",
}
DATE_COLUMNS = ["order_purchase_timestamp", "order_approved_at", "order_delivered_carrier_date",
                "order_delivered_customer_date", "order_estimated_delivery_date"]

def load_tables(data_dir):
    """Read all nine original CSVs; raise a clear error if one is missing."""
    folder = Path(data_dir)
    missing = [name for name in FILES.values() if not (folder/name).exists()]
    if missing:
        raise FileNotFoundError("Missing Olist CSV files in " + str(folder) + ": " + ", ".join(missing))
    tables = {key: pd.read_csv(folder/filename) for key,filename in FILES.items()}
    for col in DATE_COLUMNS:
        tables["orders"][col] = pd.to_datetime(tables["orders"][col], errors="coerce")
    tables["items"]["shipping_limit_date"] = pd.to_datetime(
        tables["items"]["shipping_limit_date"], errors="coerce")
    return tables

def quality_report(df):
    """Return each column's dtype, missing count and missing proportion."""
    return pd.DataFrame({"dtype": df.dtypes.astype(str), "missing": df.isna().sum(),
                         "missing_pct": df.isna().mean().mul(100).round(2)})

def order_level_items(items):
    """One row per order. Values are listed item-price and freight sums, not net revenue."""
    return items.groupby("order_id", as_index=False).agg(
        item_value=("price","sum"), freight_total=("freight_value","sum"),
        item_count=("order_item_id","size"))
