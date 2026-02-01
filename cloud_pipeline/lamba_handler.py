import boto3
import pandas as pd
from ml_model import predict_anomaly

S3_BUCKET = "your-bucket-name"
CSV_FILE = "live_sensor.csv"

def lambda_handler(event, context):
    # Download CSV from S3
    s3 = boto3.client('s3')
    s3.download_file(S3_BUCKET, CSV_FILE, '/tmp/' + CSV_FILE)

    # Predict anomalies
    anomalies, errors = predict_anomaly('/tmp/' + CSV_FILE)
    print("Anomalies:", anomalies)
    return {
        'statusCode': 200,
        'body': f"{sum(anomalies)} anomalies detected"
    }
