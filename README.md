# 📊 Sales Data Aggregation & Reporting Pipeline

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline built using **Apache Airflow** for automating the processing of sales data. It handles file merging, transformation, and generates daily reports for analysis.

## 🔧 Tech Stack

- **Apache Airflow** (Dockerized using `puckel/docker-airflow`)
- **Python** (Pandas, OS, shutil)
- **Docker + Docker Compose**
- **CSV** files as input data

---

## 📁 Project Structure

```
.
├── dags/
│   └── sales_report_dag.py         # Main Airflow DAG
├── movement.py                     # Merges raw input files into a single CSV
├── transformation.py              # Aggregates and transforms sales data
├── data/
│   ├── raw/                        # Incoming sales CSVs (index_1.csv, index_2.csv)
│   ├── processed/                  # Processed files after merging
│   └── output/                     # Final reports (daily sales, coffee sales, etc.)
├── docker-compose.yml             # Airflow + Postgres setup
└── README.md
```

---

## 🛠️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Prepare folders:**
   ```bash
   mkdir -p data/raw data/processed data/output
   ```

3. **Place input CSVs:**
   Drop `index_1.csv`, `index_2.csv` into `data/raw/`.

4. **Start Docker:**
   ```bash
   docker-compose up -d
   ```

5. **Access Airflow:**
   Open [http://localhost:8080](http://localhost:8080)
   - Username: `airflow`
   - Password: `airflow`

6. **Trigger the DAG**: `sales_report_pipeline`

---

## ⚙️ Pipeline Workflow

1. **Merge Raw Files**: Appends all CSVs in `raw/` and writes to `processed/merged_sales_data.csv`.
2. **Transform Sales Data**:
   - Aggregates total sales per coffee.
   - Aggregates daily total revenue.
   - Summarizes sales by payment method.
3. **Output Reports**: Saves reports to `data/output/`.

---

## 📈 Sample Reports

- `coffee_sales.csv` — Total sales per coffee type
- `daily_sales.csv` — Sales trend by date
- `payment_sales.csv` — Breakdown by cash/card

---

## ✨ Features

- Modular design using external Python scripts
- Uses `PythonOperator` and `BashOperator`
- Auto-handles file movement after processing
- Easy to extend and schedule

---

## 🧪 Future Improvements

- Add alerting via `EmailOperator`
- Store transformed data into a database (Postgres, SQLite)
- Add Power BI / Tableau visualization layer

---
