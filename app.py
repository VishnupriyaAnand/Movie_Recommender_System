import pickle
import streamlit as st
import requests
import pandas as pd


# Function to fetch movie poster
def fetch_poster(movie_id):
    api_key = "53c9ee80a1a4f583fcc98050bc4968b3"  # Ensure your API key is correct
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        poster_path = data.get('poster_path', None)
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_path
        else:
            print(f"No poster path found for movie ID {movie_id}")
            return "https://via.placeholder.com/500x750?text=No+Image+Available"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Request+Error"


# Function to recommend movies
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

        recommended_movie_names = []
        recommended_movie_posters = []

        for i in distances[1:6]:
            # Fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            poster = fetch_poster(movie_id)
            recommended_movie_posters.append(poster)
            recommended_movie_names.append(movies.iloc[i[0]].title)
            print(f"Recommended movie: {movies.iloc[i[0]].title}, Poster URL: {poster}")

        return recommended_movie_names, recommended_movie_posters
    except IndexError as e:
        print(f"Error in recommend function: {e}")
        return [], []


# Streamlit application layout
st.header('Movie Recommender System')
st.text('as of August 2024, the TMDB API has been banned in India, which has blocked the interface to reach the posters')
# Load the movie dictionary and similarity matrix
movies = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Convert movies to DataFrame if not already
if not isinstance(movies, pd.DataFrame):
    movies = pd.DataFrame(movies)

# Ensure 'title' is in movies
if 'title' not in movies.columns:
    st.error("Movie data does not contain 'title' column.")
else:
    movie_list = movies['title'].tolist()

    # Selectbox for movie selection
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    # Recommend button
    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        if not recommended_movie_names:
            st.write("No recommendations available.")
        else:
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.text(recommended_movie_names[0])
                st.image(recommended_movie_posters[0])

            with col2:
                st.text(recommended_movie_names[1])
                st.image(recommended_movie_posters[1])

            with col3:
                st.text(recommended_movie_names[2])
                st.image(recommended_movie_posters[2])

            with col4:
                st.text(recommended_movie_names[3])
                st.image(recommended_movie_posters[3])

            with col5:
                st.text(recommended_movie_names[4])
                st.image(recommended_movie_posters[4])
