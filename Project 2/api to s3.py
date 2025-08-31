import json
import urllib3
import boto3
import os
from datetime import datetime

# Initialize AWS S3 client and HTTP request pool
s3 = boto3.client("s3")
http = urllib3.PoolManager()

# -------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------
# Sensitive values should NOT be hardcoded. 
# Instead, use environment variables (set in AWS Lambda console or .env file locally).
BUCKET = os.environ.get("S3_BUCKET_NAME", "your-bucket-name")  # S3 bucket to store data
ACCESS_KEY = os.environ.get("AVIATIONSTACK_API_KEY", "dummy-key")  # AviationStack API key

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
    # Current UTC timestamp (used for S3 folder structure)
    now = datetime.utcnow()
    results = []  # To collect logs/results for each airline

    # Loop through each airline in our mapping
    for airline_name, iata in AIRLINES.items():
        # Build request URL for AviationStack API
        url = f"http://api.aviationstack.com/v1/flights?access_key={ACCESS_KEY}&airline_iata={iata}"
        
        try:
            # Call the external API
            resp = http.request("GET", url)
            data = json.loads(resp.data.decode("utf-8"))

            # Define S3 key structure:
            # raw/YYYY/MM/DD/IATA/flights.json
            key = f"raw/{now.year}/{now.month:02d}/{now.day:02d}/{iata}/flights.json"

            # Upload the response JSON into S3
            s3.put_object(
                Bucket=BUCKET,
                Key=key,
                Body=json.dumps(data),
                ContentType="application/json"
            )

            # Log success for this airline
            results.append(f"{airline_name} ({iata}) saved to {key}")

        except Exception as e:
            # Log failure if something goes wrong
            results.append(f"Failed {airline_name} ({iata}): {str(e)}")

    # Return results (useful for CloudWatch logs or API Gateway integration)
    return {
        "statusCode": 200,
        "body": results
    }
