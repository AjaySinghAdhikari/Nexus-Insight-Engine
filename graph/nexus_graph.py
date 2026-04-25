from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, START, END
import sys
import os

# Add root to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.decomposer import decompose_problem
from agents.domain_mapper import map_domains
from agents.solution_hunter import hunt_solutions
from agents.bridge_builder import build_bridge
from agents.synthesizer import synthesize
from knowledge.domain_ontology import DOMAIN_ONTOLOGY

class NexusState(TypedDict):
    """
    The state object for the Nexus Insight Engine workflow.
    """
    problem: str
    decomposed: Dict[str, Any]
    matched_domains: List[Dict[str, Any]]
    domain_solutions: List[Dict[str, Any]]
    bridges: List[Dict[str, Any]]
    final_report: str
    status: str
    current_step: str
    error: str

def node_decompose(state: NexusState) -> NexusState:
    """Decomposes the input problem into structural essence."""
    print("--- DECOMPOSING PROBLEM ---")
    try:
        decomposed = decompose_problem(state["problem"])
        return {**state, "decomposed": decomposed, "current_step": "decompose", "status": "In Progress"}
    except Exception as e:
        return {**state, "error": f"Decompose error: {str(e)}", "status": "Failed"}

def node_map_domains(state: NexusState) -> NexusState:
    """Maps the essence to technical and scientific domains."""
    print("--- MAPPING DOMAINS ---")
    try:
        matched = map_domains(state["decomposed"], DOMAIN_ONTOLOGY)
        return {**state, "matched_domains": matched, "current_step": "map_domains"}
    except Exception as e:
        return {**state, "error": f"Map domains error: {str(e)}", "status": "Failed"}

def node_hunt_solutions(state: NexusState) -> NexusState:
    """Researches solutions in each matched domain."""
    print("--- HUNTING SOLUTIONS ---")
    solutions = []
    essence = state["decomposed"].get("essence", "")
    for domain_info in state["matched_domains"]:
        domain_name = domain_info["domain_name"]
        try:
            solution = hunt_solutions(domain_name, essence)
            if solution: solutions.append(solution)
        except Exception as e:
            print(f"  Warning: Solution hunt failed for {domain_name}: {e}")
            continue
    return {**state, "domain_solutions": solutions, "current_step": "hunt_solutions"}

def node_build_bridges(state: NexusState) -> NexusState:
    """Generates hypotheses by bridging domain solutions to the original problem."""
    print("--- BUILDING BRIDGES ---")
    bridges = []
    essence = state["decomposed"].get("essence", "")
    for solution in state["domain_solutions"]:
        try:
            bridge = build_bridge(solution, state["problem"], essence)
            if bridge: bridges.append(bridge)
        except Exception as e:
            print(f"  Warning: Bridge building failed for {solution.get('domain')}: {e}")
            continue
    return {**state, "bridges": bridges, "current_step": "build_bridges"}

def node_synthesize(state: NexusState) -> NexusState:
    """Synthesizes all insights into a final report."""
    print("--- SYNTHESIZING FINAL REPORT ---")
    try:
        report = synthesize(state["problem"], state["bridges"], state["decomposed"])
        return {**state, "final_report": report, "current_step": "synthesize", "status": "Completed"}
    except Exception as e:
        return {**state, "error": f"Synthesis error: {str(e)}", "status": "Failed"}

def create_nexus_graph():
    """Compiles the LangGraph state machine."""
    workflow = StateGraph(NexusState)
    workflow.add_node("decompose", node_decompose)
    workflow.add_node("map_domains", node_map_domains)
    workflow.add_node("hunt_solutions", node_hunt_solutions)
    workflow.add_node("build_bridges", node_build_bridges)
    workflow.add_node("synthesize", node_synthesize)
    workflow.add_edge(START, "decompose")
    workflow.add_edge("decompose", "map_domains")
    workflow.add_edge("map_domains", "hunt_solutions")
    workflow.add_edge("hunt_solutions", "build_bridges")
    workflow.add_edge("build_bridges", "synthesize")
    workflow.add_edge("synthesize", END)
    return workflow.compile()

def run_nexus(problem: str) -> NexusState:
    """Runs the full Nexus workflow for a given problem."""
    initial_state: NexusState = {"problem": problem, "decomposed": {}, "matched_domains": [], "domain_solutions": [], "bridges": [], "final_report": "", "status": "Starting", "current_step": "start", "error": ""}
    try:
        graph = create_nexus_graph()
        return graph.invoke(initial_state)
    except Exception as e:
        initial_state.update({"error": str(e), "status": "Failed"})
        return initial_state

if __name__ == "__main__":
    result = run_nexus("How to prevent urban traffic congestion using biology?")
    print(result.get("final_report", "No report generated."))
