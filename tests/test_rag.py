from rag.chunker import chunk_text
from rag.embedder import create_embeddings
from rag.vector_store import create_faiss_index
from rag.retriever import retrieve_chunks
from llm.llm_service import generate_answer

text = """
Ai help to improves agriculture
how Machine learning improve agriculture sector
Artificial intelligence is transforming agriculture
"""
# chunk text
chunks = chunk_text(text)

# create embeddings
embeddings = create_embeddings(chunks)

#create vector db
index = create_faiss_index(embeddings)

# user query
query =  "how Ai helps in agriculture ?"

# retrieve chunks
result = retrieve_chunks(query,index,chunks)

# LLM answer
answer = generate_answer(query,retrieve_chunks)

print(result)