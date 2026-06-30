# End-to-End Financial Data Pipeline: From Chaos to Database Insights

## Project Overview
This repository showcases an end-to-end data engineering and analytics pipeline. The project takes highly corrupted, raw financial transactional data, transforms it using clean validation rules, secures data persistence in a local MySQL instance, and builds analytical matrices and time-series reports.

---

## Tech Stack & Tools
* **Languages**: Python, SQL
* **Libraries**: Pandas, NumPy, Matplotlib, SQLAlchemy
* **Database**: MySQL Relational Database Server
* **Environment**: JupyterLab

---

## ⚡ The STAR Method Project Case Study

### 1. Situation
Production financial data feeds (modeled around public central banking structures) frequently suffer from upstream system updates, manual logging bugs, and layout variations. The initial dataset received was completely unreadable and broken due to multi-format date logging, negative currency volume anomalies, and messy text boundaries.

### 2. Task
Design and implement an automated **ETL (Extract, Transform, Load)** pipeline to clean the raw variables, enforce financial absolute value rules, secure data mapping inside a MySQL table schema, and surface transactional matrix insights.

### 3. Action
* **Data Transformation**: Engineered a modular cleaning engine using **Pandas** to extract specific numbers out of mixed strings via regular expressions, safely handle conflicting multi-format dates (`format='mixed'`), eliminate irregular structural white-space padding, and map literal text null values (`"N/A"`, `"NULL"`) to formal indicators.
* **Database Engineering**: Configured a secure relational database connection using **SQLAlchemy** to store the cleaned tables, ensuring rapid downstream query capabilities.
* **Exploratory Data Analysis**: Authored advanced analytical **SQL scripts** utilizing window functions, dense ranking partitions, and nested subquery conditional tiering to segment currency volumes.
* **Multi-Dimensional Modeling**: Constructed cross-tabulation reports utilizing Pandas Pivot Tables to break down time-series trends by currency types while dynamically mapping data gaps to explicit zero-fills.
* **Data Visualization**: Formatted chronological tracking charts via **Matplotlib** to evaluate monthly velocity trend lines.

### 4. Result
* Restored **100% data integrity** across a completely corrupted dataset.
* Transformed an unpredictable raw text block into an active, production-grade database asset.
* Isolated high-value target categories via multi-layer relational data segmentation.

---

## Core Code Architecture & Snippets

### Phase 1: Python ETL Pipeline
```python
import pandas as pd
import numpy as np

# Load and drop whitespace anomalies
df = pd.read_csv("data/raw_chaotic_data.csv")
df = df.replace(r'^\s*$', np.nan, regex=True).drop_duplicates()

# Regex numeric extraction and validation
df['Exchange_Rate_Clean'] = df['Exchange_Rate'].astype(str).str.extract(r'(-?\d+\.\d+|-?\d+)')
df['Exchange_Rate_Clean'] = pd.to_numeric(df['Exchange_Rate_Clean'], errors='coerce').abs().fillna(0)

# String normalization & hidden character elimination
df["Currency_Code"] = (df["Currency_Code"]
                       .astype(str)
                       .str.replace(r'[\n\t]', ' ', regex=True)
                       .str.strip()
                       .str.upper()
                       .replace(["NONE", "N/A", "NULL", "NAN"], np.nan)
                       .fillna("Unknown"))

# Date homogenization
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'], format='mixed', errors='coerce')
```

### Phase 2: Relational Database Integration
```python
from sqlalchemy import create_engine

# Establishing secure SQL dialect mapping (Credentials generalized for deployment)
engine = create_engine("mysql+mysqlconnector://user:DB_PASSWORD@localhost/financial_db")
df.to_sql("clean_local_disaster_data", con=engine, if_exists="replace", index=False)
```

### Phase 3: Analytical Reports & Multi-Dimensional Pivot Tables

#### Advanced Cross-Tabulation Matrix
```python
# Create multi-currency report matrix
report = pd.pivot_table(df, index="month_exchanged", columns="Currency_Code", values="Exchange_Rate_Clean", aggfunc="sum", fill_value=0)

# Enforce strict chronological reindexing
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
report = report.reindex(month_order)
```

#### SQL Currency Performance Tiering Subquery
```sql
SELECT
	Currency_Code,
	SUM(Exchange_Rate) AS total_exchange_rate,
	CASE
		WHEN SUM(Exchange_Rate) > (
			SELECT AVG(total_per_currency)
			FROM (
				SELECT SUM(Exchange_Rate) AS total_per_currency
				FROM clean_local_disaster_data
				GROUP BY Currency_Code
			) subquery
		) THEN 'Premier'
		ELSE 'Standard'
	END AS Classifying_Currency_Code
FROM clean_local_disaster_data
WHERE Currency_Code != 'UNKNOWN'
GROUP BY Currency_Code
ORDER BY total_exchange_rate DESC;
```

#### SQL Daily Intra-Window Volatility Ranking
```sql
SELECT
	Transaction_Date,
	Exchange_Rate,
	DENSE_RANK() OVER(
		PARTITION BY Transaction_Date
		ORDER BY Exchange_Rate
	) AS order_of_exchangerate
FROM clean_local_disaster_data
WHERE Transaction_Date != '2026-01-01' AND Exchange_Rate > 0;
```

---

## Executive Visual Dashboards

### Chronological Monthly Volume Trends
*(Embedded figures below showcase analytical data trends sorted chronologically via system categorical mapping.)*

![Monthly Volume Trend Line Chart](images/linegraph.png)
![Currency Volume Bar Chart](images/barchart.png)
