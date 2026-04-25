"""
The Domain Ontology is the core knowledge base of the Nexus Insight Engine.
It maps diverse scientific, artistic, and engineering domains to the structural
problems they are uniquely suited to solve.
"""

PROBLEM_TYPE_DESCRIPTIONS = {
    "propagation": "The spread of information, energy, or entities through a medium or network.",
    "optimization": "Finding the most efficient or effective solution among a vast set of possibilities.",
    "balance": "Maintaining equilibrium or stability within a system under changing conditions.",
    "emergence": "Complex global patterns arising from simple local interactions without central control.",
    "self-organization": "The process where a system's internal organization increases without external guidance.",
    "feedback": "Processes where the output of a system is circled back as input, driving stability or change.",
    "resilience": "The capacity of a system to absorb disturbance and reorganize while undergoing change.",
    "adaptation": "The ability of a system to change its state or behavior in response to environmental shifts.",
    "communication": "The exchange of information between entities to coordinate behavior or transfer data.",
    "resource_allocation": "The distribution of limited assets or energy among competing needs or agents.",
    "pattern_formation": "The development of complex, repetitive structures or behaviors from uniform beginnings.",
    "conflict_resolution": "The process of reaching agreement or settling disputes between competing agents.",
    "scaling": "How system properties change as the system grows in size or complexity.",
    "repair": "The ability of a system to detect and fix internal damage or errors.",
    "navigation": "Determining and following a path through a physical or conceptual space to a goal."
}

DOMAIN_ONTOLOGY = {
    "Epidemiology": {
        "problem_types": ["propagation", "feedback", "resilience"],
        "famous_solutions": ["SIR Models", "Contact Tracing", "Herd Immunity Thresholds"],
        "keywords": ["contagion", "pathogen", "outbreak", "transmission", "R0"]
    },
    "Immunology": {
        "problem_types": ["repair", "adaptation", "communication"],
        "famous_solutions": ["Clonal Selection", "Antibody Diversity", "MHC Recognition"],
        "keywords": ["antigen", "leukocyte", "pathogen-recognition", "cytokines", "memory-cells"]
    },
    "Ecology": {
        "problem_types": ["balance", "resilience", "resource_allocation"],
        "famous_solutions": ["Trophic Cascades", "Keystone Species", "Nutrient Cycling"],
        "keywords": ["biodiversity", "niche", "biomass", "carrying-capacity", "symbiosis"]
    },
    "Mycorrhizal Networks": {
        "problem_types": ["communication", "resource_allocation", "resilience"],
        "famous_solutions": ["The Wood Wide Web", "Source-Sink Dynamics", "Interspecies Signaling"],
        "keywords": ["fungal-hyphae", "symbiotic-exchange", "nutrient-transfer", "rhizosphere"]
    },
    "Ant Colony Optimization": {
        "problem_types": ["optimization", "navigation", "self-organization"],
        "famous_solutions": ["Pheromone Trail Logic", "Stigmergy", "Shortest Path Discovery"],
        "keywords": ["swarm-intelligence", "metaheuristics", "collective-decision-making", "agents"]
    },
    "Evolutionary Biology": {
        "problem_types": ["adaptation", "optimization", "emergence"],
        "famous_solutions": ["Natural Selection", "Genetic Drift", "Adaptive Radiation"],
        "keywords": ["fitness-landscape", "mutation", "selection-pressure", "genotype", "phenotype"]
    },
    "Neuroscience": {
        "problem_types": ["communication", "pattern_formation", "repair"],
        "famous_solutions": ["Neural Plasticity", "Hebbian Learning", "Synaptic Pruning"],
        "keywords": ["neuron", "synapse", "neurotransmitters", "connectome", "signal-transduction"]
    },
    "Jazz Improvisation": {
        "problem_types": ["emergence", "communication", "conflict_resolution"],
        "famous_solutions": ["Call and Response", "Real-time Adaptation", "Modal Interaction"],
        "keywords": ["syncopation", "harmonic-progression", "solo", "ensemble-dynamics"]
    },
    "Urban Planning": {
        "problem_types": ["resource_allocation", "scaling", "optimization"],
        "famous_solutions": ["Zoning Laws", "Transit-Oriented Development", "Green Belts"],
        "keywords": ["infrastructure", "density", "land-use", "public-transit", "walkability"]
    },
    "Thermodynamics": {
        "problem_types": ["balance", "scaling", "feedback"],
        "famous_solutions": ["Entropy Maximization", "Carnot Cycle", "Phase Transitions"],
        "keywords": ["heat-transfer", "equilibrium", "enthalpy", "thermal-efficiency"]
    },
    "Fluid Dynamics": {
        "problem_types": ["propagation", "pattern_formation", "scaling"],
        "famous_solutions": ["Navier-Stokes Equations", "Reynolds Number", "Turbulence Modeling"],
        "keywords": ["viscosity", "vortex", "laminar-flow", "boundary-layer", "aerodynamics"]
    },
    "Materials Science": {
        "problem_types": ["resilience", "scaling", "repair"],
        "famous_solutions": ["Alloying", "Crystal Lattice Structures", "Composite Materials"],
        "keywords": ["tensile-strength", "ductility", "nanostructures", "polymerization"]
    },
    "Game Theory": {
        "problem_types": ["conflict_resolution", "optimization", "communication"],
        "famous_solutions": ["Nash Equilibrium", "Prisoner's Dilemma", "Zero-Sum Games"],
        "keywords": ["strategy", "payoff-matrix", "cooperation", "utility-function"]
    },
    "Cryptography": {
        "problem_types": ["communication", "scaling", "conflict_resolution"],
        "famous_solutions": ["Public Key Infrastructure", "Blockchains", "Zero-Knowledge Proofs"],
        "keywords": ["encryption", "decryption", "hashing", "protocol", "security"]
    },
    "Architecture": {
        "problem_types": ["balance", "optimization", "pattern_formation"],
        "famous_solutions": ["Load Bearing Structures", "Geodesic Domes", "Modular Construction"],
        "keywords": ["structural-integrity", "aesthetics", "spatial-organization", "ergonomics"]
    },
    "Aviation": {
        "problem_types": ["navigation", "scaling", "resilience"],
        "famous_solutions": ["Fly-by-Wire Systems", "Air Traffic Control", "Checklist Manifesto"],
        "keywords": ["avionics", "lift", "drag", "thrust", "flight-envelope"]
    },
    "Supply Chain": {
        "problem_types": ["resource_allocation", "optimization", "propagation"],
        "famous_solutions": ["Just-In-Time Manufacturing", "Bullwhip Effect Mitigation", "Logistics Hubs"],
        "keywords": ["inventory-management", "procurement", "distribution", "lead-time"]
    },
    "Linguistics": {
        "problem_types": ["pattern_formation", "communication", "emergence"],
        "famous_solutions": ["Universal Grammar", "Phonological Rules", "Semantic Networks"],
        "keywords": ["syntax", "morphology", "phonetics", "etymology", "discourse"]
    },
    "Music Theory": {
        "problem_types": ["pattern_formation", "balance", "mathematical_modeling"],
        "famous_solutions": ["Counterpoint", "Equal Temperament", "Harmonic Series"],
        "keywords": ["melody", "rhythm", "interval", "chord-substitution"]
    },
    "Archaeology": {
        "problem_types": ["navigation", "pattern_formation", "resource_allocation"],
        "famous_solutions": ["Stratigraphy", "Radiocarbon Dating", "GIS Mapping"],
        "keywords": ["excavation", "artifact", "cultural-strata", "provenance"]
    },
    "Oceanography": {
        "problem_types": ["propagation", "resource_allocation", "balance"],
        "famous_solutions": ["Thermohaline Circulation", "Ocean Current Modeling", "Marine Protected Areas"],
        "keywords": ["salinity", "bathymetry", "upwelling", "pelagic-zone"]
    },
    "Climatology": {
        "problem_types": ["feedback", "scaling", "balance"],
        "famous_solutions": ["Carbon Cycle Models", "Albedo Effect Feedback", "Climate Sensitivity"],
        "keywords": ["greenhouse-effect", "precipitation", "radiative-forcing", "paleoclimate"]
    },
    "Slime Mold Biology": {
        "problem_types": ["navigation", "optimization", "resource_allocation"],
        "famous_solutions": ["Bio-inspired Network Design", "Pulse-based Signaling", "Decentralized Pathfinding"],
        "keywords": ["Physarum-polycephalum", "protoplasmic-streaming", "spatial-memory"]
    },
    "Swarm Intelligence": {
        "problem_types": ["emergence", "self-organization", "optimization"],
        "famous_solutions": ["Particle Swarm Optimization", "Flocking Algorithms", "Distributed Task Allocation"],
        "keywords": ["agents", "local-rules", "decentralization", "collective-behavior"]
    },
    "Forest Ecology": {
        "problem_types": ["resilience", "resource_allocation", "communication"],
        "famous_solutions": ["Succession Theory", "Gap Dynamics", "Mother Tree Hypothesis"],
        "keywords": ["canopy", "understory", "mycelium", "biodiversity-hotspots"]
    },
    "Embryology": {
        "problem_types": ["pattern_formation", "self-organization", "scaling"],
        "famous_solutions": ["Morphogenetic Fields", "Hox Gene Regulation", "Cell Differentiation"],
        "keywords": ["blastocyst", "gastrulation", "organogenesis", "stem-cells"]
    },
    "Crystallography": {
        "problem_types": ["pattern_formation", "balance", "scaling"],
        "famous_solutions": ["Bragg's Law", "Unit Cell Theory", "X-ray Diffraction"],
        "keywords": ["lattice", "symmetry", "periodicity", "miller-indices"]
    },
    "Origami Mathematics": {
        "problem_types": ["optimization", "scaling", "pattern_formation"],
        "famous_solutions": ["Kawasaki's Theorem", "Huzita-Hatori Axioms", "Rigid Folding"],
        "keywords": ["crease-pattern", "tessellation", "deployable-structures"]
    },
    "Byzantine Fault Tolerance": {
        "problem_types": ["conflict_resolution", "resilience", "communication"],
        "famous_solutions": ["Practical BFT", "Paxos Algorithm", "Consensus Protocols"],
        "keywords": ["distributed-systems", "fault-model", "consistency", "replication"]
    },
    "Biomimicry": {
        "problem_types": ["adaptation", "optimization", "resilience"],
        "famous_solutions": ["Velcro", "Sharkskin Surfaces", "Bullet Train Aerodynamics"],
        "keywords": ["bio-inspiration", "functional-morphology", "sustainable-design"]
    },
    "Soil Science": {
        "problem_types": ["resource_allocation", "balance", "repair"],
        "famous_solutions": ["Cation Exchange Capacity", "Soil Horizons", "Humification"],
        "keywords": ["pedogenesis", "microbiome", "nutrient-fixation", "erosion-control"]
    },
    "Plate Tectonics": {
        "problem_types": ["propagation", "balance", "pattern_formation"],
        "famous_solutions": ["Continental Drift", "Sea Floor Spreading", "Subduction Zones"],
        "keywords": ["lithosphere", "mantle-convection", "seismicity", "fault-lines"]
    },
    "Behavioral Economics": {
        "problem_types": ["optimization", "feedback", "conflict_resolution"],
        "famous_solutions": ["Nudge Theory", "Prospect Theory", "Loss Aversion"],
        "keywords": ["heuristics", "cognitive-bias", "choice-architecture", "irrationality"]
    },
    "Military Strategy": {
        "problem_types": ["navigation", "resource_allocation", "conflict_resolution"],
        "famous_solutions": ["Combined Arms", "OODA Loop", "Logistics-First Strategy"],
        "keywords": ["tactics", "maneuver", "deterrence", "command-and-control"]
    },
    "Firefighting": {
        "problem_types": ["propagation", "resilience", "resource_allocation"],
        "famous_solutions": ["Fire Triangle Management", "Incident Command System", "Containment Lines"],
        "keywords": ["combustion", "suppression", "hazmat", "situational-awareness"]
    },
    "Maritime Navigation": {
        "problem_types": ["navigation", "optimization", "communication"],
        "famous_solutions": ["Great Circle Routing", "Dead Reckoning", "Celestial Navigation"],
        "keywords": ["nautical-charts", "tides", "currents", "waypoint"]
    },
    "Beekeeping": {
        "problem_types": ["self-organization", "resource_allocation", "communication"],
        "famous_solutions": ["Waggle Dance", "Swarm Consensus", "Temperature Regulation"],
        "keywords": ["apis", "pheromone", "foraging", "colony-health"]
    },
    "Mycology": {
        "problem_types": ["propagation", "repair", "resource_allocation"],
        "famous_solutions": ["Mycoremediation", "Enzymatic Decomposition", "Hyphal Network Optimization"],
        "keywords": ["fungi", "spores", "decomposition", "symbiosis"]
    },
    "Glaciology": {
        "problem_types": ["balance", "scaling", "propagation"],
        "famous_solutions": ["Ice Core Analysis", "Glacial Flow Modeling", "Mass Balance Equations"],
        "keywords": ["ablation", "accumulation", "ice-sheet", "calving"]
    },
    "Acoustics": {
        "problem_types": ["propagation", "pattern_formation", "feedback"],
        "famous_solutions": ["Reverberation Control", "Active Noise Cancellation", "Wave Interference"],
        "keywords": ["frequency", "resonance", "diffraction", "reflection"]
    },
    "Cybernetics": {
        "problem_types": ["feedback", "communication", "balance"],
        "famous_solutions": ["Circular Causal Loops", "Homeostasis", "Viable System Model"],
        "keywords": ["control-theory", "system-dynamics", "entropy", "regulation"]
    },
    "Social Network Analysis": {
        "problem_types": ["propagation", "emergence", "communication"],
        "famous_solutions": ["Strength of Weak Ties", "Structural Holes", "Centrality Measures"],
        "keywords": ["graph-theory", "clustering", "influence", "homophily"]
    },
    "Complexity Science": {
        "problem_types": ["emergence", "self-organization", "scaling"],
        "famous_solutions": ["Edge of Chaos", "Fractal Scaling Laws", "Agent-Based Modeling"],
        "keywords": ["non-linearity", "phase-transition", "attractors", "power-laws"]
    },
    "Demography": {
        "problem_types": ["scaling", "resource_allocation", "propagation"],
        "famous_solutions": ["Demographic Transition", "Malthusian Trap", "Population Pyramids"],
        "keywords": ["fertility", "mortality", "migration", "census"]
    },
    "Microbiology": {
        "problem_types": ["adaptation", "propagation", "communication"],
        "famous_solutions": ["Quorum Sensing", "Horizontal Gene Transfer", "Bacterial Chemotaxis"],
        "keywords": ["biofilm", "plasmid", "motility", "metabolism"]
    },
    "Seismology": {
        "problem_types": ["propagation", "pattern_formation", "resilience"],
        "famous_solutions": ["Richter Scale", "Moment Magnitude Scale", "Seismic Tomography"],
        "keywords": ["hypocenter", "epicenter", "body-waves", "surface-waves"]
    },
    "Gastronomy": {
        "problem_types": ["pattern_formation", "balance", "optimization"],
        "famous_solutions": ["Maillard Reaction Optimization", "Flavor Pairing Theory", "Sous-vide Precision"],
        "keywords": ["culinary-arts", "molecular-gastronomy", "organoleptic", "fermentation"]
    },
    "Nanotechnology": {
        "problem_types": ["scaling", "self-organization", "repair"],
        "famous_solutions": ["Carbon Nanotubes", "Molecular Assembly", "Quantum Dots"],
        "keywords": ["nanoscale", "surface-area-to-volume", "self-assembly"]
    },
    "Robotics": {
        "problem_types": ["navigation", "feedback", "optimization"],
        "famous_solutions": ["SLAM (Simultaneous Localization and Mapping)", "PID Control", "Inverse Kinematics"],
        "keywords": ["actuator", "sensor-fusion", "autonomy", "path-planning"]
    },
    "Genealogy": {
        "problem_types": ["pattern_formation", "navigation", "communication"],
        "famous_solutions": ["Pedigree Collapse", "DNA Matching", "Lineage Reconstruction"],
        "keywords": ["ancestry", "haplogroup", "pedigree", "archive"]
    },
    "Topology": {
        "problem_types": ["pattern_formation", "scaling", "optimization"],
        "famous_solutions": ["Poincaré Conjecture", "Knot Theory", "Euler Characteristic"],
        "keywords": ["homeomorphism", "manifolds", "continuity", "compactness"]
    }
}

def get_domains_by_problem_type(problem_type: str) -> list:
    """
    Returns a list of domain names that are associated with a specific problem type.
    
    Args:
        problem_type (str): The structural problem type to filter by.
        
    Returns:
        list: Names of domains that specialize in that problem type.
    """
    return [
        domain for domain, data in DOMAIN_ONTOLOGY.items()
        if problem_type.lower() in [pt.lower() for pt in data["problem_types"]]
    ]

if __name__ == "__main__":
    # Quick test
    test_type = "propagation"
    domains = get_domains_by_problem_type(test_type)
    print(f"Domains solving '{test_type}': {', '.join(domains)}")
