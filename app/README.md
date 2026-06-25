#  Text Processing API

A FastAPI-based project that provides text processing features like summarization, translation, and email generation.

---
# Functionalities
* Text Summarization

This feature generates a short and meaningful summary from long input text. It helps extract key points while preserving the original context.

* Language Translation

This functionality translates input text from one language to another using a backend service. It ensures accurate and fast conversion based on the selected target language.

* Email Generation

This feature automatically generates well-structured emails based on user input or prompts. It creates professional content suitable for formal communication.

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Pydantic
- python-dotenv

---

## 📌 Features
- ✂️ Text Summarization
- 🌐 Language Translation
- 📧 Email Generation
- ✅ Input Validation
- 🪵 Logging System
- ⚠️ Global Exception Handling

---

## 🚀 How to Run

### Install dependencies
pip install -r requirements.txt

### Run server
python -m uvicorn app.main:app --reload

---

## 📡 API Endpoints

POST /summarize  
POST /translate  
POST /generate-email  

---

## 📖 API Docs
http://127.0.0.1:8000/docs

---

## 🪵 Logs
logs/app.log

---

## ⚙️ Environment Variables
Create a .env file:

APP_NAME=Text Processing API  
DEBUG=True  

---

## 👩‍💻 Author
Shreya