import streamlit as st
from pathlib import Path

st.title("🧠 Knowledge OS")

query = st.text_input("Ask your brain:")

notes = Path("./notes").glob("*.md")

if query:
    st.subheader(f"Searching for: {query}")

for note in notes:
    st.subheader(note.stem)
    st.code(note.read_text())