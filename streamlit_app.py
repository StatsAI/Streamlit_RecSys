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
	
	#titles = str(titles.numpy())
	
	#titles = str(titles.numpy())
	
	#titles = titles.numpy()
	
	#.astype('U13')
	
	#titles = np.array2string(titles, separator = "'")
	
	#titles = list(titles).split(')
	
	titles = titles.split("'")
	
	result = titles
	
	#titles = str(titles)
	
	#result = titles.split("'")
	#.astype('U13')
	
	#inputstring = 'some strings are present in between "geeks" "for" "geeks" '
	#result = titles.split()
	
	#res=[]
	
	#for i in result:
	#	if(i.startswith('"') and i.endswith('"')):
	#		i=i.replace('"',"")
	#		res.append(i)
		
	#titles = titles.numpy().astype('U13')
	
	return result
	
	#return titles[0][:num_recs]

	#return loaded_retrieval_model

def ranking_predict(num_recs, user_id, candidate_predictions):
	
	result = loaded_ranking_model({"user_id": np.array([user_id]), "movie_title": ["Speed (1994)"]}).numpy()
	
	#result = loaded_ranking_model({"user_id": np.array([user_id]), "movie_title": [candidate_predictions]}).numpy()

	return result
	
def ranking_predict_new(num_recs, user_id, candidate_predictions):
	result = {}
	
	test_movie_titles = ['Deep Rising (1998)', 'Sphere (1998)','Fallen (1998)','Hard Rain (1998)','Jackie Brown (1997)']
	
	for movie_title in test_movie_titles:
		result[movie_title] = loaded_ranking_model({
		"user_id": np.array(["3"]),
		"movie_title": np.array([movie_title])
		})
		
	for title, score in sorted(results.items(), key=lambda x: x[1], reverse=True):	
		result[movie_title] = [title, score]

	return result	
	


####################################################################################################################################################

# Initialize session state

#if "load_state" not in st.session_state:
#	st.session_state.load_state = False

if "candidate_predictions" not in st.session_state:
	st.session_state.candidate_predictions = None

st.sidebar.write('Instructions: Click on the generate candidates button to generate a list of candidates using the retrieval model.')

#st.sidebar.button('Generate Candidates', key = "1")

if st.sidebar.button('Generate Candidates'):
	
	#candidate_predictions = retrieval_predict(num_recs, user_id)
	st.session_state.candidate_predictions = retrieval_predict(num_recs, user_id)
	st.write('Your candidate recommendations are: ' + str(st.session_state.candidate_predictions))
	

####################################################################################################################################################	

st.sidebar.write('Instructions: Click on the rank candidates button to rank the candidates using the ranking model.')

if st.sidebar.button('Rank Candidates'):
	
	ranking_predictions = ranking_predict(num_recs, user_id, st.session_state.candidate_predictions)
	st.write('Your candidate recommendations are: ' + str(st.session_state.candidate_predictions))
	st.write('Your candidate rankings are: ' + str(ranking_predictions))
