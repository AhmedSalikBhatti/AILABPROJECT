def get_item_based_recommendations(movie_id, ratings, movies):
    from sklearn.metrics.pairwise import cosine_similarity
    import pandas as pd

    # Create a pivot table
    movie_user_matrix = ratings.pivot_table(index='movieId', columns='userId', values='rating').fillna(0)

    # Compute similarity
    cosine_sim = cosine_similarity(movie_user_matrix)
    similarity_df = pd.DataFrame(cosine_sim, index=movie_user_matrix.index, columns=movie_user_matrix.index)

    # Get most similar movies
    if movie_id not in similarity_df:
        return pd.Series(dtype='float64')

    similar_scores = similarity_df[movie_id].sort_values(ascending=False)[1:11]
    return similar_scores
