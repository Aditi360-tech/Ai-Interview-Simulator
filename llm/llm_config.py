import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  # IMPORTANT

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    print("API KEY:", api_key)   # TEMP DEBUG

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3
    )
    return llm
