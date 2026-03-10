from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import json
import re

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def guardrail_node(state: dict) -> dict:
    problem = state.get("raw_input", "")

    prompt = f"""You are an input guardrail for a JEE math tutor app.

Your ONLY job is to block inputs that are clearly NOT math-related.

Respond with JSON only:
{{
  "is_valid": true or false,
  "reason": "one sentence explanation",
  "category": "math" or "non-math" or "harmful" or "unclear"
}}

Mark is_valid as TRUE for:
- Any math problem (algebra, calculus, probability, statistics, geometry, linear algebra)
- ANY difficulty level — JEE mains, JEE advanced, basic, advanced, olympiad
- Word problems involving math (cards, dice, balls, trains etc.)
- Problems with numbers, equations, variables, formulas
- Even if phrased informally or unclearly

Mark is_valid as FALSE ONLY for:
- Completely non-math topics (history, geography, general knowledge, coding, recipes)
- Harmful or abusive content
- Completely empty or gibberish input with no math intent

When in doubt — mark as TRUE. Do not over-restrict.

Input: {problem}"""

    response = llm.invoke([HumanMessage(content=prompt)])
    raw = response.content.strip()
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    result = json.loads(match.group()) if match else {"is_valid": True, "reason": "parse error", "category": "math"}

    trace = state.get("agent_trace", [])
    trace.append({
        "agent": "Guardrail",
        "output": f"Category: {result['category']} | Valid: {result['is_valid']} | {result['reason']}"
    })

    return {
        "guardrail_passed": result["is_valid"],
        "guardrail_reason": result.get("reason", ""),
        "agent_trace": trace
    }
