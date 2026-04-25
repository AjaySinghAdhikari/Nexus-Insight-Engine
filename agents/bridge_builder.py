import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import config

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def build_bridge(domain_solution: dict, original_problem: str, essence: str) -> dict:
    """
    Generates a novel hypothesis for the original problem inspired by a domain solution.
    
    Args:
        domain_solution (dict): The solution mechanism extracted from another domain.
        original_problem (str): The initial problem provided by the user.
        essence (str): The structural essence of the problem.
        
    Returns:
        dict: A novel hypothesis with action steps, novelty, and feasibility scores.
    """
    llm = ChatGroq(model=config.LLM_MODEL, groq_api_key=GROQ_API_KEY)
    
    system_prompt = """You are a world-class visionary and innovation consultant. 
You specialize in 'Trans-Domain Synthesis'—taking a solution from one field and mapping it to a completely different one.

ORIGINAL PROBLEM: {original_problem}
STRUCTURAL ESSENCE: {essence}
DOMAIN INSIGHT: {domain_solution}

TASK:
Generate a concrete, novel hypothesis for solving the original problem using the logic of the domain insight.

RESPONSE FORMAT (JSON):
- hypothesis_title: catch name for the solution.
- inspired_by: domain name.
- core_insight: 2-3 sentences explaining the 'aha!' moment.
- concrete_steps: list of 4-5 actionable steps to implement this.
- what_transfers_directly: logic that fits perfectly.
- what_needs_adaptation: logic that needs modification.
- where_analogy_breaks_down: limits of the comparison.
- novelty_score: 1-10.
- feasibility_score: 1-10.
"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "Build the bridge.")
    ])
    
    chain = prompt | llm | JsonOutputParser()
    
    try:
        return chain.invoke({
            "original_problem": original_problem,
            "essence": essence,
            "domain_solution": domain_solution
        })
    except Exception as e:
        print(f"Error in Bridge Builder: {e}")
        return {}

if __name__ == "__main__":
    test_sol = {
        "domain": "Epidemiology",
        "core_mechanism": "Targeting 'Super-spreaders' with high centrality for isolation.",
        "key_principle": "Network topology determines propagation speed."
    }
    print(build_bridge(test_sol, "Fake news on Twitter", "Propagation in networks"))
