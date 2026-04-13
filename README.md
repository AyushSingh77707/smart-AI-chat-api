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

````
smartchat-api/
├── app/
│   ├── core/
│   │   ├── dependencies.py   
│   │   └── security.py       
│   ├── models/
│   │   ├── user.py           
│   │   ├── session.py        
│   │   └── message.py        
│   ├── routers/
│   │   ├── auth.py           
│   │   ├── session.py        
│   │   └── chat.py           
│   ├── schemas/
│   │   ├── user.py           
│   │   ├── session.py        
│   │   └── chat.py           
│   ├── config.py             
│   ├── database.py           
│   └── main.py               
├── .env.example
├── requirements.txt
├── docker-compose.yml
└── Dockerfile
````

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/AyushSingh77707/smart-AI-chat-api.git
cd smart-AI-chat-api
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env file
```bash
cp .env.example .env
```

### 5. fill the .env
```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
DATABASE_URL=postgresql://postgres:password@localhost/smartchat
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 6. Create database
```bash
psql -U postgres -c "CREATE DATABASE smartchat;"
python -c "from app.database import Base, engine; from app.models.user import User; from app.models.session import Session; from app.models.message import Message; Base.metadata.create_all(bind=engine)"
```

### 7. Run uvicorn server
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
| POST | `/sessions/create` | Create new chat session |
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

After running the server:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`


