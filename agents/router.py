from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import re
import json

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def router_node(state: dict) -> dict:
    topic = state.get("topic", "algebra")
    trace = state.get("agent_trace", [])
    trace.append({"agent": "Router", "output": f"Routing to {topic} solver"})
    return {"topic": topic, "agent_trace": trace}
