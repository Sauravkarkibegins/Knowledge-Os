import ollama
import streamlit as st

context = "Git branches are used for development..."

query = st.text_input("Ask: ")

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "system",
            "content": f"""
Use this knowledge:
{context}

Question: {query}
"""
        }
    ]
)

st.write(response['message']['content'])