"""Simple reusable exploratory summaries."""
import pandas as pd

def seller_summary(items):
    return (items.groupby("seller_id").agg(
        item_count=("price","size"), observed_item_value=("price","sum"),
        average_item_price=("price","mean"))
        .sort_values("observed_item_value", ascending=False))

def category_summary(items, products, translations):
    tagged = items.merge(products[["product_id","product_category_name"]], on="product_id", how="left", validate="many_to_one")
    tagged = tagged.merge(translations, on="product_category_name", how="left", validate="many_to_one")
    return (tagged.groupby("product_category_name_english", dropna=False)
            .agg(observed_item_value=("price","sum"), item_count=("price","size"))
            .sort_values("observed_item_value", ascending=False))

def monthly_item_values(items, orders, delivered_only=False):
    records = items.merge(orders[["order_id","order_purchase_timestamp","order_status"]],
                          on="order_id", validate="many_to_one", how="left")
    if delivered_only:
        records=records.loc[records["order_status"].eq("delivered")]
    return (records.dropna(subset=["order_purchase_timestamp"])
            .groupby(records["order_purchase_timestamp"].dt.to_period("M"))["price"].sum()
            .rename("observed_item_value").sort_index())
