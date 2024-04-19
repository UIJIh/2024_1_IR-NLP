import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

class BooleanModel:
    def __init__(self, documents):
        self.index = {}
        self.documents = documents
        self.build_index()

    def build_index(self):
        for doc_id, document in enumerate(self.documents):
            for word in document['article'].split():
                if word in self.index:
                    self.index[word].add(doc_id)
                else:
                    self.index[word] = {doc_id}

    def search(self, query):
        query_words = query.split()
        result = None
        for word in query_words:
            if word in self.index:
                if result is None:
                    result = self.index[word]
                else:
                    result = result.intersection(self.index[word])
            else:
                result = set()
                break
        return result

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d', '', text)
    return ' '.join(word_tokenize(text))

def extract_keywords(article_text, num_clusters=5, num_keywords=5):
    okt = Okt()
    preprocessed_text = preprocess_text(article_text)
    words = okt.pos(preprocessed_text, stem=True)
    nouns = [word for word, pos in words if pos == 'Noun' and len(word) > 1]  # 명사이면서 길이가 1보다 긴 것만 선택
    preprocessed_text = ' '.join(nouns)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([preprocessed_text])

    num_samples = X.shape[0]
    if num_samples < num_clusters:
        num_clusters = num_samples

    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)

    cluster_centers = kmeans.cluster_centers_
    features = vectorizer.get_feature_names_out()
    top_keywords = []
    for cluster_center in cluster_centers:
        top_keyword_indices = cluster_center.argsort()[-num_keywords:][::-1]
        keywords = ['#' + features[int(i)] for i in top_keyword_indices]
        top_keywords.append(keywords)
    return ' '.join([' '.join(keywords) for keywords in top_keywords])