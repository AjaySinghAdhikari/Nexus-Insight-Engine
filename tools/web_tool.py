import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_web(query: str, max_results: int = 5) -> list[dict]:
    """
    Performs a web search using Tavily and returns structured results.
    
    Args:
        query (str): The search query.
        max_results (int): Maximum number of results to return.
        
    Returns:
        list[dict]: A list of results with title, url, content, and score.
    """
    if not TAVILY_API_KEY or TAVILY_API_KEY == "your_key_here":
        print("Warning: TAVILY_API_KEY not set. Returning empty results.")
        return []

    try:
        client = TavilyClient(api_key=TAVILY_API_KEY)
        response = client.search(query=query, search_depth="advanced", max_results=max_results)
        
        results = []
        for result in response.get("results", []):
            results.append({
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "content": result.get("content", ""),
                "score": result.get("score", 0.0)
            })
        return results
    except Exception as e:
        print(f"Error during Tavily search: {e}")
        return []

if __name__ == "__main__":
    # Test search (will fail if API key is not valid)
    print(search_web("latest breakthroughs in mycelium networks", max_results=2))
