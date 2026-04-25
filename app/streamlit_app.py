import streamlit as st
import sys, os, time, threading
from fpdf import FPDF
import unicodedata
from dotenv import load_dotenv

# Add root to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from graph.nexus_graph import run_nexus

st.set_page_config(
    page_title="NEXUS",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── GLOBAL CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
section.main,
.block-container {
    background: #06060e !important;
    color: #e2e0f0 !important;
    font-family: 'Outfit', sans-serif !important;
}

[data-testid="stAppViewBlockContainer"] {
    padding: 0 2rem 4rem !important;
    max-width: 1100px !important;
    margin: 0 auto !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0b0b18 !important;
    border-right: 1px solid rgba(255,255,255,0.05) !important;
}

/* ── Typography ── */
h1, h2, h3 {
    font-family: 'DM Serif Display', serif !important;
    color: #f0eeff !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 2px; }

/* ── Buttons ── */
.stButton > button {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    background: rgba(255,255,255,0.04) !important;
    color: #c8c5e0 !important;
    padding: 0.5rem 1.2rem !important;
}
.stButton > button:hover {
    background: rgba(138,110,255,0.15) !important;
    border-color: rgba(138,110,255,0.4) !important;
    color: #d4ccff !important;
    transform: translateY(-1px) !important;
}

/* ── Text Input ── */
.stTextArea textarea {
    font-family: 'Outfit', sans-serif !important;
    font-size: 1.05rem !important;
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 12px !important;
    color: #e2e0f0 !important;
    padding: 1rem 1.2rem !important;
    transition: border-color 0.2s !important;
    resize: none !important;
}
.stTextArea textarea:focus {
    border-color: rgba(138,110,255,0.5) !important;
    box-shadow: 0 0 0 3px rgba(138,110,255,0.08) !important;
}
.stTextArea label { display: none !important; }

/* ── Progress bar ── */
[data-testid="stProgress"] > div {
    background: rgba(255,255,255,0.06) !important;
    border-radius: 4px !important;
    height: 3px !important;
}
[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #8a6eff, #c084fc) !important;
    border-radius: 4px !important;
}

/* ── Divider ── */
hr { border-color: rgba(255,255,255,0.06) !important; margin: 2rem 0 !important; }

/* ── Markdown ── */
.stMarkdown p {
    font-family: 'Outfit', sans-serif !important;
    color: #b0adc8 !important;
    line-height: 1.7 !important;
}
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    font-family: 'DM Serif Display', serif !important;
    color: #f0eeff !important;
    margin: 1.5rem 0 0.75rem !important;
}
.stMarkdown h2 { font-size: 1.4rem !important; }
.stMarkdown h3 { font-size: 1.15rem !important; }
.stMarkdown ul, .stMarkdown ol {
    color: #b0adc8 !important;
    padding-left: 1.4rem !important;
    line-height: 1.9 !important;
}
.stMarkdown code {
    font-family: 'DM Mono', monospace !important;
    background: rgba(138,110,255,0.12) !important;
    color: #c084fc !important;
    padding: 2px 6px !important;
    border-radius: 4px !important;
    font-size: 0.85em !important;
}
.stMarkdown blockquote {
    border-left: 3px solid rgba(138,110,255,0.5) !important;
    padding-left: 1rem !important;
    color: #9895b5 !important;
    font-style: italic !important;
}

/* ── Expander ── */
[data-testid="stExpander"] {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 12px !important;
    margin-bottom: 0.75rem !important;
    overflow: hidden !important;
}
[data-testid="stExpander"]:hover {
    border-color: rgba(138,110,255,0.25) !important;
}
[data-testid="stExpanderToggleIcon"] { color: #8a6eff !important; }
details summary {
    font-family: 'Outfit', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    color: #d4d0f0 !important;
    padding: 1rem 1.2rem !important;
}
details[open] summary {
    border-bottom: 1px solid rgba(255,255,255,0.06) !important;
}
details > div {
    padding: 1rem 1.2rem !important;
}

/* ── Metric ── */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 12px !important;
    padding: 1rem 1.25rem !important;
}
[data-testid="stMetricLabel"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.7rem !important;
    color: #6b6888 !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
}
[data-testid="stMetricValue"] {
    font-family: 'DM Serif Display', serif !important;
    font-size: 1.8rem !important;
    color: #c084fc !important;
}

/* ── Spinner ── */
[data-testid="stSpinner"] { color: #8a6eff !important; }

/* ── Columns gap ── */
[data-testid="column"] { padding: 0 0.4rem !important; }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ────────────────────────────────────────────────────────────
if "report"       not in st.session_state: st.session_state.report       = None
if "bridges"      not in st.session_state: st.session_state.bridges      = []
if "domains"      not in st.session_state: st.session_state.domains      = []
if "decomposed"   not in st.session_state: st.session_state.decomposed   = {}
if "history"      not in st.session_state: st.session_state.history      = []
if "running"      not in st.session_state: st.session_state.running      = False
if "topic"        not in st.session_state: st.session_state.topic        = ""
if "step"         not in st.session_state: st.session_state.step         = 0

# ── HELPERS ──────────────────────────────────────────────────────────────────
def check_env():
    """
    Validates that the necessary API keys are present in the environment.
    """
    load_dotenv()
    missing = []
    if not os.getenv("GROQ_API_KEY"):    missing.append("GROQ_API_KEY")
    if not os.getenv("TAVILY_API_KEY"):  missing.append("TAVILY_API_KEY")
    return missing

def score_color(score: float) -> str:
    """
    Returns a CSS color hex code based on a score from 0.0 to 1.0.
    """
    if score >= 0.85: return "#7ee8a2"
    if score >= 0.70: return "#c084fc"
    return "#f9a875"

def render_score_badge(label: str, value, color: str = "#c084fc"):
    """
    Renders a custom HTML badge for scores.
    """
    return f"""
    <span style="
        display:inline-flex; align-items:center; gap:5px;
        background:rgba(255,255,255,0.04);
        border:1px solid rgba(255,255,255,0.08);
        border-radius:20px; padding:3px 10px;
        font-family:'DM Mono',monospace; font-size:0.72rem;
        color:{color}; margin-right:6px;">
        {label}&nbsp;<strong style="color:{color}">{value}</strong>
    </span>"""

# ── HEADER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 3.5rem 0 2.5rem; text-align:center; position:relative;">

  <div style="
    position:absolute; top:0; left:50%; transform:translateX(-50%);
    width:600px; height:300px;
    background: radial-gradient(ellipse at center, rgba(138,110,255,0.08) 0%, transparent 70%);
    pointer-events:none;">
  </div>

  <p style="
    font-family:'DM Mono',monospace; font-size:0.72rem;
    color:#6b6888; letter-spacing:3px; text-transform:uppercase;
    margin-bottom:1rem;">
    Cross-Domain Insight Engine
  </p>

  <h1 style="
    font-family:'DM Serif Display',serif; font-size:5rem;
    font-weight:400; color:#f0eeff; line-height:1;
    margin-bottom:1rem; letter-spacing:-2px;">
    NEXUS
  </h1>

  <p style="
    font-family:'Outfit',sans-serif; font-size:1.1rem;
    color:#7b78a0; max-width:520px; margin:0 auto; line-height:1.7;">
    Give it a problem. It searches all of human knowledge —<br>
    from <em style="color:#a89ee8">immunology</em> to
    <em style="color:#a89ee8">jazz</em> to
    <em style="color:#a89ee8">forest ecology</em> —<br>
    and returns solutions you would never think to look for.
  </p>

</div>
""", unsafe_allow_html=True)

# ── ENV CHECK ────────────────────────────────────────────────────────────────
missing_keys = check_env()
if missing_keys:
    st.markdown(f"""
    <div style="
        background:rgba(249,168,117,0.06); border:1px solid rgba(249,168,117,0.2);
        border-radius:12px; padding:1.2rem 1.5rem; margin-bottom:2rem;">
        <p style="font-family:'DM Mono',monospace; font-size:0.8rem;
                  color:#f9a875; margin-bottom:0.4rem; letter-spacing:1px;">
            ⚠ &nbsp;SETUP REQUIRED
        </p>
        <p style="color:#b0adc8; font-size:0.9rem; margin:0;">
            Add <code style="color:#f9a875">{" &nbsp;·&nbsp; ".join(missing_keys)}</code>
            to your <code>.env</code> file to get started.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ── EXAMPLE CHIPS ────────────────────────────────────────────────────────────
EXAMPLES = [
    "How do we stop misinformation spreading?",
    "How can cities reduce loneliness?",
    "How do we make habits stick?",
    "How do we prevent hospital errors?",
    "How do we make education engaging?",
    "How do we reduce traffic congestion?",
]

st.markdown("""
<p style="font-family:'DM Mono',monospace; font-size:0.7rem;
          color:#4e4c6a; text-transform:uppercase; letter-spacing:2px;
          margin-bottom:0.6rem;">
  Try an example
</p>
""", unsafe_allow_html=True)

cols = st.columns(len(EXAMPLES))
for i, ex in enumerate(EXAMPLES):
    with cols[i]:
        short = ex.replace("How do we ", "").replace("How can ", "").rstrip("?").capitalize()
        if st.button(short, key=f"chip_{i}", use_container_width=True):
            st.session_state.topic = ex
            st.rerun()

# ── INPUT ────────────────────────────────────────────────────────────────────
st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

# Use session state to manage the value to avoid Streamlit widgets error
if 'topic' not in st.session_state:
    st.session_state.topic = ""

problem_input = st.text_area(
    "problem",
    value=st.session_state.topic,
    placeholder="Describe your problem here — the harder and more complex the better...",
    height=100,
    key="problem_text",
    label_visibility="collapsed",
)

st.markdown("<div style='height:0.75rem'></div>", unsafe_allow_html=True)

col_run, col_clear, col_spacer = st.columns([2, 1, 7])
with col_run:
    run_btn = st.button("✦  Run NEXUS", use_container_width=True, type="primary",
                        disabled=st.session_state.running or bool(missing_keys))
with col_clear:
    if st.button("Clear", use_container_width=True):
        st.session_state.report     = None
        st.session_state.bridges    = []
        st.session_state.domains    = []
        st.session_state.decomposed = {}
        st.session_state.topic      = ""
        st.session_state.step       = 0
        st.rerun()

# ── PIPELINE STEPS ───────────────────────────────────────────────────────────
STEPS = [
    ("🧬", "Decompose",       "Finding the structural essence"),
    ("🗺",  "Map Domains",     "Searching all fields of knowledge"),
    ("🔍", "Hunt Solutions",  "Researching each domain's approach"),
    ("🌉", "Build Bridges",   "Translating solutions to your problem"),
    ("✦",  "Synthesize",      "Writing your insight report"),
]

def render_pipeline(active: int = -1):
    """
    Renders a custom HTML pipeline visualization for the workflow progress.
    """
    items = ""
    for i, (icon, name, desc) in enumerate(STEPS):
        if i < active:
            state_color = "#7ee8a2"
            dot = f"<span style='color:#7ee8a2;font-size:0.7rem'>✓</span>"
            opacity = "1"
        elif i == active:
            state_color = "#c084fc"
            dot = f"<span style='color:#c084fc;font-size:1rem;animation:pulse 1s infinite'>{icon}</span>"
            opacity = "1"
        else:
            state_color = "#2a2840"
            dot = f"<span style='color:#3a3858;font-size:0.9rem'>{icon}</span>"
            opacity = "0.4"

        connector = ""
        if i < len(STEPS) - 1:
            conn_color = "#7ee8a2" if i < active else ("#c084fc" if i == active else "#1e1c30")
            connector = f"""
            <div style="flex:1; height:1px; background:{conn_color};
                        margin: 0 0.5rem; opacity:0.6; align-self:center;
                        transition:background 0.4s;"></div>"""

        items += f"""
        <div style="display:flex; flex-direction:column; align-items:center;
                    gap:6px; opacity:{opacity}; transition:opacity 0.3s; min-width:80px;">
            <div style="width:38px; height:38px; border-radius:50%;
                        background:rgba(255,255,255,0.03);
                        border:1px solid {state_color}30;
                        display:flex; align-items:center; justify-content:center;">
                {dot}
            </div>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem;
                      color:{state_color}; text-align:center; letter-spacing:0.5px;
                      margin:0; line-height:1.3;">
                {name}
            </p>
        </div>
        {connector}"""

    return f"""
    <style>
    @keyframes pulse {{ 0%,100%{{opacity:1}} 50%{{opacity:0.4}} }}
    </style>
    <div style="
        display:flex; align-items:center; justify-content:space-between;
        background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.06);
        border-radius:16px; padding:1.2rem 1.5rem; margin:1.5rem 0;">
        {items}
    </div>"""

# ── RUN ──────────────────────────────────────────────────────────────────────
if run_btn and problem_input.strip():
    st.session_state.running = True
    st.session_state.topic   = problem_input.strip()
    st.session_state.report  = None
    st.session_state.bridges = []
    st.session_state.domains = []

    pipeline_slot = st.empty()
    status_slot   = st.empty()
    progress_slot = st.empty()

    step_names = ["decompose", "map_domains", "hunt_solutions", "build_bridges", "synthesize"]

    try:
        from graph.nexus_graph import run_nexus

        # We can't easily stream and update from run_nexus if it's a simple graph.invoke.
        # But we can simulate the progress for visual flair as it moves through nodes.
        # However, the graph.invoke is synchronous.
        # For true real-time updates, we would use graph.stream().
        # I will use graph.stream() here.
        
        from graph.nexus_graph import create_nexus_graph
        graph = create_nexus_graph()
        current_state = {
            "problem": problem_input.strip(),
            "decomposed": {}, "matched_domains": [], "domain_solutions": [],
            "bridges": [], "final_report": "", "status": "Starting", "current_step": "start", "error": ""
        }
        
        i = 0
        for output in graph.stream(current_state):
            node_name = list(output.keys())[0]
            current_state.update(output[node_name])
            
            pipeline_slot.markdown(render_pipeline(i), unsafe_allow_html=True)
            progress_slot.progress((i + 1) / len(STEPS))
            status_slot.markdown(f"""
            <p style="font-family:'DM Mono',monospace; font-size:0.75rem;
                      color:#8a6eff; text-align:center; margin:0.5rem 0 1rem;">
                {STEPS[i][2]}...
            </p>""", unsafe_allow_html=True)
            i += 1
            if i >= len(STEPS): break

        pipeline_slot.markdown(render_pipeline(len(STEPS)), unsafe_allow_html=True)
        progress_slot.progress(1.0)
        status_slot.markdown("""
        <p style="font-family:'DM Mono',monospace; font-size:0.75rem;
                  color:#7ee8a2; text-align:center; margin:0.5rem 0 1rem;">
            ✓ &nbsp;Complete
        </p>""", unsafe_allow_html=True)

        st.session_state.report     = current_state.get("final_report", "")
        st.session_state.bridges    = current_state.get("bridges", [])
        st.session_state.domains    = current_state.get("matched_domains", [])
        st.session_state.decomposed = current_state.get("decomposed", {})
        st.session_state.history.insert(0, {
            "problem": problem_input.strip(),
            "report":  current_state.get("final_report", ""),
        })

    except Exception as e:
        pipeline_slot.empty()
        status_slot.empty()
        progress_slot.empty()
        st.markdown(f"""
        <div style="background:rgba(226,75,74,0.06); border:1px solid rgba(226,75,74,0.2);
                    border-radius:12px; padding:1.2rem 1.5rem; margin:1rem 0;">
            <p style="font-family:'DM Mono',monospace; font-size:0.75rem;
                      color:#e24b4a; margin-bottom:0.4rem;">⚠ Error</p>
            <p style="color:#b0adc8; font-size:0.9rem; margin:0;">{str(e)}</p>
        </div>
        """, unsafe_allow_html=True)

    finally:
        st.session_state.running = False

# ── RESULTS ──────────────────────────────────────────────────────────────────
if st.session_state.report:

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Essence block ──
    if st.session_state.decomposed:
        ess  = st.session_state.decomposed.get("essence", "")
        ptypes = st.session_state.decomposed.get("problem_types", [])
        tags = "".join([
            f"<span style='background:rgba(138,110,255,0.1);border:1px solid rgba(138,110,255,0.2);"
            f"border-radius:20px;padding:2px 10px;font-size:0.72rem;color:#a89ee8;"
            f"font-family:DM Mono,monospace;margin-right:6px'>{t}</span>"
            for t in ptypes
        ])
        st.markdown(f"""
        <div style="margin:1.5rem 0 2rem; padding:1.4rem 1.6rem;
                    background:rgba(138,110,255,0.04);
                    border:1px solid rgba(138,110,255,0.12);
                    border-radius:14px;">
            <p style="font-family:'DM Mono',monospace; font-size:0.68rem;
                      color:#6b6888; text-transform:uppercase; letter-spacing:2px;
                      margin-bottom:0.7rem;">Structural Essence</p>
            <p style="font-family:'DM Serif Display',serif; font-size:1.25rem;
                      color:#d4d0f0; margin-bottom:0.9rem; line-height:1.5; font-style:italic;">
                "{ess}"
            </p>
            <div>{tags}</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Domain cards ──
    if st.session_state.domains:
        st.markdown("""
        <p style="font-family:'DM Mono',monospace; font-size:0.7rem;
                  color:#4e4c6a; text-transform:uppercase; letter-spacing:2px;
                  margin-bottom:0.9rem;">
            Analogous domains found
        </p>
        """, unsafe_allow_html=True)

        n = len(st.session_state.domains)
        cols = st.columns(min(n, 5))
        for i, d in enumerate(st.session_state.domains[:5]):
            with cols[i]:
                score = d.get("similarity_score", 0)
                pct   = int(score * 100) if score <= 1 else int(score)
                bar_w = pct
                sc    = score_color(score / 100 if score > 1 else score)
                st.markdown(f"""
                <div style="background:rgba(255,255,255,0.02);
                            border:1px solid rgba(255,255,255,0.07);
                            border-radius:12px; padding:1rem;
                            text-align:center; height:100%;">
                    <p style="font-family:'DM Serif Display',serif;
                              font-size:1.05rem; color:#d4d0f0;
                              margin-bottom:0.5rem; line-height:1.3;">
                        {d.get('domain_name','—')}
                    </p>
                    <div style="background:rgba(255,255,255,0.05);
                                border-radius:4px; height:3px; margin-bottom:0.5rem;">
                        <div style="width:{bar_w}%; height:3px;
                                    background:{sc}; border-radius:4px;"></div>
                    </div>
                    <p style="font-family:'DM Mono',monospace; font-size:0.7rem;
                              color:{sc}; margin:0;">{pct}%</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

    # ── Bridge hypotheses ──
    if st.session_state.bridges:
        st.markdown("""
        <p style="font-family:'DM Mono',monospace; font-size:0.7rem;
                  color:#4e4c6a; text-transform:uppercase; letter-spacing:2px;
                  margin:1.5rem 0 0.9rem;">
            Cross-domain insights
        </p>
        """, unsafe_allow_html=True)

        for b in st.session_state.bridges:
            title    = b.get("hypothesis_title", "Insight")
            inspired = b.get("inspired_by", "Unknown")
            insight  = b.get("core_insight", "")
            steps    = b.get("concrete_steps", [])
            novelty  = b.get("novelty_score", "—")
            feasib   = b.get("feasibility_score", "—")
            transfers = b.get("what_transfers_directly", "")
            breaks    = b.get("where_analogy_breaks_down", "")

            badges = (
                render_score_badge("Novelty", f"{novelty}/10", "#c084fc") +
                render_score_badge("Feasibility", f"{feasib}/10", "#7ee8a2") +
                render_score_badge("From", inspired, "#a89ee8")
            )

            steps_html = "".join([
                f"<li style='margin-bottom:0.5rem;color:#b0adc8;line-height:1.6'>{s}</li>"
                for s in steps
            ]) if steps else ""

            with st.expander(f"✦  {title}"):
                st.markdown(f"""
                <div style="padding:0.2rem 0 0.8rem">
                    <div style="margin-bottom:1rem">{badges}</div>
                    <p style="color:#c8c5e0; font-size:1rem; line-height:1.7;
                              margin-bottom:1.2rem;">{insight}</p>
                    {'<p style="font-family:DM Mono,monospace;font-size:0.68rem;color:#4e4c6a;text-transform:uppercase;letter-spacing:2px;margin-bottom:0.6rem">Concrete Steps</p><ol style=padding-left:1.3rem>' + steps_html + '</ol>' if steps_html else ''}
                    {'<div style="margin-top:1rem;padding:0.8rem 1rem;background:rgba(126,232,162,0.04);border-left:2px solid rgba(126,232,162,0.3);border-radius:0 8px 8px 0"><p style=font-family:DM Mono,monospace;font-size:0.68rem;color:#4e4c6a;text-transform:uppercase;letter-spacing:2px;margin-bottom:0.3rem>What transfers directly</p><p style=color:#9895b5;font-size:0.9rem;margin:0>' + transfers + '</p></div>' if transfers else ''}
                    {'<div style="margin-top:0.6rem;padding:0.8rem 1rem;background:rgba(249,168,117,0.04);border-left:2px solid rgba(249,168,117,0.25);border-radius:0 8px 8px 0"><p style=font-family:DM Mono,monospace;font-size:0.68rem;color:#4e4c6a;text-transform:uppercase;letter-spacing:2px;margin-bottom:0.3rem>Where analogy breaks down</p><p style=color:#9895b5;font-size:0.9rem;margin:0>' + breaks + '</p></div>' if breaks else ''}
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Final Report ──
    st.markdown("""
    <p style="font-family:'DM Mono',monospace; font-size:0.7rem;
              color:#4e4c6a; text-transform:uppercase; letter-spacing:2px;
              margin:1.5rem 0 1rem;">
        Full Report
    </p>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""<div style="background:rgba(255,255,255,0.015);
                        border:1px solid rgba(255,255,255,0.06);
                        border-radius:16px; padding:2rem 2.5rem;">""",
        unsafe_allow_html=True
    )
    st.markdown(st.session_state.report)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── Download ──
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    try:
        def clean(text):
            return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 20)
        pdf.cell(0, 12, "NEXUS — Insight Report", ln=True)
        pdf.set_font("Helvetica", "", 11)
        pdf.set_text_color(100, 100, 120)
        pdf.cell(0, 8, clean(st.session_state.topic), ln=True)
        pdf.ln(4)
        pdf.set_text_color(40, 40, 60)
        pdf.set_font("Helvetica", "", 10)
        for line in st.session_state.report.split("\n"):
            line = clean(line)
            if line.startswith("## "):
                pdf.set_font("Helvetica", "B", 13)
                pdf.ln(4)
                pdf.cell(0, 8, line[3:], ln=True)
                pdf.set_font("Helvetica", "", 10)
            elif line.startswith("### "):
                pdf.set_font("Helvetica", "B", 11)
                pdf.ln(2)
                pdf.cell(0, 7, line[4:], ln=True)
                pdf.set_font("Helvetica", "", 10)
            elif line.strip():
                pdf.multi_cell(0, 6, line)
            else:
                pdf.ln(3)

        pdf_bytes = pdf.output(dest="S")
        if isinstance(pdf_bytes, str):
            pdf_bytes = pdf_bytes.encode("latin-1")

        col_dl, _ = st.columns([2, 8])
        with col_dl:
            st.download_button(
                "↓  Download PDF",
                data=pdf_bytes,
                file_name="nexus_report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    except Exception as e:
        st.error(f"PDF Export failed: {e}")

# ── EMPTY STATE ──────────────────────────────────────────────────────────────
elif not st.session_state.running:
    st.markdown("""
    <div style="text-align:center; padding:3rem 0 2rem; opacity:0.35;">
        <p style="font-family:'DM Serif Display',serif; font-size:1.4rem;
                  color:#6b6888; font-style:italic;">
            "The solution to your problem<br>was solved in a different field 100 years ago."
        </p>
    </div>
    """, unsafe_allow_html=True)

# ── SIDEBAR — History ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <p style="font-family:'DM Mono',monospace; font-size:0.68rem;
              color:#4e4c6a; text-transform:uppercase; letter-spacing:2px;
              margin-bottom:1rem; padding-top:1rem;">
        Session History
    </p>
    """, unsafe_allow_html=True)

    if not st.session_state.history:
        st.markdown("""
        <p style="color:#3a3858; font-size:0.85rem; font-style:italic;">
            No problems run yet.
        </p>
        """, unsafe_allow_html=True)
    else:
        for i, item in enumerate(st.session_state.history[:8]):
            short = item["problem"][:55] + "…" if len(item["problem"]) > 55 else item["problem"]
            if st.button(short, key=f"hist_{i}", use_container_width=True):
                st.session_state.report  = item["report"]
                st.session_state.topic   = item["problem"]
                st.session_state.bridges = []
                st.session_state.domains = []
                st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"""
    <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#2e2c48; text-align:center;">
        {len(st.session_state.history)} problems explored
    </p>
    """, unsafe_allow_html=True)
