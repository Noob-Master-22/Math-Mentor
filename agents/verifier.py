import json
import re
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langgraph.types import interrupt
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)


def verifier_node(state: dict) -> dict:
    prompt = f"""You are a math solution verifier. Check this solution carefully.
Return ONLY a valid JSON object:

{{
  "confident": true or false,
  "confidence_level": "high" or "medium" or "low",
  "issues": ["list any issues found, empty list if none"],
  "verdict": "one sentence summary"
}}

Problem: {state["parsed_problem"].get("problem_text", "")}
Solution: {state["solution"]}"""

    response = llm.invoke([HumanMessage(content=prompt)])
    text = re.sub(r"```json|```", "", response.content).strip()

    try:
        verification = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        verification = json.loads(match.group()) if match else {
            "confident": True,
            "confidence_level": "medium",
            "issues": [],
            "verdict": "Could not verify"
        }

    trace = state.get("agent_trace", [])
    trace.append({"agent": "Verifier", "output": f"Confidence: {verification.get('confidence_level')} | {verification.get('verdict', '')}"})
    

    
    if not verification.get("confident", True):
        human_input = interrupt({
            "reason": "low_confidence",
            "solution": state["solution"],
            "issues": verification.get("issues", [])
        })
        return {
            "solution": human_input.get("edited_solution", state["solution"]),
            "verification": verification,
            "hitl_required": True,
            "agent_trace": trace
        }

    return {"verification": verification, "agent_trace": trace}
