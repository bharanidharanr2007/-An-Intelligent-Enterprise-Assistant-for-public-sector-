# An-Intelligent-Enterprise-Assistant-for-public-sector

# Intelligent Enterprise Assistant Chatbot
### SIH1706 – Smart India Hackathon Problem

AI-powered enterprise chatbot that helps employees get information about **HR policies, IT support, company events, and organizational documents** using **NLP and Deep Learning**.

---

# Features

- Natural language chatbot for employee queries
- HR policy and IT support question answering
- Document upload and analysis
- Document summarization
- Keyword extraction from documents
- Email based **2 Factor Authentication (2FA)**
- Bad language filtering
- Supports **minimum 5 parallel users**
- Response time < **5 seconds**

---

# Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| NLP | HuggingFace Transformers |
| LLM Framework | LangChain |
| Vector Database | FAISS |
| Database | SQLite |
| Document Processing | PyPDF2 |
| Authentication | Email OTP (SMTP) |
| Deployment | Docker |

---

# System Architecture

```
Users
|
Frontend (Streamlit)
|
Backend API (FastAPI)
|
NLP Engine (LangChain + Transformers)
|
Vector Database (FAISS)
|
Knowledge Base (HR / IT / Events Data)

```


---

# Project Structure

```
enterprise-chatbot
│
├── app.py
├── auth.py
├── chatbot.py
├── document_processor.py
├── profanity_filter.py
├── knowledge_base
│ └── hr_policy.txt
│
├── requirements.txt
├── README.md

```

# Scalability

System can support multiple users using:

FastAPI async processing

FAISS optimized vector search

Lightweight NLP models

Parallel users supported: 5+


# Demo Flow

Login using email OTP

Ask HR policy question

Ask IT support question

Upload document

Generate document summary

Test bad language filter


# Future Improvements

Voice chatbot

Multilingual support

Slack / Teams integration

Advanced LLM based reasoning


# Final Result

The Intelligent Enterprise Assistant Chatbot was successfully developed to answer employee queries related to HR policies, IT support, and company events using AI and Natural Language Processing (NLP). The system allows employees to interact with the chatbot, upload documents, and receive summaries or key information from those documents.

The chatbot includes email-based 2FA authentication for security, bad language filtering, and can support multiple users simultaneously with a response time of less than 5 seconds. This solution improves organizational efficiency by providing quick and intelligent access to company information.
