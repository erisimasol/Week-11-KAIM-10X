# Week 11 Task: Tesla Stock Analysis

## Overview
This Jupyter Notebook performs an analysis of Tesla, Inc. (Ticker: TSLA) stock data over the past 10 years. It utilizes Python libraries for data manipulation, visualization, and machine learning. The notebook fetches historical stock prices, displays key statistics, and provides insights into Tesla's financial performance.

## Table of Contents
1. [Libraries Import](#libraries-import)
2. [Installing Required Libraries](#installing-required-libraries)
3. [Fetch Tesla Stock Data](#fetch-tesla-stock-data)
4. [Display Historical Data](#display-historical-data)
5. [Tesla Company Information](#tesla-company-information)
6. [Basic Statistics and Data Analysis](#basic-statistics-and-data-analysis)
7. [Conclusion](#conclusion)

## Libraries Import
This section imports necessary libraries for data handling and visualization:
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
```

## Installing Required Libraries
To ensure all necessary libraries are available, the notebook checks for and installs `yfinance` if not already installed:
```bash
pip install yfinance
```

## Fetch Tesla Stock Data
The notebook defines the ticker symbol for Tesla and fetches the historical stock data using the `yfinance` library:
```python
ticker_symbol = 'TSLA'
tesla_data = yf.Ticker(ticker_symbol)
historical_data = tesla_data.history(period='10y')
```

## Display Historical Data
This section prints the historical stock prices of Tesla, highlighting key metrics like Open, High, Low, Close, Volume, Dividends, and Stock Splits.
```python
print("Historical Stock Prices for TSLA:")
print(historical_data)
```

## Tesla Company Information
Detailed information about Tesla, including its address, industry, and key executives, is retrieved and displayed:
```python
TSLA_info = tesla_data.info
print(TSLA_info)
```

## Basic Statistics and Data Analysis
The notebook includes code to check basic statistics, data types, and the presence of null values within the dataset:
```python
print(historical_data.info())
print(historical_data.isnull().sum())
```

## Conclusion
This notebook serves as a foundational analysis tool for understanding Tesla's stock performance over a decade. Further analysis can be conducted using machine learning models and advanced visualization techniques.

## Usage
To run this notebook:
1. Ensure you have Jupyter Notebook installed.
2. Install the required libraries as mentioned.
3. Execute each cell to fetch and analyze the Tesla stock data.

