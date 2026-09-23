from fastapi import FastAPI
from pydantic import BaseModel

from rag import retriever

from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate
import os
app = FastAPI()
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenRouter(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

prompt = ChatPromptTemplate.from_template(
"""
You are a company assistant.

Answer only from context.

Context:
{context}

Question:
{question}
"""
)

class Question(BaseModel):
    question:str

@app.post("/ask")
def ask(data: Question):

    docs = retriever.invoke(data.question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": data.question
    })

    return {
        "answer": response.content
    }