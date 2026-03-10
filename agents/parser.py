import json
import re
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

def parser_node(state: dict) -> dict:
    prompt = f"""You are a math problem parser. Extract and structure this math problem.
Return ONLY a valid JSON object, no extra text, no markdown:

{{
  "problem_text": "the cleaned up problem statement",
  "topic": "algebra or calculus or probability or linear_algebra",
  "variables": ["list of variables used"],
  "constraints": ["any constraints like x > 0"],
  "needs_clarification": false
}}

Set needs_clarification to true only if the problem is genuinely ambiguous or incomplete.

Input: {state['raw_input']}"""

    response = llm.invoke([HumanMessage(content=prompt)])
    text = re.sub(r"```json|```", "", response.content).strip()

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        # Fallback if LLM adds extra text
        match = re.search(r'\{.*\}', text, re.DOTALL)
        parsed = json.loads(match.group()) if match else {
            "problem_text": state["raw_input"],
            "topic": "algebra",
            "variables": [],
            "constraints": [],
            "needs_clarification": False
        }

    trace = state.get("agent_trace", [])
    trace.append({"agent": "Parser", "output": f"Topic: {parsed.get('topic')} | Problem: {parsed.get('problem_text', '')[:80]}"})

    return {
        "parsed_problem": parsed,
        "topic": parsed.get("topic", "algebra"),
        "hitl_required": parsed.get("needs_clarification", False),
        "agent_trace": trace
    }
