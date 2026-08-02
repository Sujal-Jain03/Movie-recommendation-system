import streamlit as st
import pickle
import nltk
import pandas as pd

import joblib

st.title('Movie Recommendation System')

with open('movies.pickle','rb') as m:
    movies=pickle.load(m)

similarity=joblib.load('similarity.joblib','rb')
movies_titles=movies['title'].values

def recommend(name_movie):
    movie_index=movies[movies['title']==name_movie].index[0]
    
    recommendations=similarity[movie_index]
    
    movie_list=sorted(enumerate(recommendations),reverse=True,key=lambda x:x[1])[1:6]
    recommeded_movies=[]
    
    for i in movie_list:
        recommeded_movies.append(movies.iloc[i[0]].title)
        
    return recommeded_movies

name_movie=st.selectbox("Enter the movie name",movies_titles)

if st.button('Recommend'):
    r=recommend(name_movie)
    st.write('The Recommended Movies are :')
    
    for i in r:
        st.write(i)
    
