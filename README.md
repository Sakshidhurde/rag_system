# 🤖 RAG-Based Customer Support Assistant

A Retrieval-Augmented Generation (RAG) system that answers customer queries using a PDF knowledge base. It combines **document retrieval, embeddings, vector database, and LLM generation** to provide accurate and context-aware responses.

---

## 🚀 Features

- 📄 Upload and process PDF documents
- 🧠 Semantic search using embeddings
- 🔎 Context-aware answer generation
- 💬 Interactive Streamlit chat UI
- 🗄️ ChromaDB vector database
- 🔗 LangGraph workflow orchestration
- ⚡ Fast and scalable retrieval system
- 👨‍💻 Human-in-the-Loop (optional)

---

## 🏗️ System Architecture
User → Streamlit UI → LangGraph → Retriever → ChromaDB → Context → LLM → Answer

---

## 📂 Project Structure

- app.py → Streamlit frontend UI  
- ingest.py → PDF loading & chunking  
- retriever.py → Similarity search  
- vectorstore.py → ChromaDB setup  
- pipeline.py → Main RAG workflow  
- data/ → Uploaded PDFs  
- chroma_db/ → Vector storage  

---

## ⚙️ Installation

### 1️⃣ Clone Repository
git clone https://github.com/your-username/rag-project.git

cd rag-project

---

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate # Windows

---

### 3️⃣ Install Dependencies
pip install -r requirements.txt

---

## ▶️ Run Project
streamlit run app.py


---

## 📄 How It Works

### 1. Document Ingestion
- PDF is uploaded  
- Text extracted using PyPDF  
- Text split into chunks  
- Converted into embeddings  
- Stored in ChromaDB  

---

### 2. Query Processing
- User enters question  
- Query converted to embedding  
- Similar chunks retrieved  

---

### 3. Answer Generation
- Retrieved context sent to LLM  
- LLM generates final response  
- Answer displayed in UI  

---

## 🧠 Technologies Used

- Python  
- Streamlit  
- LangGraph  
- ChromaDB  
- SentenceTransformers  
- PyPDF  
- LLM (OpenAI / Mistral / HuggingFace)

---

## 📌 Example Questions

- What is refund policy?  
- How can I contact support?  
- What is delivery time?  
- Can I cancel my order?  

---

## 📊 Future Improvements

- Multi-PDF support  
- Reranking model for better accuracy  
- Voice-based chatbot  
- Feedback learning system  
- Cloud deployment (AWS / GCP)

---

## 👨‍💻 Author

RAG-Based Customer Support System Project  
Designed for learning **Retrieval-Augmented Generation + LangGraph workflows**

---

## ⭐ Acknowledgements

- LangChain / LangGraph  
- ChromaDB  
- HuggingFace  
- OpenAI / Mistral
