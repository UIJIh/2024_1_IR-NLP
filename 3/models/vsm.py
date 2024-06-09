import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
csv.field_size_limit(100000000)
import os

class VSMModel:
    def __init__(self, script_list, title_list, norm=None):
        self.script_list = script_list
        self.title_list = title_list
        self.vectorizer = TfidfVectorizer(norm=norm)
        self.tfidf_matrix = None
        self.calculate_tfidf()

    def calculate_tfidf(self):
        self.tfidf_matrix = self.vectorizer.fit_transform(self.script_list)
        #print("TF-IDF matrix calculated.")

    def find_reference_script_index(self, query):
        tfidfv1 = TfidfVectorizer(vocabulary=[query], norm=None)
        max_value = 0
        reference_script_index = 0
        array = tfidfv1.fit_transform(self.script_list).toarray()
        for i in range(len(array)):
            if array[i] > max_value:
                max_value = array[i]
                reference_script_index = i
        return reference_script_index
        
    def find_similar_movies(self, query, similarity_threshold=0.25):
        reference_script_index = self.find_reference_script_index(query)
        cosine_sim_matrix = cosine_similarity(self.tfidf_matrix)

        similar_movies = [
            (self.title_list[i], cosine_sim_matrix[reference_script_index][i])
            for i in range(len(self.script_list))
            if cosine_sim_matrix[reference_script_index][i] > similarity_threshold
        ]

        # Sorting similar movies based on cosine similarity score
        similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
        
        # Extracting titles from sorted similar movies
        similar_movie_titles = [title for title, _ in similar_movies]

        return similar_movie_titles