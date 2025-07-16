# simple gen ai app using ollama model gemma3:1b

import os
from dotenv import load_dotenv
# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

langchain_api_key = os.getenv('LANGSMITH_API_KEY')
langchain_project = os.getenv('LANGSMITH_PROJECT')
LANGSMITH_TRACING = True

# chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful assistant. Please respond to the question asked'),
        ('user','question:{question}')
    ]

)

# streamlit framework
st.title('Langchain App with gemma3:1b Model')
input_text = st.text_input('What question you have in mind?')

# Ollama gemma3:1b model
llm = OllamaLLM(model = 'gemma3:1b')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser    

if input_text:
    st.write(chain.invoke({'question': input_text}))

