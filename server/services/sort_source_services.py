from typing import List
from sentence_transformers import SentenceTransformer
import numpy as np
class SortSourceServices:
    def __init__(self):
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    def sort_source(self, query:str, search_results: list[dict]):
         relevant_docs = []
         query_embedding = self.embedding_model.encode([query])

         for res in search_results:
                res_embedding = self.embedding_model.encode([res["content"]])

                similarity = np.dot(query_embedding, res_embedding.T)/(
                np.linalg.norm(query_embedding)*np.linalg.norm(res_embedding)
                )
                res["relevance_score"] = similarity

                if similarity > 0.3:
                    relevant_docs.append(res)

         return sorted(relevant_docs, key=lambda x: x["relevance_score"], reverse=True)

                
                 
        
