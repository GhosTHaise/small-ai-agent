from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

OLLAMA_IP = "http://172.24.192.1:11434"
model = OllamaLLM(model="llama3.2:1b", base_url=OLLAMA_IP)


template = """
    You are an expert in answering questions about a pizza restaurent
    
    Here are some relevant reviews: {reviews}
    
    Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

result = chain.invoke({
    "reviews" : [],
    "question" : "What is the best pizza place in town ?"
})

print(result)

