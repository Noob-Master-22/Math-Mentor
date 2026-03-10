from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

def explainer_node(state: dict) -> dict:
    problem = state["parsed_problem"].get("problem_text", state["raw_input"])
    prompt = f"""You are a JEE math explainer.

Explain the solution to: {problem}
Solution to explain: {state['solution']}

Rules:
- Explain ONLY this solution, do not introduce a new problem
- Do NOT cite documents, chunks, or any external source by name
- If a formula is used, explain WHY it applies here
- Keep explanation grounded to the exact problem above."""

    response = llm.invoke([HumanMessage(content=prompt)])

    trace = state.get("agent_trace", [])
    trace.append({"agent": "Explainer", "output": "Step-by-step explanation ready"})

    return {"explanation": response.content, "agent_trace": trace}
