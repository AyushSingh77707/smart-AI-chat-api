# 🤖 SmartChat API

A production-ready AI-powered chat backend built with FastAPI and Groq LLM.

## ✨ Features

- JWT Authentication (Register, Login)
- Multi-session chat management
- AI-powered responses using Groq LLM
- Automatic session title generation
- Full conversation history per session
- PostgreSQL database with SQLAlchemy ORM

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **AI Provider:** Groq (LLaMA 3)
- **Authentication:** JWT (python-jose)
- **Password Hashing:** Bcrypt

## 📁 Project Structure

smartchat-api/
├── app/
│   ├── core/
│   │   ├── dependencies.py   # JWT auth dependency
│   │   └── security.py       # Password & token logic
│   ├── models/
│   │   ├── user.py           # User model
│   │   ├── session.py        # Chat session model
│   │   └── message.py        # Message model
│   ├── routers/
│   │   ├── auth.py           # Auth endpoints
│   │   ├── session.py        # Session endpoints
│   │   └── chat.py           # AI chat endpoints
│   ├── schemas/
│   │   ├── user.py           # User schemas
│   │   ├── session.py        # Session schemas
│   │   └── chat.py           # Chat schemas
│   ├── config.py             # Settings
│   ├── database.py           # DB connection
│   └── main.py               # App entry point
├── .env.example
├── requirements.txt
├── docker-compose.yml
└── Dockerfile

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/AyushSingh77707/smart-AI-chat-api.git
cd smart-AI-chat-api
```

### 2. Virtual environment banao
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Dependencies install karo
```bash
pip install -r requirements.txt
```

### 4. .env file banao
```bash
cp .env.example .env
```

### 5. .env fill karo
```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
DATABASE_URL=postgresql://postgres:password@localhost/smartchat
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 6. Database banao
```bash
psql -U postgres -c "CREATE DATABASE smartchat;"
python -c "from app.database import Base, engine; from app.models.user import User; from app.models.session import Session; from app.models.message import Message; Base.metadata.create_all(bind=engine)"
```

### 7. Server run karo
```bash
uvicorn app.main:app --reload
```

## 📌 API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login and get token |
| GET | `/auth/me` | Get current user |

### Sessions
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/sessions/` | Create new chat session |
| GET | `/sessions/` | Get all sessions |
| GET | `/sessions/{id}` | Get session with messages |
| DELETE | `/sessions/{id}` | Delete session |

### Chat
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/chat/` | Send message and get AI reply |

## 🐳 Docker Setup

```bash
docker-compose up --build
```

## 📄 API Documentation

Server run karne ke baad:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
DATABASE_URL=postgresql://postgres:password@localhost/smartchat
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
