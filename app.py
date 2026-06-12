from pathlib import Path
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Knowledge OS", page_icon="🧠", layout="wide")

# --- CUSTOM CSS DESIGN ---
st.markdown("""
    <style>
    .os-card {
        background-color: #1e1e2e;
        color: #cdd6f4;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #89b4fa;
        margin-bottom: 15px;
        font-family: monospace;
    }
    .os-header {
        color: #89b4fa;
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER WITH COLUMNS ---
# Fixes your st.columns("hello") error. Columns need numbers or lists for layout widths.
col1, col2 = st.columns([4,1])

with col1:
    st.title("🧠 Knowledge OS Clone")
    st.caption("Your local Markdown-powered second brain.")

with col2:
    # Example of a metric counter component
    st.metric(label="OS Status", value="Online", delta="Healthy")

st.divider() # Example of a visual layout separator line

# --- TABS LAYOUT ---
# Example of separating views so your workspace stays clean
tab_chat, tab_explorer = st.tabs(["💬 Chat / Search", "📂 File Explorer"])

with tab_chat:
    # --- USER INPUT ---
    query = st.text_input("Chat with OS", placeholder="Type a keyword to scan your markdown notes...")

    if query:
        st.write(f"🔍 **Active Query:** `{query}`")

    # --- LOADING FILE PATHS ---
    # Creates the notes folder automatically if it doesn't exist yet so it won't crash
    Path('./notes').mkdir(exist_ok=True)
    notes = Path('./notes').glob("*.md")

    result = []

    # --- SEARCH ENGINE LOOP ---
    for note in notes: 
        content = note.read_text(encoding="utf-8")
        if query and query.lower() in content.lower():
            result.append((note, content))

    # --- VISUAL STATUS & OUTPUT HANDLING ---
    if not query:
        # Example of an Info Box for the initial "empty/null" query state
        st.info("💡 Enter a keyword in the chat bar above to query your system knowledge.")

    elif not result:
        # Example of a Warning Box for failed matches
        st.warning(f"❌ No matching documents found for: '{query}'")

    else:
        # Example of a Success Banner when a query hits targets
        st.success(f"🎯 Found {len(result)} matching knowledge snippet(s):")
        
        for note_obj, content_text in result:
            # Example of an Expander dropdown component to structure long notes cleanly
            with st.expander(f"📄 Note: {note_obj.name}", expanded=True):
                
                # Example of using our custom CSS design inside the expander
                st.markdown(f"""
                    <div class="os-card">
                        <div class="os-header">SYSTEM RESPONDING:</div>
                        <div>{content_text}</div>
                    </div>
                """, unsafe_allow_html=True)

with tab_explorer:
    st.subheader("System Directories")
    st.write("Below is the source path for your operating directory:")
    # Example of system information block design
    st.code("Root -> ./notes/*.md", language="bash")