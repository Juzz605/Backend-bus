import streamlit as st
import pandas as pd

st.title("Live Sensor Dashboard")

data = pd.read_csv("live_sensor.csv")
st.line_chart(data)
