from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.PersistentClient(path="./database")
collection = client.get_or_create_collection("notes")

notes_path = Path("./notes")

for file in notes_path.glob("*.md"):
    text = file.read_text()

    embedding = model.encode(text).tolist()

    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[file.stem]
    )

print("Indexed successfully")