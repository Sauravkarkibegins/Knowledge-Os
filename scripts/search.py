from sentence_transformers import SentenceTransformer
import chromadb
import streamlit as st

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.PersistentClient(path="./database")
collection = client.get_collection("notes")

query = st.text_input("Search: ")

if query :
  embedding = model.encode(query).tolist()

  results = collection.query(
    query_embeddings=[embedding],
    n_results=3
 ) 

  st.write(f"Answer : {results["documents"]}")

else :
  st.info('No query')