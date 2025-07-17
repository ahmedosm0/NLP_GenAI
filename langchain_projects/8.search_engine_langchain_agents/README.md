# 🧠 Generative AI RAG & Agent-Based Chat Apps

A collection of Generative AI applications built with **LangChain**, **Streamlit**, and **Groq (LLM)**. These include:

- Chat with PDF using RAG (with/without chat history)
- Search-enabled agents using Arxiv, Wikipedia, and DuckDuckGo
- Simple static PDF Q&A interface

---

## 📦 Tech Stack

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00A67E?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-0A0A0A?style=for-the-badge&logo=groq)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black)

---

## 📂 Apps Overview

### ✅ 1. RAG PDF Q&A (Single Question)
> **File**: `app.py`  
Ask a question from a PDF file using **FAISS** vector DB and **HuggingFace embeddings**.

**Core Features:**
- PDF loaded with `PyPDFLoader`
- Embeddings via `all-MiniLM-L6-v2`
- LangChain `retrieval_chain` + `stuff_documents_chain`

---

### 🧠 2. Conversational RAG with Chat History
> **File**: `rag_chat.py`  
Chat naturally with your PDFs using **LangChain memory** and **RunnableWithMessageHistory**.

**Core Features:**
- Upload multiple PDFs
- Track conversation history
- Reformulate follow-up questions
- Uses `ChatMessageHistory`, `Chroma`, and `ChatGroq`

---

### 🌍 3. LLM + Tools Agent Chat (Wikipedia, Arxiv, Search)
> **File**: `agent_chat.py`  
An intelligent agent that uses multiple **search tools** (Wikipedia, Arxiv, DuckDuckGo) to answer user queries.

**Core Features:**
- AgentType: `ZERO_SHOT_REACT_DESCRIPTION`
- Tools: Arxiv, Wikipedia, DuckDuckGo
- Memory-based chat interface

---

## 🧪 Local Setup

### ⚙️ Prerequisites
- Python 3.10+
- Install [Ollama](https://ollama.com/) and run a model:
```bash
ollama run llama3

## 📸 Demo
![App Screenshot](./app.png)

## 📦 Installation
```bash
1. Clone the Repository
git clone https://github.com/ahmedosm0/NLP_GenAI.git

2. Install dependencies:
pip install -r requirements.txt

3. Run the application with:
streamlit run app.py

