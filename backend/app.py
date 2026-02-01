from flask import Flask, request, jsonify
import pandas as pd
import os
import boto3

app = Flask(__name__)

CSV_FILE = "live_sensor.csv"
S3_BUCKET = "your-bucket-name"  # replace with your bucket name

# Initialize CSV file if not exists
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["temperature", "vibration"])
    df.to_csv(CSV_FILE, index=False)

# AWS S3 client
s3 = boto3.client('s3')

@app.route('/upload_sensor', methods=['POST'])
def upload_sensor():
    content = request.get_json()
    df = pd.DataFrame([content])
    df.to_csv(CSV_FILE, mode='a', header=False, index=False)

    # Optional: upload to S3 immediately
    s3.upload_file(CSV_FILE, S3_BUCKET, CSV_FILE)
    print("Uploaded to S3:", content)

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(port=5000)
