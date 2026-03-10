from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from rag.retriever import get_retriever
from memory.store import find_similar, save_interaction
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)


def solver_node(state: dict) -> dict:
    problem = state["parsed_problem"].get("problem_text", state["raw_input"])

    
    memory_match = find_similar(problem)
    memory_hint = ""
    memory_note = "No similar past problem found"

    if memory_match:
        memory_hint = (
            f"A similar problem was solved before:\n"
            f"Problem: {memory_match['problem']}\n"
            f"Solution approach: {memory_match['solution'][:400]}\n"
            f"Student feedback: {memory_match['feedback'] or 'none yet'}"
        )
        memory_note = f"Memory match found (similarity: {memory_match['similarity']})"

    
    retriever = get_retriever()
    docs = retriever.invoke(problem)
    chunks = [
        {"source": d.metadata.get("source", "kb"), "text": d.page_content}
        for d in docs
    ]

    # Build context block — ONLY use as formula reference
    if chunks:
        context_block = f"""Use the following ONLY as a formula/concept reference:
{chr(10).join([d['text'] for d in chunks])}

Do NOT solve a problem from the above. Solve ONLY the problem stated below."""
    else:
        context_block = """No reference material was retrieved.
Solve using standard verified math only.
Do NOT cite any source, document, or formula sheet by name."""

    # Memory hint block — use as approach hint only, not as the problem
    memory_block = ""
    if memory_hint:
        memory_block = f"""--- MEMORY HINT (approach reference only) ---
{memory_hint}
Do NOT copy this solution. Adapt the approach to the exact problem below."""


    prompt = f"""You are an expert JEE math tutor.

{context_block}

{memory_block}

Problem to solve: {problem}

Rules:
- Solve EXACTLY the problem above, not any similar or related problem
- Provide a clear numbered step-by-step solution showing all working
- State every formula before using it
- Do NOT reference any document, chunk, or source by name
- Do NOT say "according to the knowledge base" or "as retrieved"
- If unsure of a formula, derive it from first principles instead"""

    response = llm.invoke([HumanMessage(content=prompt)])

    
    save_interaction(problem, response.content)

    trace = state.get("agent_trace", [])
    trace.append({
        "agent": "Solver",
        "output": f"{memory_note} | RAG retrieved {len(chunks)} chunks | Solution generated"
    })

    return {
        "solution": response.content,
        "retrieved_chunks": chunks,
        "memory_hint": memory_hint,
        "agent_trace": trace
    }
