def generate_answer(query, context):
    
    prompt = f"""
You are a precise customer support assistant.

Use ONLY the most relevant part of the context.

Rules:
- Give short answer (1–3 lines)
- Do NOT repeat full document
- Do NOT include unrelated policies

Context:
{context}

Question:
{query}

Answer:
"""

    # SIMPLE EXTRACTION LOGIC (NO LLM NEEDED YET)
    return extract_best_sentence(query, context)


def extract_best_sentence(query, context):
    sentences = context.split(".")

    query_words = query.lower().split()

    for sentence in sentences:
        if any(word in sentence.lower() for word in query_words):
            return sentence.strip() + "."

    # fallback: first line only
    return sentences[0].strip() + "."