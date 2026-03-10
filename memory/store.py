import os
import json
import streamlit as st
import numpy as np
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from pymongo import MongoClient
from tools.embeddings import get_embeddings


load_dotenv()

IST = timezone(timedelta(hours=5, minutes=30))
embeddings_model = get_embeddings()





def get_collection():
    # Try st.secrets first (Streamlit Cloud), fallback to .env (local)
    try:
        uri = st.secrets["MONGODB_URI"]
    except Exception:
        uri = os.getenv("MONGODB_URI")
    
    client = MongoClient(uri)
    return client["math_mentor"]["memory"]

def get_ist_time():
    return datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S IST")

def save_interaction(problem_text: str, solution: str, feedback: str = "", evaluation: dict = {}):
    col = get_collection()
    if not col.find_one({"problem": problem_text}):
        emb = embeddings_model.embed_query(problem_text)
        col.insert_one({
            "problem": problem_text,
            "solution": solution,
            "feedback": feedback,
            "evaluation": evaluation,
            "embedding": emb,
            "timestamp": get_ist_time()
        })

def update_feedback(problem_text: str, feedback: str):
    col = get_collection()
    col.update_one({"problem": problem_text}, {"$set": {"feedback": feedback}})

def find_similar(problem_text: str, threshold: float = 0.75):
    col = get_collection()
    rows = list(col.find({}))
    if not rows:
        return None

    query_emb = np.array(embeddings_model.embed_query(problem_text))
    best_match, best_score = None, 0.0

    for row in rows:
        stored_emb = np.array(row["embedding"])
        score = np.dot(query_emb, stored_emb) / (
            np.linalg.norm(query_emb) * np.linalg.norm(stored_emb)
        )
        if score > best_score:
            best_score = score
            best_match = {
                "problem": row["problem"],
                "solution": row["solution"],
                "feedback": row.get("feedback", ""),
                "evaluation": row.get("evaluation", {}),
                "similarity": round(float(score), 3)
            }

    return best_match if best_score >= threshold else None

def get_all_interactions():
    col = get_collection()
    return [
        {
            "id": str(r["_id"]), "problem": r["problem"],
            "solution": r["solution"], "feedback": r.get("feedback", ""),
            "evaluation": r.get("evaluation", {}), "timestamp": r["timestamp"]
        }
        for r in col.find({}, {"embedding": 0}).sort("timestamp", -1)
    ]
