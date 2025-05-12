import pandas as pd
from models.item_cf import get_item_based_recommendations
from utils.data_loader import load_data  # make sure this file exists!

ratings, movies = load_data()

def get_recommendations(movie_title):
    # Convert movie title to movieId
    movie_id = movies[movies['title'] == movie_title]['movieId'].values
    if len(movie_id) == 0:
        return []
    movie_id = movie_id[0]

    # Call with all required arguments
    recs = get_item_based_recommendations(movie_id, ratings, movies)

    # Get the recommended movie titles from the movieId list
    recommended_titles = movies[movies['movieId'].isin(recs.index)]['title'].tolist()
    return recommended_titles
