from tavily import TavilyClient
from config import TAVILY_API_KEY

client = TavilyClient(api_key=TavilyClient)

def search_web(query):
    response = client.search(
        query = query,
        max_results = 6,
        search_depth="advanced"
    )

    results = response["results"]

    return results