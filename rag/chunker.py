from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text: str):
    text_spilitter = (
       RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 100,
       ) 
    )

    chunks = text_spilitter.split_text(text)

    return chunks