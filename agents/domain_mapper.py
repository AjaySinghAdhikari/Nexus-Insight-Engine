import os
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Add root to path for tools
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from tools.semantic_search import SemanticSearcher

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def map_domains(decomposed: dict, ontology: dict) -> list[dict]:
    """
    Maps a decomposed problem to relevant domains using semantic similarity and LLM reasoning.
    
    Args:
        decomposed (dict): The decomposed problem structure.
        ontology (dict): The DOMAIN_ONTOLOGY dictionary.
        
    Returns:
        list[dict]: Top 5 matching domains with explanations.
    """
    llm = ChatGroq(model=config.LLM_MODEL, groq_api_key=GROQ_API_KEY)
    searcher = SemanticSearcher()
    
    essence = decomposed.get("essence", "")
    target_problem_types = set(decomposed.get("problem_types", []))
    
    results = []
    for domain_name, data in ontology.items():
        domain_types = set(data.get("problem_types", []))
        overlap = len(target_problem_types.intersection(domain_types))
        type_score = overlap / 3.0
        
        context_str = f"{' '.join(data.get('famous_solutions', []))} {' '.join(data.get('keywords', []))}"
        semantic_score = searcher.similarity(essence, context_str)
        final_score = (type_score * 0.4) + (semantic_score * 0.6)
        
        results.append({
            "domain_name": domain_name,
            "similarity_score": final_score,
            "matching_problem_types": list(target_problem_types.intersection(domain_types)),
            "domain_data": data
        })
    
    results.sort(key=lambda x: x["similarity_score"], reverse=True)
    top_candidates = results[:10]
    
    final_top_5 = []
    system_prompt = """You are a cross-disciplinary expert. Given a structural problem essence and a domain, 
explain in ONE SENTENCE why this domain's core principles are relevant to solving the problem."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "Problem Essence: {essence}\nDomain: {domain_name}\nDomain Keywords: {keywords}\nWhy relevant?")
    ])
    
    explanation_chain = prompt | llm | StrOutputParser()
    
    for cand in top_candidates[:5]:
        explanation = explanation_chain.invoke({
            "essence": essence,
            "domain_name": cand["domain_name"],
            "keywords": ", ".join(cand["domain_data"]["keywords"])
        })
        final_top_5.append({
            "domain_name": cand["domain_name"],
            "similarity_score": round(cand["similarity_score"], 3),
            "matching_problem_types": cand["matching_problem_types"],
            "why_relevant": explanation.strip()
        })
        
    return final_top_5

if __name__ == "__main__":
    from knowledge.domain_ontology import DOMAIN_ONTOLOGY
    test_decomposed = {
        "essence": "A system where misinformation spreads exponentially through connected nodes via social validation.",
        "problem_types": ["propagation", "feedback", "communication"]
    }
    print(map_domains(test_decomposed, DOMAIN_ONTOLOGY))
