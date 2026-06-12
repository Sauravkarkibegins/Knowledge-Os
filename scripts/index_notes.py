from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./database")
collection = client.get_or_create_collection("notes")

def chunk_text(text, size=500):
    return [text[i:i+size] for i in range(0, len(text), size)]

for file in Path("./notes").glob("*.md"):
    text = file.read_text()

    chunks = chunk_text(text)
    embeddings = model.encode(chunks).tolist()

    for i, chunk in enumerate(chunks):
        collection.upsert(
            documents=[chunk],
            embeddings=[embeddings[i]],
            ids=[f"{file.stem}_{i}"],
            metadatas=[{"file": file.name}]
        )

print("Indexed successfully")