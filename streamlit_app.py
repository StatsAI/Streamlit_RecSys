import streamlit as st
import numpy as np 
import tensorflow as tf
from PIL import Image

st.title('Tensorflow Recommenders Library Movie Recommendation System')

st.write('This is a web app to recommend movies to users based upon their watch history using the Tensorflow Recommenders Python library.')

st.write('It uses the following two-model approach approach, as outlined by: [Tensorflow Recommenders](https://www.tensorflow.org/recommenders/examples/basic_retrieval)')         
         
#opening the image

image = Image.open('images/rec_sys.PNG')

#displaying the image on streamlit app

st.image(image)

st.write('Instructions: The inputs on the sidebar allow you to select the user and the number of recommendations you would like to generate for the user')

st.write('Click on the generate candidates button to generate a list of candidates using the retreval model.')

st.write('Click on the rank candidates button to rank the candidates using the ranking model.')

st.sidebar.write('zys'
         
user_id = st.sidebar.selectbox(label = 'Select the user ID', options = ('1', '2', '3', '4', '5')) 

num_recs = st.sidebar.slider(label = 'Number of Recommendations', min_value = 1.0,
                          max_value = 5.0 ,
                          value = 3.0,
                          step = 1.0)

