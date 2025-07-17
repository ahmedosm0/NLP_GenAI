# 🦜 LangChain SQL Chat Agent

A Streamlit app that allows users to **chat with a SQL database** using **LangChain**, powered by **Groq's LLM**. This app supports both **SQLite** (local `.db` file) and **MySQL** database connections.

---

## 🚀 Features

- 🔌 Connect to **SQLite3** or your own **MySQL** database
- 💬 Natural language queries to extract data from your DB
- 🤖 Uses **LangChain SQL Agent** with `ZERO_SHOT_REACT_DESCRIPTION`
- ⚡ Powered by **Groq’s Llama3-8b-8192** LLM for fast, intelligent responses
- 💡 Built-in chat memory and `StreamlitCallbackHandler` for live interactions

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00A67E?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-111111?style=for-the-badge)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

---

## 📸 Demo

![App Screenshot](./app.png)

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.10+
- `Groq` API Key from [console.groq.com](https://console.groq.com/)
- SQLite `.db` file (default: `student.db`) or MySQL database credentials

### 📦 Install Dependencies

```bash
pip install -r requirements.txt

streamlit run app.py
