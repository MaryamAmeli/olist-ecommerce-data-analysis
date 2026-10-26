# Olist E-Commerce: Pandas from Beginner to Advanced

An **English-language, step-by-step Jupyter tutorial** on real Brazilian e-commerce records, from reading CSVs to multi-table analysis and visualization. The notebooks and reusable Python modules are designed for an educational GitHub portfolio.



## Contents
- `notebooks/01_pandas_zero_to_advanced.ipynb`: progressively explained, executable lessons and exercises
- `src/data_cleaning.py`: reliable file loading and data-quality checks
- `src/exploratory_analysis.py`: reusable seller, category and monthly summaries
- `src/visualization.py`: plotting helpers
- `src/pricing_analysis.py`: observed price spreads and month-based comparison
- `data/README.md`: download instructions (CSV files are not redistributed)
- `figures/`: optional exported figures
- `results/`: locally generated reports

## Setup
1. Download all nine original CSVs from https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce and put them in `data/`.
2. From the repository root, create and activate a virtual environment (optional but recommended).
3. Run `pip install -r requirements.txt`.
4. Run `jupyter lab` and open `notebooks/01_pandas_zero_to_advanced.ipynb`.
5. **Run all cells from top to bottom**; the notebook locates the project root automatically when started from either the root or `notebooks/`.

## Analytical definitions and limitations
- Item-price sum is **not** the same as payments collected, recognized revenue, or profit.
- A single order may contain several line items and several payment records. Aggregate at order level before joining payments or reviews.
- Repeated price observations may occur on different dates; an observed price gap does **not** imply algorithmic collusion.
- Historical coverage is uneven near the start and end; truncated months should be interpreted cautiously.
- The customer ID and customer unique ID have different meanings.

## Credit and license
Dataset: **Olist**, *Brazilian E-Commerce Public Dataset* (Kaggle). Check the dataset page for applicable conditions.
Code and original explanations: MIT License (see `LICENSE`).
