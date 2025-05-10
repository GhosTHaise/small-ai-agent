from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from config import OLLAMA_IP
from vector import retriever

model = OllamaLLM(model="llama3.2:1b", base_url=OLLAMA_IP)

template = """
    You are an expert in answering questions about a pizza restaurent
    
    Here are some relevant reviews: {reviews}
    
    Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n---------------------------")
    question = input("Ask you question (q to quit): ")
    if question == "q":
        break
    
    reviews = retriever.invoke(question)
    
    result = chain.invoke({
        "reviews" : reviews,
        "question" : question
    })

    print(result)

