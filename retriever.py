from vectorstore import search_similar

def retrieve(query):
    chunks = search_similar(query, k=3)

    # FILTER only most relevant sentence-like chunk
    filtered = []

    for c in chunks:
        if any(word in c.lower() for word in query.lower().split()):
            filtered.append(c)

    return filtered if filtered else chunks[:1]