"""Reusable chart functions. Titles and axes are intentionally explicit."""
import matplotlib.pyplot as plt

def price_histogram(items, bins=40):
    fig, ax = plt.subplots(figsize=(8,4))
    ax.hist(items["price"].dropna(), bins=bins, edgecolor="white")
    ax.set(title="Distribution of listed item prices", xlabel="Item price (BRL)", ylabel="Item count")
    fig.tight_layout()
    return fig,ax

def monthly_line(monthly):
    fig,ax=plt.subplots(figsize=(9,4))
    ax.plot(monthly.index.astype(str), monthly.to_numpy(), marker="o")
    ax.set(title="Monthly observed item value", xlabel="Purchase month", ylabel="Item-price sum (BRL)")
    ax.tick_params(axis="x",rotation=60)
    fig.tight_layout()
    return fig,ax
