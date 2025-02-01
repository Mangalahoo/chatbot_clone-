from typing import List
from sentence_transformers import SentenceTransformer
class SortSourceServices:
    def __init__(self):
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    def sort_source(self, query:str, search_results: list[dict]):
        # sort source

        query_embedding = self.embedding_model.encode([query])
        print(query_embedding)
