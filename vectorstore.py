from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("rag_docs")


def store_chunks(chunks):
    embeddings = model.encode(chunks)

    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embeddings[i].tolist()]
        )


def search_similar(query, k=3):
    query_embedding = model.encode([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k
    )

    return results["documents"][0]