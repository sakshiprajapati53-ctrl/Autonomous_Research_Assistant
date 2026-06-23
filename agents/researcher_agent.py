from rag.retriever import retrieve_chunks

def researcher_agent(task,index,chunks):
    results = retrieve_chunks(task,index,chunks)

    return results