import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Knowledge OS",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .reportview-container .main .block-container {
        padding-top: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .stTextInput>div>div>input {
        height: 3rem;
        font-size: 1rem;
    }
    .result-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 0.8rem;
        border: 1px solid #e6e9ed;
        margin-bottom: 1rem;
    }
    .result-title {
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧠 Knowledge OS")
st.markdown(
    "Find notes quickly by searching your vault and reviewing matches instantly."
)

with st.sidebar:
    st.header("Search Notes")
    st.write("Enter a search query to find matching markdown files in the `notes/` folder.")
    st.write("- Search is case-insensitive")
    st.write("- Matches are shown with the note title and full content")
    st.write("- Leave search empty to see all notes")
    notes_dir = Path("./notes")
    st.markdown(f"**Notes directory:** `{notes_dir.resolve()}`")

query = st.text_input("Ask your brain:", placeholder="Type keywords, topics, or note titles...")
notes = sorted(Path("./notes").glob("*.md"))
results = []

for note in notes:
    content = note.read_text()
    if not query or query.lower() in content.lower() or query.lower() in note.stem.lower():
        results.append((note, content))

if not results:
    st.warning("No matching notes found. Try a different keyword or check the notes folder.")
else:
    st.write(f"**{len(results)} note{'s' if len(results) != 1 else ''} found**")
    for note, content in results:
        with st.expander(note.stem, expanded=False):
            st.markdown(f"<div class='result-card'>", unsafe_allow_html=True)
            st.markdown(content)
            st.markdown("</div>", unsafe_allow_html=True)
