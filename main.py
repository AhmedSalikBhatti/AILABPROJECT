from models.user_cf import get_user_based_recommendations
from models.item_cf import get_item_based_recommendations
from utils.data_loader import load_data

ratings, movies = load_data()

def get_recommendations(user_id):
    user_recs = get_user_based_recommendations(user_id, ratings)
    item_recs = get_item_based_recommendations(user_id, ratings)
    return user_recs.head(10), item_recs.head(10)
