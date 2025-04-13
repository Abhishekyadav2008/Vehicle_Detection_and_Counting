import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("🚗 Vehicle Detection Dashboard")

if os.path.exists("count.txt"):
    with open("count.txt", "r") as f:
        count = f.read()
else:
    count = "0"

st.metric("Total Vehicles Detected", count)

st.video("video.mp4")