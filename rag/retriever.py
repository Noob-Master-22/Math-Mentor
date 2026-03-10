import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from tools.embeddings import get_embeddings  

load_dotenv()

CHROMA_DIR = "chroma_db"
KB_DIR = "kb"


def build_index():
    print("Loading KB files...")
    loader = DirectoryLoader(
        KB_DIR,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )
    docs = loader.load()
    print(f"Loaded {len(docs)} files")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(docs)
    print(f"Split into {len(chunks)} chunks")

    print("Embedding and storing...")
    db = Chroma.from_documents(
        chunks,
        get_embeddings(),
        persist_directory=CHROMA_DIR
    )
    print(f"✅ Index built with {len(chunks)} chunks → saved to chroma_db/")

def get_retriever():
    db = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=get_embeddings()
    )
    return db.as_retriever(search_kwargs={"k": 3})

if __name__ == "__main__":
    build_index()
