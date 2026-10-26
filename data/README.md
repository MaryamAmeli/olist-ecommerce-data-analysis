# Dataset Information

## 1. Dataset Overview

This project uses the **Brazilian E-Commerce Public Dataset by Olist**, a real-world e-commerce dataset available on Kaggle.

The dataset contains approximately 100,000 orders placed between 2016 and 2018 on Brazilian online marketplaces. It includes information about customers, sellers, products, orders, payments, shipping, and customer reviews.

The dataset supports educational exercises, exploratory data analysis (EDA), statistical analysis, data visualization, and pricing analysis using Python and Pandas.

## 2. Dataset Source

- **Dataset:** Brazilian E-Commerce Public Dataset by Olist
- **Provider:** Olist
- **Platform:** Kaggle
- **Download:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- **Period:** 2016–2018
- **Approximate orders:** 100,000

## 3. Dataset Files

| File | Description |
|---|---|
| `olist_orders_dataset.csv` | Order status and timestamps |
| `olist_order_items_dataset.csv` | Items, products, sellers, transaction prices, and freight charges |
| `olist_products_dataset.csv` | Product features and categories |
| `olist_sellers_dataset.csv` | Seller information and locations |
| `olist_customers_dataset.csv` | Customer identifiers and locations |
| `olist_order_payments_dataset.csv` | Payment methods, installments, and values |
| `olist_order_reviews_dataset.csv` | Ratings and customer reviews |
| `olist_geolocation_dataset.csv` | Postal codes and geographic coordinates |
| `product_category_name_translation.csv` | Portuguese-to-English product category translations |

## 4. Download and Setup

The original CSV files are **not included** in this GitHub repository.

1. Open the [dataset page on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
2. Download and extract the dataset archive.
3. Place the nine CSV files directly inside this `data/` directory.
4. Install the dependencies listed in the project's `requirements.txt`.
5. Open the notebook in `notebooks/` and run the cells in order.

Expected folder structure after downloading:

```text
data/
├── README.md
├── olist_orders_dataset.csv
├── olist_order_items_dataset.csv
├── olist_products_dataset.csv
├── olist_sellers_dataset.csv
├── olist_customers_dataset.csv
├── olist_order_payments_dataset.csv
├── olist_order_reviews_dataset.csv
├── olist_geolocation_dataset.csv
└── product_category_name_translation.csv
```

## 5. Analysis Applications

- Data cleaning and exploratory data analysis (EDA)
- Descriptive statistics and visualization
- Product-price distributions and category comparisons
- Monthly order and item-value trends
- Seller and customer analysis
- Shipping and customer-review analysis
- Observed price variation across sellers

## 6. Important Limitations

- The data record historical transactions, **not** a complete record of product listings, competitors' price offers, or automated pricing decisions.
- Observed differences in transaction prices do not establish algorithmic coordination or collusion.
- Item prices, payment totals, and realized net revenue are different measures. Order status, refunds, shipping charges, and table relationships must be considered.
- The study period is historical; findings should not be presented as current marketplace conditions.

## 7. Attribution and Usage

The dataset was published by **Olist** and is available through **Kaggle**. This project does not claim ownership of the original data. Consult the dataset page for its applicable license and usage conditions before redistributing data.

**Suggested attribution:** Olist. *Brazilian E-Commerce Public Dataset by Olist*. Kaggle. https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
