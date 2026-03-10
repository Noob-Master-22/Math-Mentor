# 📐 Math Mentor

> An AI-powered JEE mathematics tutor with multimodal input, RAG-backed knowledge retrieval, and a multi-agent reasoning pipeline.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-multiagent-purple?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-LLaMA3.3+Whisper-orange?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=flat-square)

---

## ✨ Features

- **Multimodal Input** — type a problem, upload an image, or speak into the mic
- **5-Agent Pipeline** — each agent has a single responsibility for clean, traceable reasoning
- **RAG Knowledge Base** — curated JEE formulas, worked examples, and common mistakes
- **Memory Layer** — learns from past interactions and surfaces similar solved problems
- **Human-in-the-Loop** — flags low-confidence solutions for manual review before delivery
- **Dark UI** — clean Streamlit interface with agent trace, confidence badge, and feedback system

---

## 🧠 Architecture

```
Input (text / image / audio)
        ↓
  Input Processor        ← OCR or Whisper transcription
        ↓
     Parser              ← extracts problem, topic, variables
        ↓
     Router              ← classifies: algebra / calculus / probability / linear algebra
        ↓
     Solver              ← RAG retrieval + memory hint + LLaMA 3.3 70B
        ↓
    Verifier             ← confidence scoring, HITL trigger if low confidence
        ↓
    Explainer            ← step-by-step student-friendly explanation
```

---

## 🗂️ Project Structure

```
math-mentor/
├── agents/
│   ├── parser.py         # Extracts structured problem from raw input
│   ├── router.py         # Classifies topic
│   ├── solver.py         # RAG + memory backed solver
│   ├── verifier.py       # Confidence scoring + HITL
│   └── explainer.py      # Student-facing explanation
├── rag/
│   └── retriever.py      # ChromaDB vector store builder + retriever
├── memory/
│   └── store.py          # SQLite-backed interaction memory
├── tools/
│   ├── image_parser.py   # Groq vision OCR
│   ├── audio_parser.py   # Groq Whisper transcription
│   └── embeddings.py     # Embedding model wrapper
├── kb/                   # Markdown knowledge base (JEE formulas + examples)
├── graph.py              # LangGraph state machine
├── app.py                # Streamlit UI
└── .env.example
```

---

## ⚙️ Setup

**1. Clone the repo**
```bash
git clone https://github.com/Noob-Master-22/math-mentor.git
cd math-mentor
```

**2. Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API keys**
```bash
cp .env.example .env
```

Edit `.env`:
```
GROQ_API_KEY=your_groq_api_key_here
```

**5. Build the vector index**
```bash
python3 rag/retriever.py
```

**6. Run the app**
```bash
streamlit run app.py
```

---

## 🧪 Input Modes

| Mode | How |
|---|---|
| ✍️ Text | Type any JEE math problem directly |
| 🖼️ Image | Upload a photo or screenshot of a handwritten/printed problem |
| 🎙️ Audio | Record live via mic or upload an `.m4a` file |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | Groq — LLaMA 3.3 70B Versatile |
| Speech-to-Text | Groq — Whisper Large v3 |
| Vision / OCR | Groq — LLaMA Vision |
| Orchestration | LangGraph |
| Vector Store | ChromaDB |
| Embeddings | HuggingFace / LangChain |
| Memory | SQLite |
| UI | Streamlit |

---

## 📄 License

Copyright (c) 2026 Satvik Reddy. All rights reserved.

This project and its source code are made available for **evaluation and review purposes only**.

- You may **view** and **run** this code locally for assessment
- You may **not** copy, modify, distribute, sublicense, or use any part of this code in your own projects
- You may **not** use this code commercially or claim it as your own work

Unauthorized use, reproduction, or distribution of this code is strictly prohibited.
