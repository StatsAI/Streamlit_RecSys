import streamlit as st
import numpy as np 
import tensorflow as tf

# create 5 pages in streamlit app 
    # page 1: introduction

# add market research tab 
app_mode = st.sidebar.selectbox('Select Page', ['Introduction', 'Patient Dashboard', 'Modeling Accuracy Dashboard', 'Real-time Prediction', 'Hardware Build'])

if app_mode == 'Introduction':
    st.title("Project Background")
    st.markdown("Dataset :")

if app_mode == 'Patient Dashboard':
    st.title("Patient Dashboard")
	st.markdown("Dataset :")
