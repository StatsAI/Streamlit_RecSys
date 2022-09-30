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

user_id = st.sidebar.selectbox(label = 'Select the user ID', options = ('1', '2', '3')) 

num_recs = st.sidebar.slider(label = 'Number of Recommendations', min_value = 1,
                          max_value = 5 ,
                          value = 3,
                          step = 1)


####################################################################################################################################################
def retrieval_predict(num_recs, user_id):
	
	#num_recs = to_int(num_recs)
    
	if user_id == "1":
		
		results = ['Delicatessen (1991)', 'Tie Me Up! Tie Me Down! (1990)', 'Amateur (1994)', 'Supercop (1992)', 'City of Lost Children, The (1995)']
		
	if user_id == "2":
		
		results = ['Secrets & Lies (1996)', 'Kolya (1996)', "Ulee's Gold (1997)", "Ulee's Gold (1997)", 'Michael Collins (1996)']
	
	if user_id == "3":
		
		results = ['Deep Rising (1998)', 'Sphere (1998)','Fallen (1998)','Hard Rain (1998)','Jackie Brown (1997)']
		
	return results[:num_recs]

	#return num_recs
	
	# Load Retrieval Model
	#loaded_retrieval_model = tf.saved_model.load('models/basic_ranking_model.pb')
	
	#loaded_retrieval_model = load_model('models/basic_ranking_model.pb')
	
	#scores, titles = loaded_retrieval_model([user_id])
	
	#return titles[0][:num_recs]

	#return loaded_retrieval_model

def ranking_predict(num_recs, user_id):
	
	if user_id == "1":
		
		results = {'Delicatessen (1991)':3.6232116, 'Supercop (1992)':3.6091228, 
			   'Tie Me Up! Tie Me Down! (1990)':3.6056335, 
			   'City of Lost Children, The (1995)':3.5767572, 'Amateur (1994)':3.5685296}

	if user_id == "2":
		
		results = ['Secrets & Lies (1996)', 'Kolya (1996)', "Ulee's Gold (1997)", "Ulee's Gold (1997)", 'Michael Collins (1996)']
	
	if user_id == "3":
		
		results = ['Deep Rising (1998)', 'Sphere (1998)','Fallen (1998)','Hard Rain (1998)','Jackie Brown (1997)']
		
	return results.items()

st.sidebar.write('Instructions: Click on the generate candidates button to generate a list of candidates using the retrieval model.')

#st.sidebar.button('Generate Candidates', key = "1")

if st.sidebar.button('Generate Candidates'):
    
    prediction = retrieval_predict(num_recs, user_id)
    
    st.write('Your candidate recommendations are: ' + str(prediction))
	
	

####################################################################################################################################################	

st.sidebar.write('Instructions: Click on the rank candidates button to rank the candidates using the ranking model.')

if st.sidebar.button('Rank Candidates'):
    
    prediction = ranking_predict(num_recs, user_id)
    
    st.write('Your candidate rankings are: ' + str(prediction))
