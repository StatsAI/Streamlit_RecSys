import streamlit as st
import numpy as np 
import tensorflow as tf

# create 5 pages in streamlit app 
    # page 1: introduction

# add market research tab 


st.title('Tensorflow Recommenders: Movie Recommendation System')

st.write('This is a web app to recommend movies using the Tensorflow Recommenders Python library. It uses the following approach:')

st.write('Instructions: The inputs on the sidebar allow you to select the user and the number of recommendations you would like to get. After that, click on the generate recommendations button at the bottom to get the results!')


user_id = st.selectbox(label = 'Select the user ID', ('Email', 'Home phone', 'Mobile phone'))

num_recs = st.sidebar.slider(label = 'Number of Recommendations', min_value = 1.0,
                          max_value = 5.0 ,
                          value = 3.0,
                          step = 1.0)
