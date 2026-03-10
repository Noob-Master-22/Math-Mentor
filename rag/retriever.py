import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from tools.embeddings import get_embeddings


load_dotenv()

INDEX_NAME = os.getenv("PINECONE_INDEX", "math-mentor")
KB_DIR = "kb"

def get_pinecone_index():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    if INDEX_NAME not in [i.name for i in pc.list_indexes()]:
        pc.create_index(
            name=INDEX_NAME,
            dimension=384,  # all-MiniLM-L6-v2 dimension
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
    return pc.Index(INDEX_NAME)

def build_index():
    loader = DirectoryLoader(KB_DIR, glob="**/*.md", loader_cls=TextLoader,
                             loader_kwargs={"encoding": "utf-8"})
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    vectorstore = PineconeVectorStore.from_documents(
        chunks,
        get_embeddings(),
        index_name=INDEX_NAME
    )
    print(f"✅ {len(chunks)} chunks stored in Pinecone")

def get_retriever():
    vectorstore = PineconeVectorStore(
        index_name=INDEX_NAME,
        embedding=get_embeddings()
    )
    return vectorstore.as_retriever(search_kwargs={"k": 3})

if __name__ == "__main__":
    build_index()
