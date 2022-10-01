import streamlit as st
import numpy as np 
import tensorflow as tf
from PIL import Image


# load tensorflow models for retrieval and ranking
loaded_retrieval_model = tf.saved_model.load('models/index_model')
loaded_ranking_model = tf.saved_model.load('models/ranking_model')

# this works
#model1 = tf.keras.models.load_model('models/my_keras_model1.h5')

####################################################################################################################################################

st.title('Tensorflow Recommenders Library Movie Recommendation System')

st.write('This is a web app to recommend movies to users based upon their watch history using the Tensorflow Recommenders Python library.')

st.write('It uses the following two-model approach approach, as outlined by: [Tensorflow Recommenders](https://www.tensorflow.org/recommenders/examples/basic_retrieval)')         

#opening the image

image = Image.open('images/rec_sys.PNG')

#displaying the image on streamlit app

st.image(image)

st.sidebar.write('Instructions: Use the below controls to select the number of movie recommendations you would like to generate for a given user.')

user_id = st.sidebar.selectbox(label = 'Select the user ID', options = ('1', '2', '3', '4','5','6','7','8','9','10')) 

num_recs = st.sidebar.slider(label = 'Number of Recommendations', min_value = 1,
                          max_value = 5 ,
                          value = 3,
                          step = 1)

####################################################################################################################################################
def retrieval_predict(num_recs, user_id):
	
	scores, titles = loaded_retrieval_model([user_id])
	
	return titles[0][:num_recs]

	#return loaded_retrieval_model

def ranking_predict(num_recs, user_id, candidate_predictions):
	
	result = loaded_ranking_model({"user_id": np.array([user_id]), "movie_title": ["Speed (1994)"]}).numpy()
	
	#result = loaded_ranking_model({"user_id": np.array([user_id]), "movie_title": [candidate_predictions]}).numpy()

	#return result[:num_recs]
	
	return list(result.items())[:num_recs]

####################################################################################################################################################

# Initialize session state

if "load_state" not in st.session_state:
	st.session_state.load_state = False


st.sidebar.write('Instructions: Click on the generate candidates button to generate a list of candidates using the retrieval model.')

#st.sidebar.button('Generate Candidates', key = "1")

if st.sidebar.button('Generate Candidates') or st.session_state.load_state:
    
    candidate_predictions = retrieval_predict(num_recs, user_id)
    
    st.write('Your candidate recommendations are: ' + str(candidate_predictions))
	

####################################################################################################################################################	

st.sidebar.write('Instructions: Click on the rank candidates button to rank the candidates using the ranking model.')

if st.sidebar.button('Rank Candidates'):
    
    ranking_predictions = ranking_predict(num_recs, user_id)
    
    st.write('Your candidate rankings are: ' + str(ranking_predictions))
