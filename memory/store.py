import sqlite3
import json
import numpy as np
import os
from tools.embeddings import get_embeddings
from datetime import datetime, timezone, timedelta


IST = timezone(timedelta(hours=5, minutes=30))

DB_PATH = "memory/math_memory.db"
embeddings_model = get_embeddings()

def init_db():
    os.makedirs("memory", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            problem     TEXT NOT NULL,
            solution    TEXT NOT NULL,
            feedback    TEXT DEFAULT '',
            evaluation  TEXT DEFAULT '',
            embedding   TEXT NOT NULL,
            timestamp   DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    try:
        conn.execute("ALTER TABLE memory ADD COLUMN evaluation TEXT DEFAULT ''")
        conn.commit()
    except sqlite3.OperationalError:
        pass 
    conn.commit()
    conn.close()
    
def get_ist_time():
    return datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S IST")

def save_interaction(problem_text: str, solution: str, feedback: str = "", evaluation: dict = {}):
    conn = sqlite3.connect(DB_PATH)
    existing = conn.execute(
        "SELECT id FROM memory WHERE problem = ?", (problem_text,)
    ).fetchone()

    if not existing:
        emb = embeddings_model.embed_query(problem_text)
        conn.execute(
            "INSERT INTO memory (problem, solution, feedback, evaluation, embedding, timestamp) VALUES (?,?,?,?,?,?)",
            (problem_text, solution, feedback, json.dumps(evaluation), json.dumps(emb), get_ist_time())
        )
        conn.commit()
    conn.close()
    


def update_feedback(problem_text: str, feedback: str):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """UPDATE memory SET feedback = ?
           WHERE problem = ?
           AND id = (SELECT MAX(id) FROM memory WHERE problem = ?)""",
        (feedback, problem_text, problem_text)
    )
    conn.commit()
    conn.close()

def find_similar(problem_text: str, threshold: float = 0.75):
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT problem, solution, feedback, evaluation, embedding FROM memory"
    ).fetchall()
    conn.close()

    if not rows:
        return None

    query_emb = np.array(embeddings_model.embed_query(problem_text))
    best_match = None
    best_score = 0.0

    for prob, sol, feedback, evaluation, emb_json in rows:
        stored_emb = np.array(json.loads(emb_json))
        score = np.dot(query_emb, stored_emb) / (
            np.linalg.norm(query_emb) * np.linalg.norm(stored_emb)
        )
        if score > best_score:
            best_score = score
            best_match = {
                "problem": prob,
                "solution": sol,
                "feedback": feedback,
                "evaluation": json.loads(evaluation) if evaluation else {},
                "similarity": round(float(score), 3)
            }

    if best_score >= threshold:
        return best_match
    return None

def get_all_interactions():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT id, problem, solution, feedback, evaluation, timestamp FROM memory ORDER BY timestamp DESC"
    ).fetchall()
    conn.close()
    return [
        {
            "id": r[0], "problem": r[1], "solution": r[2],
            "feedback": r[3], "evaluation": json.loads(r[4]) if r[4] else {},
            "timestamp": r[5]
        }
        for r in rows
    ]

init_db()
