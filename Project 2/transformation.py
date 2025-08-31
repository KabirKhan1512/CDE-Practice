import json
import boto3
import pandas as pd
import os
from datetime import datetime
from io import StringIO

# -------------------------------------------------------------------
# AWS CLIENTS
# -------------------------------------------------------------------
s3 = boto3.client("s3")

# -------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------
# IMPORTANT:
# - Do not hardcode sensitive values like bucket names or API keys.
# - Store these in AWS Lambda Environment Variables or AWS Secrets Manager.
# - For local testing, you can set environment variables in a .env file.
BUCKET = os.environ.get("S3_BUCKET_NAME", "your-bucket-name")  # Replace default for local testing only

# Airline mapping (friendly name → IATA airline code)
AIRLINES = {
    "Airsial": "PF",
    "PIA": "PK",
    "SereneAir": "ER",
    "Flyjinah": "9P",
    "Airblue": "PA"
}

# -------------------------------------------------------------------
# MAIN LAMBDA HANDLER
# -------------------------------------------------------------------
def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    This function:
    1. Reads raw flight data (JSON) from S3.
    2. Cleans and normalizes it into Pandas DataFrames.
    3. Saves per-airline processed CSVs back to S3.
    4. Saves a combined CSV (all airlines together) for downstream analytics.
    """

    now = datetime.utcnow()  # Current UTC timestamp (used for folder naming)
    processed_files = []     # List of processed file paths for logging
    combined_df = pd.DataFrame()  # To accumulate all airline data

    # -------------------------------------------------------------------
    # LOOP THROUGH EACH AIRLINE
    # -------------------------------------------------------------------
    for airline_name, iata in AIRLINES.items():
        # Define S3 key paths (raw → processed)
        raw_key = f"raw/{now.year}/{now.month:02d}/{now.day:02d}/{iata}/flights.json"
        processed_key = f"processed/{now.year}/{now.month:02d}/{now.day:02d}/{iata}/flights.csv"

        try:
            # 1. Get raw JSON file from S3
            response = s3.get_object(Bucket=BUCKET, Key=raw_key)
            raw_data = response["Body"].read().decode("utf-8")
            data = json.loads(raw_data)

            # 2. Convert JSON → DataFrame (flatten nested structures)
            df = pd.json_normalize(data.get("data", []), sep="_")

            if df.empty:
                continue  # Skip if no flight data

            # 3. Drop unwanted columns (to reduce noise)
            df = df.drop(
                ["aircraft", "live", "departure_estimated_runway",
                 "departure_actual_runway", "arrival_estimated_runway",
                 "arrival_actual_runway"],
                axis=1,
                errors="ignore"
            )

            # 4. Convert date/time columns to datetime dtype
            cols_to_convert = [
                "flight_date",
                "departure_scheduled",
                "departure_estimated",
                "departure_actual",
                "arrival_scheduled",
                "arrival_estimated",
                "arrival_actual"
            ]
            for col in cols_to_convert:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], errors="coerce")

            # 5. Add airline metadata (useful for joins later)
            df["airline_name"] = airline_name
            df["airline_iata"] = iata

            # 6. Save processed data for this airline as CSV in memory
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False)

            # 7. Upload per-airline processed CSV to S3
            s3.put_object(
                Bucket=BUCKET,
                Key=processed_key,
                Body=csv_buffer.getvalue(),
                ContentType="text/csv"
            )

            # Log success
            processed_files.append(f"{airline_name} ({iata}) → {processed_key}")

            # 8. Append to combined dataframe
            combined_df = pd.concat([combined_df, df], ignore_index=True)

        except s3.exceptions.NoSuchKey:
            # If raw data file doesn't exist, log and continue
            processed_files.append(f"No raw data found for {airline_name} ({iata})")

    # -------------------------------------------------------------------
    # SAVE COMBINED DATASET (all airlines together)
    # -------------------------------------------------------------------
    if not combined_df.empty:
        combined_key = f"processed/{now.year}/{now.month:02d}/{now.day:02d}/all_airlines.csv"
        csv_buffer = StringIO()
        combined_df.to_csv(csv_buffer, index=False)

        s3.put_object(
            Bucket=BUCKET,
            Key=combined_key,
            Body=csv_buffer.getvalue(),
            ContentType="text/csv"
        )

        processed_files.append(f"Combined file saved to {combined_key}")

    # -------------------------------------------------------------------
    # RETURN RESPONSE
    # -------------------------------------------------------------------
    return {
        "statusCode": 200,
        "body": processed_files
    }
