from ingest import load_pdf, chunk_text
from vectorstore import store_chunks
from retriever import retrieve
from llm import generate_answer


# -------------------------
# INGESTION PIPELINE
# -------------------------
def ingest_pipeline(pdf_path):
    text = load_pdf(pdf_path)
    chunks = chunk_text(text)
    store_chunks(chunks)
    return f"Ingested {len(chunks)} chunks"


# -------------------------
# QUERY PIPELINE (RAG FLOW)
# -------------------------
def rag_pipeline(query):
    
    chunks = retrieve(query)

    if not chunks or len(chunks) == 0:
        return "⚠️ Sorry, no information found in document."

    context = "\n".join(chunks)

    answer = generate_answer(query, context)

    return answer