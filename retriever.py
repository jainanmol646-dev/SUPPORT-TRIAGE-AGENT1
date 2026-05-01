from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_docs():
    with open("data/socs.txt", "r") as f:
        return f.readlines()


def retrieve_docs(issue, docs):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([issue] + docs)

    similarity = cosine_similarity(vectors[0:1], vectors[1:])
    idx = similarity.argmax()

    return docs[idx], similarity[0][idx]