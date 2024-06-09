# import pandas as pd
# from transformers import AutoModel, AutoTokenizer
# import torch
# import torch.nn.functional as F
# import numpy as np

# class TransformerModel:
#     def __init__(self, script_list, title_list):
#         self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#         self.tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
#         self.model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
#         self.model.to(self.device)
#         self.script_list = script_list
#         self.title_list = title_list
#         self.script_embeddings = None
#         self.script_embedding()

#     def script_embedding(self):        
#         script_encodings = self.tokenizer(self.script_list, truncation=True, padding=True, max_length=128, return_tensors='pt')
#         script_encodings = {key: val.to(self.device) for key, val in script_encodings.items()}
        
#         if 'token_type_ids' in script_encodings:
#             del script_encodings['token_type_ids']

#         with torch.no_grad():
#             script_outputs = self.model(**script_encodings)
#             self.script_embeddings = self.mean_pooling(script_outputs, script_encodings['attention_mask'])

#     def mean_pooling(self, model_output, attention_mask):
#         token_embeddings = model_output[0]
#         input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
#         return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

#     def find_similar_movies(self, query, threshold=0.2):
#         query_encoding = self.tokenizer(query, truncation=True, padding=True, max_length=128, return_tensors='pt')
#         query_encoding = {key: val.to(self.device) for key, val in query_encoding.items()}

#         if 'token_type_ids' in query_encoding:
#             del query_encoding['token_type_ids']

#         with torch.no_grad():
#             query_output = self.model(**query_encoding)
#             query_embedding = self.mean_pooling(query_output, query_encoding['attention_mask'])

#         def cosine_similarity(a, b):
#             return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

#         script_embeddings_np = self.script_embeddings.cpu().numpy()
#         query_embedding_np = query_embedding.cpu().numpy()
#         similarity_scores = np.array([cosine_similarity(query_embedding_np[0], script_embedding) for script_embedding in script_embeddings_np])

#         # Sorting indices based on similarity scores
#         sorted_indices = np.argsort(similarity_scores)[::-1]

#         # Filtering based on threshold
#         filtered_indices = sorted_indices[similarity_scores[sorted_indices] > threshold]

#         similar_movies = [self.title_list[i] for i in filtered_indices]
        
#         return similar_movies

import torch
import torch.nn.functional as F
import numpy as np
from transformers import AutoModel, AutoTokenizer

class TransformerModel:
    def __init__(self, script_list, title_list):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        # Hugging Face Hub 경로
        repo_name = "Uiji/movie-search-query-finetuned-all-MiniLM-L6-v2"
        model_name_or_path = repo_name

        # 모델과 토크나이저 로드
        self.model = AutoModel.from_pretrained(model_name_or_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

        self.model.to(self.device)
        self.model.eval()

        self.script_list = script_list
        self.title_list = title_list
        self.script_embeddings = None
        self.script_embedding()

    def script_embedding(self):        
        script_encodings = self.tokenizer(self.script_list, truncation=True, padding=True, max_length=128, return_tensors='pt')
        script_encodings = {key: val.to(self.device) for key, val in script_encodings.items()}
        
        if 'token_type_ids' in script_encodings:
            del script_encodings['token_type_ids']

        with torch.no_grad():
            script_outputs = self.model(**script_encodings)
            self.script_embeddings = self.mean_pooling(script_outputs, script_encodings['attention_mask'])

    def mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def find_similar_movies(self, query, threshold=0.9962): 
        query_encoding = self.tokenizer(query, truncation=True, padding=True, max_length=128, return_tensors='pt')
        query_encoding = {key: val.to(self.device) for key, val in query_encoding.items()}

        if 'token_type_ids' in query_encoding:
            del query_encoding['token_type_ids']

        with torch.no_grad():
            query_output = self.model(**query_encoding)
            query_embedding = self.mean_pooling(query_output, query_encoding['attention_mask'])

        def cosine_similarity(a, b):
            return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

        script_embeddings_np = self.script_embeddings.cpu().numpy()
        query_embedding_np = query_embedding.cpu().numpy()
        similarity_scores = np.array([cosine_similarity(query_embedding_np[0], script_embedding) for script_embedding in script_embeddings_np])

        # Sorting indices based on similarity scores
        sorted_indices = np.argsort(similarity_scores)[::-1]

        # Filtering based on threshold
        filtered_indices = sorted_indices[similarity_scores[sorted_indices] > threshold]
        #print(len(filtered_indices))
        similar_movies = [self.title_list[i] for i in filtered_indices]
        
        return similar_movies