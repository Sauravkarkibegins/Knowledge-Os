import streamlit as st
from pathlib import Path
st.write("Knowlege Os Clone")
query = st.text_input("Chat with Os")

st.write(f"Query : {query}")

notes = Path('./notes').glob("*md")


result =[]

for note in notes : 
    content  = note.read_text()


    if query and query.lower() in content.lower() :
           result.append((note ,content))
        



if not result :
      st.write("No match found")
else:
    for note_obj, content_text in result:
        # note_obj is the first item in the tuple, content_text is the second
           st.write(f"**Answer:** {content_text}")






    