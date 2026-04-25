import arxiv
import datetime

def search_arxiv(query: str, max_results: int = 3) -> list[dict]:
    """
    Searches ArXiv for academic papers and returns structured results.
    
    Args:
        query (str): The research query.
        max_results (int): Maximum number of results to return.
        
    Returns:
        list[dict]: A list of papers with title, authors, summary, url, and date.
    """
    try:
        client = arxiv.Client()
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )

        results = []
        for result in client.results(search):
            results.append({
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "summary": result.summary.replace("\n", " "),
                "url": result.pdf_url,
                "published_date": result.published.strftime("%Y-%m-%d")
            })
        return results
    except Exception as e:
        print(f"Error during ArXiv search: {e}")
        return []

if __name__ == "__main__":
    # Test search
    papers = search_arxiv("swarm intelligence in urban logistics", max_results=2)
    for p in papers:
        print(f"Title: {p['title']}\nPublished: {p['published_date']}\n")
