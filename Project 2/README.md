# ✈️ Flight Data ETL Pipeline (Pakistan's All Airlines)

This project builds a **serverless ETL pipeline** to fetch, process, and store flight data of Pakistan’s airlines using the [AviationStack API](https://aviationstack.com/), AWS, and Snowflake.

It is my **first end-to-end data engineering project** after completing my training with **Sir Qasim and Ayan at SMIT**.

---

## 📌 Project Overview

The pipeline automates the following steps:

1. **Extract** flight data of major Pakistani airlines (PIA, Airsial, SereneAir, Fly Jinnah, Airblue) from the AviationStack API.
2. **Store Raw Data** into AWS S3 in JSON format, partitioned by date and airline.
3. **Transform** raw JSON into clean CSVs using AWS Lambda and **Pandas**:
   - Flatten nested JSON.
   - Drop unnecessary fields (e.g., live data, aircraft details).
   - Convert timestamps into proper datetime format.
   - Append airline metadata (IATA code, airline name).
4. **Save Processed Data** back to S3 as both:
   - Per-airline CSV files.
   - A combined file containing all airlines for the day.
5. **Load into Snowflake**:
   - A **star schema** with **3 dimensions** (Airline, Airport, Flight) and **1 fact table (Flight Performance)**.
6. **Visualize** the processed data in **Power BI** (in progress).

---

## 🖼️ Project Flow

### 🔹 ETL Flow

![Flow Diagram](flow.jpeg)

### 🔹 Snowflake Schema

![Snowflake Schema](schema.jpeg)

---

## ⚙️ Tech Stack

- **AWS Lambda** – ETL orchestration
- **AWS S3** – Data lake (raw + processed zones)
- **Python (Pandas, Boto3, urllib3)** – Data processing and API integration
- **Snowflake** – Data warehouse with star schema
- **Power BI** – Visualization and analysis (ongoing)
- **AWS Secrets Manager** – Secure storage for API keys and sensitive credentials

---
