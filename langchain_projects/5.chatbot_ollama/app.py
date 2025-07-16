from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# simple gen ai app using ollama model gemma3:1b

import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY')
os.environ['LANGSMITH_PROJECT'] = os.getenv('LANGSMITH_PROJECT')
LANGSMITH_TRACKING = True 

prompt = ChatPromptTemplate(
    [
        "system","you are helpful assistant, please respond to the user's query in a concise manner.",
        "user","question:{question}"
    ]
)

def generate_res(question, model='gemma3:1b'):
    llm = OllamaLLM(model = model)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

st.title('langchain chatbot with gemma3:1b model')
user_input = st.text_input('what question do you have in mind?')
if user_input:
    response = generate_res(user_input)
    st.write(response)