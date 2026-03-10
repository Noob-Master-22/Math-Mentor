def router_node(state: dict) -> dict:
    topic = state.get("topic", "algebra")
    trace = state.get("agent_trace", [])
    trace.append({"agent": "Router", "output": f"Routing to {topic} solver"})
    return {"topic": topic, "agent_trace": trace}
