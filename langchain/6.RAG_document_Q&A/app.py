import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['HF_API_KEY'] = os.getenv('HF_API_KEY')

llm = ChatGroq(api_key = 'GROQ_API_KEY', model = 'llama-3.1-8b-instant')
embeddings = HuggingFaceEmbeddings(model="all-MiniLM-L6-v2")

prompt = ChatPromptTemplate.from_template(
    """
        you are a helpful assistant that answers questions based on the provided documents.
        Please answer most accurate response based on question
        if you don't know the answer, say "i don't know".
        <context>
        {context}
        <context>
        Question: {input}
    """
)

def Create_Vector_Embeddings():
    if 'vectors' not in st.session_state:
        st.session_state.embeddings = HuggingFaceEmbeddings(model = "all-MiniLM-L6-v2")
        st.session_state.loader = PyPDFLoader('../1.imp_modules/attention.pdf')
        st.session_state.docs = st.session_state.loader.load() # load documents of pdf
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) 
        st.session_state.split_docs = st.session_state.text_splitter.split_documents(st.session_state.docs) # split documents into smaller chunks
        st.session_state.db = FaissDB.from_documents(st.session_state.split_docs, st.session_state.embeddings) # create vector store

st.title("RAG Document Q&A App")

import time

user_input = st.text_input('enter your query')

if st.button('Document Embeddings'):
    Create_Vector_Embeddings()
    st.write('Vector Database is ready')

if user_input:
    document_chain = create_stuff_document_chain(llm, prompt)
    retriever = st.session_state.db.as_retriever()
    retriever_chain = create_retrival_chain(retriever, document_chain)

    start = time.process_time()
    response = retriever_Chain.invoke({input: user_input})
    print('response time: {time.process_time() - start}')

    st.write(response['answer'])

    with st.expender('Document Similarity Search'):
        for i, doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write('-----------------------------')
        