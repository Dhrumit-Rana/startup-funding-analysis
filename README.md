# Startup Funding Analysis

An interactive Streamlit dashboard that explores startup funding in India. Use it to see overall funding trends, look up a single startup, or study an investor's portfolio.

> **Note:** This is a learning project, built to practise **pandas** and **Streamlit**. The dataset is **not fully cleaned**, so some values (for example dates, city names, sector names and investor names) may be missing, inconsistent or duplicated, and the numbers and charts should not be treated as accurate or used for real investment decisions.

## Live Demo

**https://startup-funding-analysis-lsdbcjqpkcatxtrpom7peb.streamlit.app/**

## Features

### Overall Analysis
- Key figures: total funding, maximum funding, average funding per startup, and number of funded startups
- Month-on-month (MoM) graph, switchable between total amount and number of deals
- City-wise funding pie chart
- Top startups, overall or by year
- Top investors

### Startup Analysis
- Industry and location of the selected startup
- Funding rounds table with date, round, investors and amount
- Total amount raised

### Investor Analysis
- Recent investments
- Biggest investments
- Sectors, stages and cities invested in
- Year-wise investment trend

## Tech Stack

- Python
- Streamlit
- pandas
- matplotlib

## Project Structure

```text
startup-funding-analysis/
├── app.py                    # Streamlit app
├── data/
│   └── startup_cleaned.csv   # Partly cleaned dataset
├── requirements.txt
└── README.md
```

## Run Locally

1. Clone the repository

   ```bash
   git clone https://github.com/Dhrumit-Rana/startup-funding-analysis.git
   cd startup-funding-analysis
   ```

2. (Optional) Create and activate a virtual environment

   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Mac/Linux: source .venv/bin/activate
   ```

3. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app

   ```bash
   streamlit run app.py
   ```

   The app opens at http://localhost:8501.

## Data

The dataset contains Indian startup funding records with these columns: date, startup, vertical, subvertical, city, investors, round and amount. Amounts are shown in crore (CR).

**Data quality:** the data is only partly cleaned. Known issues include dates in mixed formats that fail to parse, inconsistent spellings of cities and sectors (for example "Bangalore" and "Bengaluru"), and investor names stored as comma-separated text. Cleaning the data fully was not the goal of this project.

Data source:https://www.kaggle.com/datasets/sudalairajkumar/indian-startup-funding

## What I Learned

- Loading, cleaning and transforming data with pandas
- Grouping and aggregating data with `groupby`
- Building an interactive dashboard with Streamlit widgets, columns and charts
- Deploying a Streamlit app from GitHub

## Possible Improvements

- Clean the data fully (dates, city names, sector names, investors)
- Cache data loading with `@st.cache_data`
- Use interactive charts (for example Plotly)

## Author

Dhrumit-Rana - [GitHub](https://github.com/Dhrumit-Rana)
