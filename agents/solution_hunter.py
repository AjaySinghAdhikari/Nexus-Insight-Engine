import os
import sys
import time
import random
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Add root to path for tools
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from tools.web_tool import search_web
from tools.arxiv_tool import search_arxiv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def hunt_solutions(domain: str, essence: str, max_retries: int = 3) -> dict:
    """
    Searches for solutions in a specific domain and extracts the core mechanism.
    
    Args:
        domain (str): The scientific or human domain to search within.
        essence (str): The structural essence of the problem.
        max_retries (int): Maximum number of retries for the LLM call.
        
    Returns:
        dict: A dictionary containing the domain, core mechanism, examples, principles, and sources.
    """
    llm = ChatGroq(model=config.LLM_MODEL, groq_api_key=GROQ_API_KEY)
    
    # 2s wait between domain searches to avoid rate limits on parallel execution
    time.sleep(2)
    
    # Search
    web_results = search_web(f"{domain} solution to {essence}", max_results=3)
    arxiv_results = search_arxiv(f"{domain} {essence}", max_results=2)
    
    all_context = ""
    sources = []
    
    for r in web_results:
        all_context += f"\nSource ({r['url']}): {r['content']}"
        sources.append(r['url'])
    for r in arxiv_results:
        all_context += f"\nArXiv ({r['url']}): {r['summary']}"
        sources.append(r['url'])
        
    system_prompt = """You are a technical researcher. Analyze the provided search results to extract how the domain of {domain} 
solves problems with the essence: '{essence}'.

RESPONSE FORMAT (JSON):
- domain: {domain}
- core_mechanism: describing the abstract logic of the solution.
- specific_examples: list of 2-3 real-world examples from this domain.
- key_principle: one sentence capturing the fundamental truth.
- sources: list of source URLs provided.
"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "CONTEXT:\n{context}")
    ])
    
    chain = prompt | llm | JsonOutputParser()
    
    # Retry logic with exponential backoff
    for attempt in range(max_retries):
        try:
            response = chain.invoke({
                "domain": domain,
                "essence": essence,
                "context": all_context[:8000]
            })
            return response
        except Exception as e:
            if "rate_limit" in str(e).lower() and attempt < max_retries - 1:
                wait_time = (2 ** attempt) + random.random()
                print(f"Rate limited. Retrying in {wait_time:.2f}s...")
                time.sleep(wait_time)
                continue
            print(f"Error in Solution Hunter for {domain}: {e}")
            break
            
    return {
        "domain": domain,
        "core_mechanism": "Failed to extract mechanism.",
        "specific_examples": [],
        "key_principle": "N/A",
        "sources": sources
    }

if __name__ == "__main__":
    print(hunt_solutions("Epidemiology", "Exponential propagation of harmful entities in a network"))
