import streamlit as st
import json

def json_page():
    st.write('Se ve bonito')
    # Load json file
    st.write(json.load(open('D:/Users/Usuario/Documents/GitHub/MyLearnCoach/app/data/courses_data.json')))
