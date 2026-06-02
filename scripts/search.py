from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.PersistentClient(path="./database")
collection = client.get_collection("notes")

query = input("Search: ")

embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[embedding],
    n_results=3
)

print(results["documents"])