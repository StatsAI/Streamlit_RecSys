import streamlit as st
import numpy as np 
import tensorflow as tf
from PIL import Image

st.title('Streamlit + Tensorflow Recommenders: Movie Recommendation System')

st.write('This is a web app to recommend movies using the Tensorflow Recommenders Python library. It uses the following approach:')

#opening the image

image = Image.open('images/rec_sys.PNG')

#displaying the image on streamlit app

st.image(image)

st.write("Image Source: [Tensorflow Recommenders](https://www.tensorflow.org/recommenders/examples/basic_retrieval)")

st.write('Instructions: The inputs on the sidebar allow you to select the user and the number of recommendations you would like to get. After that, click on the generate recommendations button at the bottom to get the results!')

user_id = st.sidebar.selectbox(label = 'Select the user ID', options = ('1', '2', '3', '4', '5')) 

num_recs = st.sidebar.slider(label = 'Number of Recommendations', min_value = 1.0,
                          max_value = 5.0 ,
                          value = 3.0,
                          step = 1.0)

