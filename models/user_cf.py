import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def get_user_based_recommendations(user_id, ratings, movies, top_n=10):
    user_movie_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating')
    user_similarity = cosine_similarity(user_movie_matrix.fillna(0))
    user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)
    
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:]
    top_users = similar_users.head(10).index
    top_users_ratings = ratings[ratings['userId'].isin(top_users)]
    
    recommended_movies = top_users_ratings.groupby('movieId')['rating'].mean().sort_values(ascending=False).head(top_n)
    recommended_movies = recommended_movies.reset_index()
    recommended_movies = recommended_movies.merge(movies, on='movieId')
    
    return recommended_movies[['title', 'rating']]
