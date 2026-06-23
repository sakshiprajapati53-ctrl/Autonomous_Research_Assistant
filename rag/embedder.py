from sentence_transformers import (SentenceTransformer)

# load all models
model = SentenceTransformer("all-MiniLM-L6-v2")

# embedding fxn
def create_embeddings(chunks):
    embeddings = model.encode(chunks)

    return embeddings

# Why model outside function?
# ans :- Because model loading expensive hota hai.If inside function:
# har request pe reload so it will becomeVery slow.