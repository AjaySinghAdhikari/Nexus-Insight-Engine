import sys
print("Starting imports")
try:
    print("Importing agents.decomposer")
    from agents.decomposer import decompose_problem
    print("Importing agents.domain_mapper")
    from agents.domain_mapper import map_domains
    print("Importing agents.solution_hunter")
    from agents.solution_hunter import hunt_solutions
    print("Importing agents.bridge_builder")
    from agents.bridge_builder import build_bridge
    print("Importing agents.synthesizer")
    from agents.synthesizer import synthesize
    print("Importing knowledge.domain_ontology")
    from knowledge.domain_ontology import DOMAIN_ONTOLOGY
    print("Done importing all")
except Exception as e:
    print("Error:", e)
print("Finished script")
