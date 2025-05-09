from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2:1b")

template = """
    You are an expert in answering questions about a pizza restaurent
    
    Here are some relevant reviews: {reviews}
    
    Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate(template)