import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import config

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def decompose_problem(problem: str) -> dict:
    """
    Analyzes a user problem to extract its structural essence and matching problem types.
    
    Args:
        problem (str): The raw user problem string.
        
    Returns:
        dict: Decomposed problem structure containing essence, types, and constraints.
    """
    llm = ChatGroq(model=config.LLM_MODEL, groq_api_key=GROQ_API_KEY)
    parser = JsonOutputParser()

    system_prompt = """You are a master of first-principles thinking and structural analysis.
Your task is to strip away the surface details of a problem and identify its deep, mathematical or structural core.

MATCHING PROBLEM TYPES:
Use exactly 3 keywords from this list: [propagation, optimization, balance, emergence, self_organization, feedback, resilience, adaptation, communication, resource_allocation, pattern_formation, conflict_resolution, scaling, repair, navigation]

RESPONSE FORMAT:
You must return a JSON object with these exact keys:
- essence: one sentence describing the mathematical/structural nature of the problem (ignore surface details).
- problem_types: list of 3 matching problem_type keywords.
- constraints: list of key constraints or requirements.
- what_success_looks_like: one sentence describing a successful outcome.
"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{problem}")
    ])

    chain = prompt | llm | parser

    try:
        response = chain.invoke({"problem": problem})
        return response
    except Exception as e:
        print(f"Error in Decomposer: {e}")
        return {}

if __name__ == "__main__":
    test_problem = "How can we prevent the spread of misinformation on social media during a crisis?"
    print(decompose_problem(test_problem))
