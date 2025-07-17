# Generative AI Chat App with Gemma 3:1b

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-1e1e20?style=for-the-badge&logo=ollama&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00A67E?style=for-the-badge)

A simple generative AI application using the Gemma 3:1b model through Ollama, powered by LangChain and Streamlit.

## Features

- 💬 Interactive chat interface powered by Streamlit
- 🤖 Local AI inference using Ollama's Gemma 3:1b model
- ⛓️ LangChain integration for prompt templating and output parsing
- 🔒 Environment variable configuration for LangSmith tracing

## Prerequisites

Before running the application, ensure you have:

1. Python 3.10
2. [Ollama](https://ollama.com/) installed and running
3. Gemma 3:1b model downloaded (run `ollama run gemma:3b` in terminal)
4. LangSmith account for tracing (optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ahmedosm0/NLP_GenAI.git

2. Install dependencies:
pip install -r requirements.txt

3. Run the application with:
streamlit run app.py

## 📸 Demo
![App Screenshot](https://raw.githubusercontent.com/ahmedosm0/NLP_GenAI/main/gen_ai_app.png)

