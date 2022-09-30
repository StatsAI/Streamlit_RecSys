import streamlit as st
import numpy as np 
import tensorflow as tf

# create 5 pages in streamlit app 
    # page 1: introduction

# add market research tab 


st.title('Wine Quality Classifier Web App')

st.write('This is a web app to classify the quality of your wine based on\
         several features that you can see in the sidebar. Please adjust the\
         value of each feature. After that, click on the Predict button at the bottom to\
         see the prediction of the classifier.')


fixed_acidity = st.sidebar.slider(label = 'Fixed Acidity', min_value = 4.0,
                          max_value = 16.0 ,
                          value = 10.0,
                          step = 0.1)