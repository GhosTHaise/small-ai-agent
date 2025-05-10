from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd
from config import OLLAMA_IP

df = pd.read_csv("realistic_restaurant_reviews.csv")

embeddings = OllamaEmbeddings(model="mxbai-embed-large", base_url=OLLAMA_IP)

db_location ="./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating" : row["Rating"], "Date" : row["Date"]},
            id=str(i)
        )
        
        ids.append(str(i))
        documents.append(document)
        

