from graph import create_graph
from memory.store import get_all_interactions
from rag.retriever import get_retriever  # ← ADD THIS

graph = create_graph()

if __name__ == "__main__":

    # Test image input
    print("\n=== IMAGE INPUT TEST ===")
    with open("test_image.jpg", "rb") as f:
        img_bytes = f.read()

    config3 = {"configurable": {"thread_id": "test-img-1"}}
    result3 = graph.invoke({
        "raw_input": "",
        "input_type": "image",
        "image_bytes": img_bytes,
        "agent_trace": [],
        "memory_hint": "",
        "hitl_required": False
    }, config3)

    print("Extracted:", result3["parsed_problem"].get("problem_text"))



    # Safe access
    print("Explanation:", result3.get("explanation", "NOT FOUND")[:200])


    # Test retriever
    print("\n=== RETRIEVER TEST ===")
    retriever = get_retriever()
    tests = [
        "solve quadratic equation roots",
        "Bayes theorem conditional probability",
        "integration by parts formula",
        "common mistakes logarithm",
        "JEE shortcut trick algebra"
    ]
    for q in tests:
        docs = retriever.invoke(q)
        print(f"\nQuery: {q}")
        for d in docs:
            print(f"  → {d.metadata.get('source','?').split('/')[-1]}: {d.page_content[:80]}")

    print("\n=== AUDIO RAG DEBUG ===")
    with open("test_audio.m4a", "rb") as f:
        audio_bytes = f.read()

    config = {"configurable": {"thread_id": "debug-audio-1"}}
    result = graph.invoke({
        "raw_input": "",
        "input_type": "audio",
        "audio_bytes": audio_bytes,
        "agent_trace": [],
        "memory_hint": "",
        "hitl_required": False
    }, config)

print("raw_input after processor:", result.get("raw_input"))        # should have transcribed text
print("parsed_problem:", result.get("parsed_problem"))              # should have problem_text
print("topic:", result.get("topic"))                                # should be algebra/calculus etc
print("retrieved_chunks count:", len(result.get("retrieved_chunks", [])))  # should be > 0
print("agent_trace:", result.get("agent_trace"))
