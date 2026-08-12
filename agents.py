import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url

# 1. Load local .env if running on localhost
load_dotenv()

# 2. Safely retrieve the Groq API key (works both locally and on Streamlit Cloud)
groq_api_key = os.getenv("GROQ_API_KEY")

# Fallback to Streamlit Secrets if running on Streamlit Cloud
if not groq_api_key and "GROQ_API_KEY" in st.secrets:
    groq_api_key = st.secrets["GROQ_API_KEY"]

# 3. Model setup with explicit api_key
llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0,
    groq_api_key=groq_api_key
)

# 1st agent 
def build_search_agent():
    return llm.bind_tools([web_search])

# 2nd agent 
def build_reader_agent():
    return llm.bind_tools([scrape_url])

# Writer chain 
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Critic chain 
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()