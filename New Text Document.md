# ☁️ Cloud Data Engineering Practice Repository

Welcome! This repository is my **Cloud Data Engineering practice lab**.  
It’s built to document my journey after completing a Data Engineering course — where I’ll apply theory to **real-world pipelines, APIs, and analytics projects**.

---

## 🎯 Goals

- Strengthen **ETL / ELT pipeline building** with modern cloud tools
- Practice **data modeling, orchestration, and streaming**
- Build **Power BI dashboards** for insights
- Gain hands-on experience with **AWS, Snowflake, Kafka, Airflow, and Python**

---

## 📂 Planned Projects

### 🟢 Beginner–Intermediate

1. 🎧 **Spotify Playlist Dynamics Tracker**  
   Stream play events → Kafka → Airflow → Snowflake → Power BI dashboards (trends, genres, retention).

2. ✈️ **Flight Price History Archiver**  
   Daily flight prices → Airflow → S3 → Lambda → Snowflake. Dashboards for price trends & volatility.

3. 🎮 **Multi-Platform Game Release Tracker**  
   Scrape Steam/Epic/Xbox → normalize releases → Snowflake → Visualize genres & platform growth.

4. 🗃️ **AWS S3 → Redshift Incremental Load Orchestrator**  
   Detect new S3 files → Transform in Docker tasks → Load deltas into Redshift.

5. 📊 **YouTube Metadata Pipeline**  
   YouTube API → Flatten JSON → AWS Glue → Snowflake → Star schema for engagement analytics.

6. 💬 **On-Demand YouTube Comments Archiver**  
   Fetch comments via Python → Kafka → Snowflake → Sentiment analysis (NLTK/TextBlob).

7. 🌦️ **Global Weather Data Hub**  
   NOAA/OpenWeatherMap APIs → NiFi ingestion → Snowflake climate trend analysis.

---

### 🟡 Intermediate

8. 🛍️ **Geo-Fenced Retail Analytics Dashboard**  
   Enrich purchase logs with geodata → Kafka → Snowflake → BI maps.

9. 🔌 **EV Charging Station Availability System**  
   Real-time API polling → Kafka → Snowflake SQL views → Power BI dashboards.

10. 💳 **Credit Card Transaction Anomaly Feeder**  
    Visa/Mastercard streams → Kafka → Snowflake → Fraud detection models.

11. 🔐 **Real-Time GDPR Compliance Pipeline**  
    Kafka streams → Lambda PII redaction → Snowflake compliance reporting.

12. 📈 **Crypto Exchange Order Book Synchronizer**  
    Binance/Kraken order books → Kafka → Snowflake → Price spread analytics.

13. 🕹️ **Real-Time e-Sports Match Telemetry**  
    Game events → Kafka/NiFi → Snowflake → Player performance dashboards.

14. 🏃‍♂️ **Player Fatigue Model**  
    Stream stats → Python fatigue scoring → Snowflake → BI for coaches.

15. 🚨 **Dynamic Ad Click Fraud Detector**  
    Stream click events → Anomaly detection in Python → Snowflake storage.

16. ⚙️ **Serverless ML Model Retrainer**  
    Airflow DAGs → Lambda retrains → Store models in S3 → Monitor accuracy.

17. 🛫 **Real-Time Flight Delay Predictor**  
    Airline APIs → NiFi ingestion → Python feature engineering → Snowflake.

---

### 🔴 Advanced

18. 🎲 **Sports Betting Odds Analyzer**  
    Bookmaker APIs → Kafka → PySpark analysis → Snowflake.

19. 🎤 **Concert Demand Forecasting**  
    Ticketmaster + Spotify → Kafka → Snowflake ML models → Demand predictions.

20. 🧊 **NFT Trading Monitor**  
    Blockchain streams → Kafka → Python transforms → Snowflake → BI visualizations.

21. ⚡ **Energy Market Arbitrage**  
    Live market feeds → Kafka → Airflow pipelines → Snowflake → Opportunity detection.

22. ⛓️ **Block-to-SQL Blockchain Indexer**  
    Ethereum blocks → Python parsing → Snowflake relational schema.

23. 📰 **Stock News Correlator**  
    SEC + Bloomberg feeds → Kafka/NiFi → Snowflake → NLP sentiment analytics.

---

## 🛠️ Tech Stack

- **Languages**: Python (Pandas, Matplotlib, Seaborn, Plotly, NLTK)
- **Cloud**: AWS (S3, Lambda, Glue, MWAA, Redshift)
- **Data Warehouse**: Snowflake
- **Streaming**: Apache Kafka, NiFi
- **Orchestration**: Apache Airflow
- **Visualization**: Power BI

---

## 🚀 Next Steps

- [ ] Implement projects incrementally
- [ ] Document architecture diagrams for each project
- [ ] Share Power BI dashboards screenshots
- [ ] Add lessons learned in `docs/`

---

✨ _This repo is my sandbox — a place to experiment, learn, and build real-world Cloud Data Engineering workflows._  
Stay tuned! 🚀
