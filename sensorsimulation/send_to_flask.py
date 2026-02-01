import time
import requests
from generate_data import generate_sensor_data

FLASK_URL = "http://127.0.0.1:5000/upload_sensor"

while True:
    data = generate_sensor_data()
    response = requests.post(FLASK_URL, json=data)
    print("Sent:", data, "Status:", response.status_code)
    time.sleep(60)  # wait 1 minute
