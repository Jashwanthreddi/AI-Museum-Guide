# 🎨 AI-Powered Interactive Museum Guide 🤖

An intelligent AI-based virtual museum assistant built using Flask, LangChain, FAISS, and OpenAI APIs.  
This project provides an interactive chatbot and voice assistant experience for visitors of the Salar Jung Museum.

The system uses Retrieval-Augmented Generation (RAG) to retrieve museum-related information from custom datasets and generate intelligent responses in natural language.

---

# 📌 Project Overview

The AI Museum Guide helps users explore museum information through conversational AI.

Users can ask questions related to:
- 🏛️ Museum history
- 🎭 Art collections
- 🖼️ Galleries & exhibitions
- 📚 Manuscripts & library
- ⏰ Timings & entry fees
- 🚌 Transportation & directions
- ♿ Visitor facilities
- 🎤 Voice-based interaction

The project combines:
- Semantic Search
- Vector Databases
- OpenAI LLMs
- Flask Web Application
- RAG Architecture

---

# 🚀 Features

## ✅ AI Chatbot
Ask museum-related questions in natural language.

Example:
```text
Who was Salar Jung III?
```

---

## ✅ Voice Assistant
Dedicated voice interaction interface for better accessibility.

---

## ✅ Semantic Search using FAISS
Uses vector embeddings to retrieve highly relevant information instead of simple keyword matching.

---

## ✅ Intelligent Greeting Detection
Handles greetings separately for better conversational flow.

Examples:
```text
Hi
Hello
Good Morning
```

---

## ✅ Museum Knowledge Base
Contains rich information about:
- Indian Art
- Persian Art
- European Art
- Far Eastern Art
- Museum History
- Manuscripts
- Library Collections
- Visitor Information

---

# 🧠 How the Project Works

```text
User Question
      ↓
Flask Backend
      ↓
FAISS Similarity Search
      ↓
Retrieve Relevant Chunks
      ↓
LangChain QA Chain
      ↓
OpenAI Language Model
      ↓
AI Generated Response
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Flask | Web Framework |
| LangChain | LLM Workflow |
| OpenAI API | AI Response Generation |
| FAISS | Vector Database |
| HTML/CSS | Frontend |
| JavaScript | Client-side Interaction |

---

# 📂 Project Structure

```text
AI-Museum-Guide/
│
├── app.py                     # Main Flask application
├── salarjung.txt              # Museum dataset 1
├── salarjung2.txt             # Museum dataset 2
├── .env                       # API keys and environment variables
├── .gitignore
│
├── templates/
│   ├── index.html             # Landing page
│   ├── bot.html               # Chatbot interface
│   └── voiceassistant.html    # Voice assistant UI
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Museum-Guide.git
cd AI-Museum-Guide
```

---

## 2️⃣ Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Libraries

Create a `requirements.txt` file:

```txt
flask
langchain
langchain-community
langchain-openai
faiss-cpu
openai
tiktoken
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

⚠️ Never upload your API key to GitHub.

---

# ▶️ Running the Project

```bash
python app.py
```

Application will run on:

```text
http://127.0.0.1:5000
```

---

# 💬 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Landing Page |
| `/chat` | GET | Chatbot Interface |
| `/voice` | GET | Voice Assistant |
| `/ask` | POST | AI Question Endpoint |

---

# 🧩 Core Functionalities

## 📄 Document Loading
Loads museum datasets from text files.

---

## ✂️ Text Chunking
Splits large text into manageable chunks using LangChain text splitters.

---

## 🧠 Embedding Generation
Creates vector embeddings using OpenAI Embeddings.

---

## 🔍 Similarity Search
Uses FAISS to retrieve the most relevant chunks for user queries.

---

## 🤖 Response Generation
Uses LangChain QA chain with OpenAI LLM to generate final responses.

---

# 🏛️ Knowledge Base Highlights

The project dataset includes:

## 🎨 Art Collections
- Indian Art
- Persian Art
- European Art
- Chinese & Japanese Art

---

## 📚 Manuscripts & Library
- Rare manuscripts
- Historical books
- Arabic, Persian & Urdu collections

---

## 🏛️ Museum Information
- Entry fees
- Timings
- Facilities
- Transportation routes

---

# 📸 Example Questions

```text
What are the museum timings?
Tell me about Veiled Rebecca.
How can I reach the museum?
What collections are available?
Who was Salar Jung III?
```

---

# 🧪 Example Response

```text
User:
Tell me about Veiled Rebecca.

AI:
Veiled Rebecca is a famous marble sculpture created
by G.B. Benzoni and acquired by Salar Jung I during
his visit to Italy in 1876.
```

---

# 🔐 Security Improvements

## Current Limitations
- Hardcoded API keys
- No authentication
- Debug mode enabled

---

## Recommended Improvements
- Use secure `.env` configuration
- Add authentication system
- Disable debug mode in production
- Implement rate limiting
- Add logging & monitoring

---

# 🌟 Future Enhancements

- 🎤 Real-time Speech-to-Text
- 🌐 Multilingual Support
- 📱 Mobile Responsive UI
- 🧠 Conversational Memory
- 🗺️ Interactive Museum Navigation
- 🔊 Text-to-Speech Responses
- ☁️ Cloud Deployment

---

# 📚 Concepts Used

This project demonstrates:
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Embeddings
- NLP Applications
- Flask Backend Development
- AI Chatbot Systems

---

# 👨‍💻 Author

## Bejjanki Jashwanth Reddy

# 🤝 Contributions

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and create pull requests.

---

# 📜 License

This project is developed for educational and learning purposes.

---
