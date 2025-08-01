import pickle
import os

# Get the absolute path to the .pkl file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pkl_path = os.path.join(BASE_DIR, 'tfidf_similarity.pkl')

# Load the pickle data using the correct path
with open(pkl_path, 'rb') as f:
    data = pickle.load(f)

cos_sim = data["cos_sim"]
isbn_to_index = data["isbn_to_index"]
books = data["books"]

def recommend_similar_books(isbn, N=20):
    if isbn not in isbn_to_index:
        return []
    idx = isbn_to_index[isbn]
    scores = list(enumerate(cos_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    scores = scores[1:N + 1]
    similar_books = [books.iloc[score[0], 0] for score in scores]
    return similar_books
