from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict, Optional
from tools.image_parser import extract_math_from_image
from tools.audio_parser import extract_math_from_audio 

class MathState(TypedDict):
    raw_input: str
    input_type: str       
    image_bytes: bytes   
    audio_bytes: Optional[bytes] 
    parsed_problem: dict       # output of parser agent
    topic: str                 # algebra | calculus | probability | linear_algebra
    retrieved_chunks: list     # RAG results
    solution: str              # solver output
    verification: dict         # {confident: bool, confidence_level: str, issues: list}
    explanation: str           # explainer output
    evaluation: dict           # evaluator output
    guardrail_passed: bool     # guardrail bool
    guardrail_reason: str      # guardrail reason
    memory_hint: str           # similar past problem if found
    hitl_required: bool        # whether human review is needed
    agent_trace: list          # list of {agent, output} dicts for UI
    
def input_processor_node(state: dict) -> dict:
    """Handles image/audio → text conversion before Parser runs"""
    if state["input_type"] == "image" and state.get("image_bytes"):
        extracted, low_confidence = extract_math_from_image(state["image_bytes"])
        trace = state.get("agent_trace", [])
        trace.append({
            "agent": "Input Processor",
            "output": f"Image OCR complete | Low confidence: {low_confidence}"
        })
        return {
            "raw_input": extracted,
            "hitl_required": low_confidence,
            "agent_trace": trace
        }
    elif state["input_type"] == "audio" and state.get("audio_bytes"): 
        extracted, low_confidence = extract_math_from_audio(state["audio_bytes"])
        trace = state.get("agent_trace", [])
        trace.append({
            "agent": "Input Processor",
            "output": f"Audio transcription complete | Low confidence: {low_confidence}"
        })
        return {
            "raw_input": extracted,
            "hitl_required": low_confidence,
            "agent_trace": trace
        }

    return state 

def create_graph():
    from agents.parser import parser_node
    from agents.router import router_node
    from agents.solver import solver_node
    from agents.verifier import verifier_node
    from agents.explainer import explainer_node
    from agents.guardrail import guardrail_node      
    from agents.evaluator import evaluator_node      

    builder = StateGraph(MathState)

    builder.add_node("input_processor", input_processor_node)
    builder.add_node("guardrail", guardrail_node)    
    builder.add_node("parser", parser_node)
    builder.add_node("router", router_node)
    builder.add_node("solver", solver_node)
    builder.add_node("verifier", verifier_node)
    builder.add_node("explainer", explainer_node)
    builder.add_node("evaluator", evaluator_node)    

    builder.set_entry_point("input_processor")
    builder.add_edge("input_processor", "guardrail") 
    builder.add_conditional_edges(                   
        "guardrail",
        lambda state: "parser" if state.get("guardrail_passed", True) else END
    )
    builder.add_edge("parser", "router")
    builder.add_edge("router", "solver")
    builder.add_edge("solver", "verifier")
    builder.add_edge("verifier", "explainer")
    builder.add_edge("explainer", "evaluator")       
    builder.add_edge("evaluator", END)               

    return builder.compile(checkpointer=MemorySaver())



