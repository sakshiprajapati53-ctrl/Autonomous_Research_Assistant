import numpy as np

#FAISS vectors NumPy arrays me work karte hai
from rag.embedder import (model)

#Retrieval Function
def retrieve_chunks(query,index,chunks,top_k=3):

    # Query Embedding
    query_embedding = model.encode(
    [query]
)
    # Similarity Search
    distances, indices = index.search(
    query_embedding,
    top_k
)
     # Retrieve matching chunks
    retrieved_chunks = [
        chunks[i]
        for i in indices[0]
    ]

    return retrieved_chunks
