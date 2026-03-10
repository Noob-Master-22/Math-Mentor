import streamlit as st
from graph import create_graph
from memory.store import save_interaction, update_feedback, get_all_interactions
from tools.image_parser import extract_math_from_image
from tools.audio_parser import extract_math_from_audio
from langgraph.types import Command
import uuid


st.set_page_config(
    page_title="Math Mentor",
    page_icon="📐",
    layout="wide"
)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* { font-family: 'Inter', sans-serif; }

/* ── Background ── */
.stApp { background: #080b14; }
[data-testid="stSidebar"] {
    background: #0d1017 !important;
    border-right: 1px solid #1e2433;
}

/* ── Hide default header decoration ── */
[data-testid="stDecoration"] { display: none; }

/* ── Title area ── */
.main-title {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(120deg, #818cf8, #38bdf8, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
    margin-bottom: 0;
}
.main-subtitle {
    color: #4b5563;
    font-size: 0.9rem;
    margin-top: 2px;
    margin-bottom: 24px;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: #0d1017;
    border: 1px solid #1e2433;
    border-radius: 14px;
    padding: 5px;
    gap: 4px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    padding: 8px 22px;
    font-weight: 600;
    font-size: 0.88rem;
    color: #6b7280;
    border: none !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #818cf8, #38bdf8) !important;
    color: white !important;
}

/* ── Primary Buttons ── */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #818cf8 0%, #38bdf8 100%);
    color: white !important;
    border: none !important;
    border-radius: 12px;
    padding: 10px 28px;
    font-weight: 700;
    font-size: 0.95rem;
    letter-spacing: 0.3px;
    box-shadow: 0 4px 20px rgba(129,140,248,0.3);
    transition: all 0.2s ease;
}
.stButton > button[kind="primary"]:hover {
    box-shadow: 0 6px 28px rgba(129,140,248,0.5);
    transform: translateY(-1px);
}

/* ── Secondary Buttons ── */
.stButton > button[kind="secondary"] {
    background: #1e2433 !important;
    color: #94a3b8 !important;
    border: 1px solid #2d3748 !important;
    border-radius: 12px;
    font-weight: 600;
}

/* ── Text areas ── */
.stTextArea textarea {
    background: #0d1017 !important;
    border: 1px solid #1e2433 !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    font-size: 0.95rem !important;
    line-height: 1.6 !important;
    transition: border 0.2s;
}
.stTextArea textarea:focus {
    border: 1px solid #818cf8 !important;
    box-shadow: 0 0 0 3px rgba(129,140,248,0.15) !important;
}

/* ── Text input ── */
.stTextInput input {
    background: #0d1017 !important;
    border: 1px solid #1e2433 !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
}

/* ── File uploader ── */
[data-testid="stFileUploader"] {
    background: #0d1017;
    border: 2px dashed #1e2433;
    border-radius: 16px;
    padding: 8px;
    transition: border 0.2s;
}
[data-testid="stFileUploader"]:hover {
    border-color: #818cf8;
}

/* ── Metrics ── */
[data-testid="stMetric"] {
    background: #0d1017;
    border: 1px solid #1e2433;
    border-radius: 14px;
    padding: 16px 20px;
}
[data-testid="stMetricLabel"] { color: #6b7280 !important; font-size: 0.8rem !important; }
[data-testid="stMetricValue"] { color: #e2e8f0 !important; font-weight: 700 !important; }

/* ── Expanders ── */
[data-testid="stExpander"] {
    background: #0d1017 !important;
    border: 1px solid #1e2433 !important;
    border-radius: 12px !important;
    overflow: hidden;
}
.streamlit-expanderHeader {
    background: #0d1017 !important;
    color: #94a3b8 !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
}

/* ── Sidebar items ── */
[data-testid="stSidebar"] .stExpander {
    background: #13161f !important;
    border: 1px solid #1e2433 !important;
    border-radius: 10px !important;
    margin-bottom: 6px;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #94a3b8 !important;
    font-size: 0.75rem !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 700 !important;
}

/* ── Info / Warning / Success ── */
[data-testid="stAlert"] { border-radius: 12px !important; }

/* ── Divider ── */
hr { border-color: #1e2433 !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #080b14; }
::-webkit-scrollbar-thumb { background: #1e2433; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">📐 Math Mentor</p>', unsafe_allow_html=True)
st.markdown('<p class="main-subtitle">JEE-style math solver powered by RAG + Multi-Agent AI</p>', unsafe_allow_html=True)



# Initialize session state
if "graph" not in st.session_state:
    st.session_state.graph = create_graph()
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())
if "result" not in st.session_state:
    st.session_state.result = None
if "hitl_pending" not in st.session_state:
    st.session_state.hitl_pending = False
if "hitl_data" not in st.session_state:
    st.session_state.hitl_data = None
if "current_problem" not in st.session_state:
    st.session_state.current_problem = ""


# ── SIDEBAR: Retrieved Context + Memory ──────────────────────────
with st.sidebar:
    st.header("📚 Retrieved Context")
    if st.session_state.result and st.session_state.result.get("retrieved_chunks"):
        for i, chunk in enumerate(st.session_state.result["retrieved_chunks"]):
            with st.expander(f"Chunk {i+1} — {chunk['source'].split('/')[-1]}"):
                st.caption(chunk["source"])
                st.markdown(chunk["text"][:300])
    else:
        st.caption("Retrieved chunks will appear here after solving.")

    st.divider()
    st.header("🧠 Memory")
    memories = get_all_interactions()
    if memories:
        st.caption(f"{len(memories)} problems stored")
        for m in memories[:5]:
            with st.expander(f"{m['problem'][:40]}..."):
                st.caption(f"🕐 {m['timestamp']}")
                st.caption(f"Feedback: {m['feedback'] or 'none'}")
    else:
        st.caption("No past problems yet.")


# ── MAIN: Input Tabs ──────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["📝 Type", "🖼️ Image", "🎙️ Audio", "ℹ️ About"])

with tab1:
    text_input = st.text_area(
        "Type your math problem:",
        placeholder="e.g. Find the roots of x^2 - 5x + 6 = 0",
        height=100
    )
    solve_text = st.button("🔍 Solve", key="solve_text", type="primary")


with tab2:
    uploaded = st.file_uploader(
        "Upload a photo or screenshot of your math problem",
        type=["jpg", "jpeg", "png"]
    )
    if uploaded:
        st.image(uploaded, caption="Uploaded image", width=400)
        image_bytes = uploaded.read()

        with st.spinner("Extracting math from image..."):
            extracted_text, low_conf = extract_math_from_image(image_bytes)

        st.success("Text extracted!")
        edited_text = st.text_area(
            "Extracted text (edit if needed):",
            value=extracted_text,
            height=80
        )
        if low_conf:
            st.warning("Low confidence extraction — please verify the text above")

        solve_image = st.button("Solve", key="solve_image", type="primary")


with tab3:
    st.markdown("**Option 1: Record directly**")
    st.caption("Click the mic button, speak your problem, click stop.")

    audio_input = st.audio_input("🎙️ Record your problem", key="mic_recorder")

    solve_audio = False
    edited_audio_text = ""
    audio_bytes_data = None

    if audio_input:
        # st.audio_input returns WAV — convert to m4a-compatible bytes with correct filename
        audio_bytes_data = audio_input.read()

        with st.spinner("Transcribing..."):
            transcribed_text, low_conf_audio = extract_math_from_audio(
                audio_bytes_data, filename="audio.wav"  
            )

        st.success("Transcribed!")
        edited_audio_text = st.text_area(
            "Transcribed text (edit if needed):",
            value=transcribed_text,
            height=80,
            key="audio_text_live"
        )
        if low_conf_audio:
            st.warning("Low confidence — please verify the text above")

        solve_audio = st.button("🔍 Solve", key="solve_audio_live", type="primary")

    st.divider()
    st.markdown("**Option 2: Upload an m4a file**")

    audio_uploaded = st.file_uploader(
        "Upload your recorded audio",
        type=["m4a"],  
        key="audio_uploader"
    )

    solve_audio_upload = False
    edited_audio_upload_text = ""
    audio_upload_bytes = None

    if audio_uploaded:
        st.audio(audio_uploaded)
        audio_upload_bytes = audio_uploaded.read()
        filename = audio_uploaded.name  

        with st.spinner("Transcribing audio..."):
            transcribed_upload, low_conf_upload = extract_math_from_audio(
                audio_upload_bytes, filename=filename  
            )

        st.success("Audio transcribed!")
        edited_audio_upload_text = st.text_area(
            "Transcribed text (edit if needed):",
            value=transcribed_upload,
            height=80,
            key="audio_text_upload"
        )
        if low_conf_upload:
            st.warning("Low confidence transcription — please verify the text above")

        solve_audio_upload = st.button("🔍 Solve", key="solve_audio_upload", type="primary")


with tab4:
    st.markdown("""
    ## About Math Mentor
    
    An AI-powered JEE math tutor built with:
    - **5 specialized agents** (Parser → Router → Solver → Verifier → Explainer)
    - **RAG pipeline** with curated math knowledge base
    - **Memory layer** that learns from past interactions
    - **Human-in-the-loop** review for low-confidence solutions
    - **Multimodal input** — type, image, or audio (record or upload m4a)
    
    ### Architecture
    ```
    Input → Parser → Router → Solver (RAG + Memory) → Verifier → Explainer
                                                          ↓ (if unsure)
                                                       HITL Review
    ```
    """)


# ── SOLVE LOGIC ───────────────────────────────────────────────────
def run_graph(raw_input, input_type="text", image_bytes=None, audio_bytes=None):
    st.session_state.thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": st.session_state.thread_id}}

    initial_state = {
        "raw_input": raw_input,
        "input_type": input_type,
        "image_bytes": image_bytes or b"",
        "audio_bytes": audio_bytes or b"",
        "agent_trace": [],
        "memory_hint": "",
        "hitl_required": False
    }

    with st.spinner("Agents working..."):
        try:
            result = None
            for event in st.session_state.graph.stream(
                initial_state, config, stream_mode="values"
            ):
                result = event
                if "__interrupt__" in event:
                    st.session_state.hitl_pending = True
                    st.session_state.hitl_data = event["__interrupt__"]
                    st.session_state.result = result
                    return

            st.session_state.result = result
            st.session_state.hitl_pending = False
            st.session_state.current_problem = raw_input

        except Exception as e:
            st.error(f"Error: {str(e)}")


if solve_text and text_input.strip():
    run_graph(text_input.strip(), "text")

if tab2 and uploaded and solve_image and edited_text.strip():
    run_graph(edited_text.strip(), "image", image_bytes=image_bytes)

if solve_audio and edited_audio_text.strip():
    run_graph(edited_audio_text.strip(), "audio", audio_bytes=audio_bytes_data)

if solve_audio_upload and edited_audio_upload_text.strip():
    run_graph(edited_audio_upload_text.strip(), "audio", audio_bytes=audio_upload_bytes)


# ── HITL PANEL ────────────────────────────────────────────────────
if st.session_state.hitl_pending and st.session_state.hitl_data:
    st.divider()
    st.warning("**Human Review Required** — The Verifier is not confident in this solution")

    hitl = st.session_state.hitl_data
    if isinstance(hitl, (list, tuple)):
        hitl = hitl[0].value if hasattr(hitl[0], 'value') else {}

    issues = hitl.get("issues", [])
    if issues:
        st.error("Issues found: " + " | ".join(issues))

    current_solution = hitl.get("solution", "")
    edited_solution = st.text_area(
        "Review and edit the solution:",
        value=current_solution,
        height=200
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Approve & Continue", type="primary"):
            config = {"configurable": {"thread_id": st.session_state.thread_id}}
            with st.spinner("Resuming..."):
                result = st.session_state.graph.invoke(
                    Command(resume={"edited_solution": edited_solution}),
                    config
                )
            st.session_state.result = result
            st.session_state.hitl_pending = False
            st.rerun()

    with col2:
        if st.button("Reject & Re-solve"):
            st.session_state.hitl_pending = False
            st.session_state.result = None
            st.rerun()


# ── RESULTS PANEL ─────────────────────────────────────────────────
if st.session_state.result and not st.session_state.hitl_pending:
    result = st.session_state.result
    st.divider()

    # ── Top metrics row ──
    verification = result.get("verification", {})
    confidence = verification.get("confidence_level", "medium")
    verdict = verification.get("verdict", "")
    topic = result.get("topic", "unknown")
    chunks_count = len(result.get("retrieved_chunks", []))

    col1, col2, col3 = st.columns(3)
    col1.metric("🎯 Topic", topic.capitalize())
    col2.metric("📚 Chunks Retrieved", chunks_count)
    color = {"high": "🟢", "medium": "🟡", "low": "🔴"}.get(confidence, "🟡")
    col3.metric("✅ Confidence", f"{color} {confidence.upper()}")

    if verdict:
        st.caption(f"Verifier: {verdict}")

    if result.get("memory_hint"):
        st.info("🧠 Memory hint was used — similar past problem found")

    st.divider()

    # ── Problem card ── ← THIS IS WHERE YOU ADD IT
    problem_text = result.get("parsed_problem", {}).get("problem_text", "")
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #0d1017, #111827);
        border: 1px solid #1e2433;
        border-left: 4px solid #818cf8;
        border-radius: 14px;
        padding: 18px 22px;
        margin: 16px 0;
        box-shadow: 0 4px 24px rgba(129,140,248,0.08);
    '>
        <span style='color:#818cf8; font-size:0.78rem; font-weight:700; 
                     text-transform:uppercase; letter-spacing:1px;'>📌 Problem</span>
        <p style='color:#e2e8f0; font-size:1.05rem; margin-top:8px; 
                  margin-bottom:0; line-height:1.7;'>{problem_text}</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Explanation ──
    st.subheader("📖 Step-by-Step Explanation")
    st.markdown(result.get("explanation", "No explanation generated"))

    with st.expander("🔧 Raw Solution", expanded=False):
        st.markdown(result.get("solution", ""))

    with st.expander("🔍 Agent Trace", expanded=False):
        for step in result.get("agent_trace", []):
            st.markdown(f"**[{step['agent']}]** {step['output']}")

    # ── Feedback ──
    st.divider()
    st.markdown("**Was this solution helpful?**")
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("✅ Correct"):
            problem = result.get("parsed_problem", {}).get("problem_text", "")
            update_feedback(problem, "correct")
            st.success("Thanks! Saved to memory.")
    with col2:
        feedback_text = st.text_input("Wrong? Tell us what's incorrect:", key="feedback_input")
        if st.button("Submit Feedback") and feedback_text:
            problem = result.get("parsed_problem", {}).get("problem_text", "")
            update_feedback(problem, f"incorrect: {feedback_text}")
            st.warning("Feedback saved. Will improve future answers.")
