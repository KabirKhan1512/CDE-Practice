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

## 📂 Repository Structure

flight-data-pipeline/
│── lambda_function.py # Main Lambda function to process raw S3 JSON → CSV
│── schema.sql # SQL scripts for Snowflake star schema (dims + fact)
│── requirements.txt # Python dependencies for Lambda (Pandas, Boto3, etc.)
│── flow.jpeg # ETL process flow diagram
│── schema.jpeg # Snowflake star schema diagram
│── README.md # Project documentation (this file)

yaml
Copy code

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flight-data-pipeline.git
cd flight-data-pipeline
2. Configure Environment Variables
Set required variables in your Lambda environment or locally using a .env file:

bash
Copy code
S3_BUCKET_NAME=your-bucket-name
AVIATIONSTACK_API_KEY=your-api-key
For production, store sensitive values in AWS Secrets Manager.

3. Deploy to AWS Lambda
Package the code into a ZIP file with dependencies.

Deploy via AWS Console, AWS SAM, or Terraform (optional).

4. Snowflake Setup
Run the provided SQL scripts to create your star schema:

dim_airline

dim_airport

dim_flight

fact_flight_performance

5. Run & Verify
Trigger the Lambda → check S3 bucket for raw/ and processed/ folders.
Snowpipe (or tasks) will load data into Snowflake for analysis.

📊 Future Work
Finalize Power BI dashboards.

Automate Snowflake data refresh with tasks.

Add error monitoring + logging with AWS CloudWatch.

Extend pipeline for more airlines or real-time streaming.

🙌 Acknowledgements
Special thanks to Sir Qasim and Ayan (SMIT) for guidance throughout the course.
```
