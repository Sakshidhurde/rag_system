import streamlit as st
from pipeline import rag_pipeline, ingest_pipeline

st.set_page_config(page_title="RAG Support Assistant", layout="wide")

# -------------------------
# SESSION STATE INIT
# -------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False


# -------------------------
# SIDEBAR
# -------------------------
with st.sidebar:
    st.title("📄 Knowledge Base")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file is not None:
        with open("data/knowledge.pdf", "wb") as f:
            f.write(uploaded_file.read())

        st.session_state.pdf_uploaded = True
        st.success("📄 PDF uploaded successfully")

        if st.button("🚀 Process PDF"):
            with st.spinner("Processing document..."):
                msg = ingest_pipeline("data/knowledge.pdf")
            st.success(msg)

    st.markdown("---")

    # -------------------------
    # CHAT CONTROLS
    # -------------------------
    st.subheader("🧹 Chat Controls")

    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.success("Chat cleared!")

    if st.button("Delete Last Message"):
        if st.session_state.chat_history:
            st.session_state.chat_history.pop()

    st.markdown("---")


    if st.session_state.pdf_uploaded:
        st.success("📊 Document Ready")
    else:
        st.warning("⚠️ Upload PDF first")


# -------------------------
# MAIN UI
# -------------------------
st.title("🤖 RAG Customer Support Assistant")

st.markdown("Ask questions from your uploaded document below 👇")

# -------------------------
# CHAT INPUT
# -------------------------
query = st.chat_input("Ask your question about the document...")

# -------------------------
# PROCESS QUERY
# -------------------------
if query:

    if not st.session_state.pdf_uploaded:
        st.error("Please upload and process a PDF first.")
    else:
        with st.spinner("Thinking... 🤔"):
            response = rag_pipeline(query)

        st.session_state.chat_history.append((query, response))


# -------------------------
# CHAT DISPLAY
# -------------------------
for user_q, bot_a in reversed(st.session_state.chat_history):

    with st.chat_message("user"):
        st.markdown(f"🧑‍💬 {user_q}")

    with st.chat_message("assistant"):
        st.markdown(f"🤖 {bot_a}")