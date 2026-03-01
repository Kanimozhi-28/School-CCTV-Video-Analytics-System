import streamlit as st

def show_camera_card(camera_name, status):
    st.write(f"Camera: {camera_name} - Status: {status}")
