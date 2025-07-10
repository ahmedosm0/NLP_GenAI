import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# loading env variables
from dotenv import load_dotenv
load_dotenv()

# callings api keys
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
os.environ['HF_API_KEY'] = os.getenv('HF_API_KEY')

# loading embeddings model of huggingface
embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

st.title('Conversational RAG With PDF uplaods and chat history')
st.write("Upload Pdf's and chat with their content")

# input GROQ API KEY from user for loading GROQ model
API_input = st.text_input("Enter GROQ API KEY', type='password'")
if API_input:
    llm = ChatGroq(model_name='llama-3.1-8b-instant', groq_api_key=GROQ_API_KEY)

# processing uploaded pdf docs
    uploaded_files = st.file_uploader('upload PDF file', type='pdf', accept_multiple_files=True)
    if uploaded_files:
        documents = []
        for uploaded_file in uploaded_files:
            temp_pdf = f"./temp.pdf"
            with open(temp_pdf, 'wb') as f:
                f.write(uploaded_file.getvalue())
                file_name = uploaded_file.name

            loader = PyPdfLoader(temp_pdf)
            docs = loader.load()
            documents.extend(docs)

# split docs into chunks, and store in vector store
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = text_splitter.split_documents(documents)
        vector_store = Chroma.from_documents(split_docs, embeddings)
        retriever = vector_store.as_retriever()

# creating history aware retriever
        contextualize_system_prompt = (
            "Given a chat history and the latest user question"
            "which might reference context in the chat history, "
            "formulate a standalone question which can be understood "
            "without the chat history. Do NOT answer the question, "
            "just reformulate it if needed and otherwise return it as is."
        )
        contextualize_system_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        
        history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_system_prompt)

# creating 
        system_prompt = (
                "You are an assistant for question-answering tasks. "
                "Use the following pieces of retrieved context to answer "
                "the question. If you don't know the answer, say that you "
                "don't know. Use three sentences maximum and keep the "
                "answer concise."
                "\n\n"
                "{context}"
            )
        
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessgagesPlaceholder('chat_history'),
                ("human", "{input}")
            ]
        )
        question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
        rag_chin = create_retrieval_chain(history_aware_retriever, question_answer_chain)

        def get_session_history(session_id:str)->BaseChatMessageHistory:
            if session_id not in st.session_state.store:
                st.session_state.store[session_id]=ChatMessageHistory()
            return st.session_state.store[session_id]

# converstaional rag chain
        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain, get_session_history,
            input_message_key="input",
            history_message_key="chat_history",
            output_message_key="answer"
        )






