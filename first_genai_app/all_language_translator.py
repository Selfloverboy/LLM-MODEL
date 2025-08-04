import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Title
st.title('🌍 Language Translator - Gemini + LangChain Demo')

# Language options
languages = ["Kannada", "Telugu", "Hindi", "Tamil", "French", "Spanish", "German"]

# User input
input_language = st.selectbox("Select Input Language", ["English"])  # You can add more if needed
output_language = st.selectbox("Select Output Language", languages)
input_text = st.text_input("Enter text to translate:")

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
    ("human", "{input}")
])

# LLM setup
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Translation
if input_text:
    result = chain.invoke({
        "input_language": input_language,
        "output_language": output_language,
        "input": input_text
    })
    st.markdown("### Translated Text:")
    st.success(result)
