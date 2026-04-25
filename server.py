import json
import asyncio
from fastapi import FastAPI, Request, Body
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import sys

# Load environment variables
load_dotenv()

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from graph.nexus_graph import create_nexus_graph, NexusState

app = FastAPI(title="NEXUS API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from the 'frontend' directory
if not os.path.exists("frontend"):
    os.makedirs("frontend")
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
async def read_index():
    return FileResponse("frontend/index.html")

@app.post("/api/research")
async def research(request: Request):
    data = await request.json()
    problem = data.get("problem")
    
    if not problem:
        return {"error": "No problem provided"}

    async def event_generator():
        graph = create_nexus_graph()
        initial_state = {
            "problem": problem,
            "decomposed": {},
            "matched_domains": [],
            "domain_solutions": [],
            "bridges": [],
            "final_report": "",
            "status": "Starting",
            "current_step": "start",
            "error": ""
        }
        
        # Mapping graph nodes to user-friendly steps
        step_mapping = {
            "decompose": "Analyzing Problem Structure",
            "map_domains": "Mapping Knowledge Domains",
            "hunt_solutions": "Hunting Cross-Domain Solutions",
            "build_bridges": "Synthesizing Bridge Hypotheses",
            "synthesize": "Generating Final Insight Report"
        }

        # Use graph.stream to get updates
        # Note: LangGraph invoke/stream can be sync or async. 
        # The current implementation in nexus_graph.py is sync.
        # We run it in a thread to avoid blocking the event loop.
        
        loop = asyncio.get_event_loop()
        
        def run_graph():
            return graph.stream(initial_state, stream_mode="updates")

        # Stream the updates
        final_state = initial_state
        
        # Initial event
        yield f"data: {json.dumps({'step': 'start', 'status': 'Starting Research...'})}\n\n"
        
        # We use a wrapper to run the generator in a thread or just iterate if it's fast
        # For LangGraph stream, it yields dicts like {'node_name': {state_updates}}
        for update in graph.stream(initial_state, stream_mode="updates"):
            node_name = list(update.keys())[0]
            state_update = update[node_name]
            final_state.update(state_update)
            
            yield f"data: {json.dumps({'step': node_name, 'status': step_mapping.get(node_name, node_name)})}\n\n"
            # Small delay for visual effect
            await asyncio.sleep(0.5)

        # Final state event
        yield f"data: {json.dumps({'step': 'complete', 'status': 'Research Complete', 'state': final_state})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
