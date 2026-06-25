from rag.retriever import retrieve_chunks
from tools.web_search import search_web

def researcher_agent(task,index,chunks):
    # PDF retrieval
    retrieve_chunks_results = retrieve_chunks(task,index,chunks)

    # web research
    web_results = search_web(task)
    web_content = []

    for results in web_results:
        web_content.append(results["content"])

    # combine sources
    combined_research = (retrieve_chunks_results +  web_content)

    return combined_research

# Architecture Understanding

#Task
#  ↓
#PDF Retrieval
#  ↓
#Web Search
#  ↓
#Combine Knowledge
#  ↓
#Writer Agent

#SYSTEM LEVEL ARCHITECTURE

#PDFs
#  ↓
#FAISS Retrieval
#  ↓
#Research Agent
#  ↓
#Web Search
#  ↓
#Combined Context
#  ↓
#Critic Agent
#  ↓
#Writer Agent
#  ↓
#Final Research Report