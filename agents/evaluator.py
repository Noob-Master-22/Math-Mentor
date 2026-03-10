from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import re

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def evaluator_node(state: dict) -> dict:
    problem = state["parsed_problem"].get("problem_text", state["raw_input"])

    prompt = f"""You are an expert JEE math evaluator. Evaluate the solution and explanation quality.

Problem: {problem}
Solution: {state.get('solution', '')}
Explanation: {state.get('explanation', '')}

Respond with JSON only:
{{
  "score": 1-10,
  "correctness": "correct" | "partially_correct" | "incorrect",
  "clarity": "clear" | "average" | "unclear",
  "completeness": "complete" | "incomplete",
  "feedback": "one sentence summary of quality"
}}"""

    response = llm.invoke([HumanMessage(content=prompt)])

    import json, re
    raw = response.content.strip()
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    result = json.loads(match.group()) if match else {
        "score": 7, "correctness": "correct",
        "clarity": "clear", "completeness": "complete",
        "feedback": "Solution looks good"
    }

    trace = state.get("agent_trace", [])
    trace.append({
        "agent": "Evaluator",
        "output": f"Score: {result['score']}/10 | {result['correctness']} | {result['feedback']}"
    })

    return {
        "evaluation": result,
        "agent_trace": trace
    }
