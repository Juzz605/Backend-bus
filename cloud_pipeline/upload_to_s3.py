import boto3

s3 = boto3.client('s3')
s3.upload_file("live_sensor.csv", "your-bucket-name", "live_sensor.csv")
print("CSV uploaded to S3!")
