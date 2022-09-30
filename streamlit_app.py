import streamlit as st
import numpy as np 
import tensorflow as tf
from PIL import Image

#loaded_retrieval_model = tf.saved_model.load('saved_model.pb')

####################################################################################################################################################

st.title('Tensorflow Recommenders Library Movie Recommendation System')

st.write('This is a web app to recommend movies to users based upon their watch history using the Tensorflow Recommenders Python library.')

st.write('It uses the following two-model approach approach, as outlined by: [Tensorflow Recommenders](https://www.tensorflow.org/recommenders/examples/basic_retrieval)')         


####################################################################################################################################################

#opening the image

image = Image.open('images/rec_sys.PNG')

#displaying the image on streamlit app

st.image(image)

st.sidebar.write('Instructions: Use the below controls to select the number of movie recommendations you would like to generate for a given user.')

user_id = st.sidebar.selectbox(label = 'Select the user ID', options = ('1', '2', '3', '4', '5')) 

num_recs = st.sidebar.slider(label = 'Number of Recommendations', min_value = 1.0,
                          max_value = 5.0 ,
                          value = 3.0,
                          step = 1.0)


####################################################################################################################################################
def retrieval_predict(num_recs, user_id):
	
	#num_recs = to_int(num_recs)
    
	if user_id == "1":
		
		results = ['Delicatessen (1991)', 'Tie Me Up! Tie Me Down! (1990)', 'Amateur (1994)', 'Supercop (1992)', 'City of Lost Children, The (1995)']
		
	#return results[:2]

	return num_recs
	
	# Load Retrieval Model
	#loaded_retrieval_model = tf.saved_model.load('models/basic_ranking_model.pb')
	
	#loaded_retrieval_model = load_model('models/basic_ranking_model.pb')
	
	#scores, titles = loaded_retrieval_model([user_id])
	
	#return titles[0][:num_recs]

	#return loaded_retrieval_model


st.sidebar.write('Instructions: Click on the generate candidates button to generate a list of candidates using the retrieval model.')

#st.sidebar.button('Generate Candidates', key = "1")

if st.sidebar.button('Generate Candidates'):
    
    prediction = retrieval_predict(num_recs, user_id)
    
    st.write('Your candidate recommendations are: ' + str(prediction))
	
	

####################################################################################################################################################	

st.sidebar.write('Instructions: Click on the rank candidates button to rank the candidates using the ranking model.')

st.sidebar.button('Rank Candidates')
