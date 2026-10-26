"""Descriptive seller-price comparisons; these cannot establish collusion."""
import pandas as pd

def multi_seller_product_spreads(items):
    summary = items.groupby("product_id").agg(
        distinct_sellers=("seller_id","nunique"), observations=("price","size"),
        min_observed_price=("price","min"), max_observed_price=("price","max"))
    summary=summary.loc[(summary["distinct_sellers"]>1)&(summary["min_observed_price"]>0)].copy()
    summary["observed_spread_pct"]=(summary["max_observed_price"] / summary["min_observed_price"] - 1)*100
    return summary.sort_values("observed_spread_pct", ascending=False)

def product_month_price_comparison(items, orders):
    merged=items.merge(orders[["order_id","order_purchase_timestamp"]],on="order_id",validate="many_to_one")
    merged["purchase_month"]=merged["order_purchase_timestamp"].dt.to_period("M")
    return (merged.dropna(subset=["purchase_month"])
            .groupby(["product_id","purchase_month","seller_id"])["price"]
            .agg(observations="size", average_price="mean").reset_index())
