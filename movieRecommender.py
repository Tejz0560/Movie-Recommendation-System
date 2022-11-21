from pyparsing import col
import streamlit as st
import pickle 
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=9b4ec5669cd8f407d40626d34d31c887'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index
    print(movie_index)
    distances = similarity[movie_index[0]]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies = []
    recommended_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommended_poster

movies_dict = pickle.load(open('D:\\temp\\My_Work\\Movie Recommendation\\movies_dict.pkl','rb'))
similarity = pickle.load(open('D:\\temp\\My_Work\\Movie Recommendation\\similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)
st.title("Movies Recommender System")
selected_movie = st.selectbox("Select the movie you just watched!!!",
movies['title'].values)

if(st.button('Recommend')):
    recommendations,posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])