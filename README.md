# NEXUS — Cross-Domain Insight Engine

**NEXUS** is an autonomous cross-disciplinary innovation engine designed to solve complex, high-stakes problems by borrowing structural solutions from unrelated scientific and human domains. Instead of looking at surface-level details, NEXUS identifies the mathematical "essence" of a challenge and maps it to fields like Epidemiology, Mycology, or Swarm Intelligence to generate radical, non-obvious hypotheses.

## How It Works
```text
[ USER PROBLEM ] 
       │
       ▼
[ DECOMPOSER ] ──────► Identifies Structural Essence (e.g., Propagation, Feedback)
       │
       ▼
[ DOMAIN MAPPER ] ────► Matches Essence to 50+ Scientific Domains
       │
       ▼
[ SOLUTION HUNTER ] ──► Researches Domain-Specific breakthrough mechanisms
       │
       ▼
[ BRIDGE BUILDER ] ───► Translates Domain logic into a Novel Hypothesis
       │
       ▼
[ SYNTHESIZER ] ──────► Compiles Final Strategic Report (Markdown/PDF)
```

## Features
- **Analogical Reasoning**: Goes beyond LLM pattern matching by forcing cross-domain synthesis.
- **50+ Scientific Domains**: Hardcoded ontology including Glaciology, Cybernetics, Mycorrhizal Networks, and more.
- **Deep Research**: Real-time academic search via ArXiv and web intelligence via Tavily.
- **Visual Workflow**: Real-time progress monitoring through a premium "Deep Space" web interface.
- **SSE Streaming**: Live updates from the LangGraph agent directly to the browser.
- **Strategic Scoring**: Automatically ranks solutions based on Novelty vs. Feasibility.

## Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-000000?style=for-the-badge&logo=chroma&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-f55036?style=for-the-badge&logo=groq&logoColor=white)

## Getting Started
1. **Clone the repo**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Environment**: Create a `.env` file and add:
   ```env
   GROQ_API_KEY=your_key_here
   TAVILY_API_KEY=your_key_here
   ```
4. **Launch NEXUS**:
   ```bash
   python server.py
   ```
5. **Access the UI**: Open your browser and navigate to `http://localhost:8000`.

*(Note: The legacy Streamlit dashboard is still available in `app/streamlit_app.py`)*

## Example Inputs
1. **Input**: "How do we stop misinformation spreading?"
   - **Output**: An "Immune System" approach using contact-tracing logic from Epidemiology.
2. **Input**: "How can we make urban transport more efficient?"
   - **Output**: A "Slime Mold" decentralized routing algorithm inspired by *Physarum polycephalum*.
3. **Input**: "How do we reduce employee burnout?"
   - **Output**: A "Forest Ecology" strategy based on nutrient-sharing mycorrhizal networks.

## Project Structure
```text
nexus-insight-engine/
├── agents/           # Specialized LLM nodes
├── knowledge/        # Domain ontology & vector store
├── graph/            # LangGraph workflow orchestrator
├── tools/            # Web, ArXiv, and Semantic Search tools
├── app/              # Streamlit dashboard
├── .env              # Secrets (ignored)
├── config.py         # Global settings
└── requirements.txt  # Dependencies
```

## Why This Is Different From ChatGPT
While ChatGPT can "act like an expert," it is limited by the patterns it has seen in its training data. **NEXUS** uses a deliberate **analogical reasoning** pipeline. It *forces* the AI to move away from the problem space (e.g., Marketing) and look into a foreign space (e.g., Oceanography). By finding structural isomorphisms between these fields, NEXUS uncovers solutions that standard LLM prompts would never reach because they lack the "structural leap" mechanism.
