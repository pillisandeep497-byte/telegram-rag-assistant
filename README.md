# 🤖 Telegram RAG Assistant

A Retrieval-Augmented Generation (RAG) chatbot that answers company policy and HR-related questions directly from Telegram.

Built using:

- FastAPI
- LangChain
- FAISS
- OpenRouter / Gemini
- n8n
- Telegram Bot API

---

## Features

✅ Multi-PDF RAG

✅ Telegram Integration

✅ FastAPI Backend

✅ LangChain Retrieval Chain

✅ FAISS Vector Database

✅ HR Policy Assistant

✅ Real-Time Question Answering

---

## Architecture

Telegram
↓
n8n Workflow
↓
FastAPI API
↓
LangChain RAG
↓
FAISS Vector Store
↓
LLM (OpenRouter/Gemini)
↓
Telegram Response

---

## Demo Questions

What is the leave policy?

How many casual leaves are available?

What is the probation period?

What are office timings?

What is the company dress code?

---

## Tech Stack

Python

FastAPI

LangChain

FAISS

n8n

Telegram

OpenRouter

Streamlit

---

## Future Improvements

- Conversation Memory
- Voice Questions
- WhatsApp Integration
- PostgreSQL Storage
- Redis Cache
- LangGraph Agents

---

## Installation

### Clone Repository

git clone https://github.com/pillisandeep497-bye/telegram-rag-assistant.git

cd telegram-rag-assistant

### Install Requirements

pip install -r requirements.txt

### Run FastAPI

uvicorn app:app --reload

### Start n8n

npx n8n

### Start LocalTunnel

lt --port 5678

---

## Author

Sandeep Pilli

AI & ML Diploma Student

Aspiring GenAI Engineer
