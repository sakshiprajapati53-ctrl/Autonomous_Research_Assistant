from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text

text = load_pdf("sample.pdf")
chunks = chunk_text(text)
print(chunks[0])
print(len(chunks))