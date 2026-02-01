import numpy as np
import pandas as pd

def generate_sensor_data():
    temperature = 60 + np.random.normal(0, 1)
    vibration = 0.5 + np.random.normal(0, 0.05)
    return {"temperature": temperature, "vibration": vibration}

if __name__ == "__main__":
    data = generate_sensor_data()
    print(data)
