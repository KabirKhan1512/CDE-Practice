import os
import logging
import snowflake.connector

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Get Snowflake credentials from environment variables
    user = os.environ['SNOWFLAKE_USER']
    password = os.environ['SNOWFLAKE_PASSWORD']
    account = os.environ['SNOWFLAKE_ACCOUNT']
    warehouse = os.environ.get('SNOWFLAKE_WAREHOUSE', 'COMPUTE_WH')
    database = os.environ.get('SNOWFLAKE_DATABASE', 'FLIGHT_DATA_PROJECT')
    schema = os.environ.get('SNOWFLAKE_SCHEMA', 'PUBLIC')
    
    try:
        # Connect to Snowflake
        with snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        ) as conn:
            with conn.cursor() as cs:
                logger.info("Starting COPY INTO staging table from S3 stage...")
                cs.execute("""
                    COPY INTO staging_all_airlines
                    FROM @flight_data_stage
                    PATTERN = '.*all_airlines[.]csv'
                    FILE_FORMAT = (
                        TYPE = 'CSV'
                        FIELD_OPTIONALLY_ENCLOSED_BY = '"'
                        SKIP_HEADER = 1
                    )
                    ON_ERROR = 'CONTINUE'
                    FORCE = FALSE;  -- only load new files, skip already processed ones
                """)
                logger.info("COPY completed successfully.")
                
        return {
            'statusCode': 200,
            'body': 'Data loaded into staging_all_airlines successfully.'
        }
        
    except snowflake.connector.errors.Error as e:
        logger.error(f"Snowflake error: {e}")
        return {
            'statusCode': 500,
            'body': f"Snowflake error: {e}"
        }
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {
            'statusCode': 500,
            'body': f"Unexpected error: {e}"
        }
