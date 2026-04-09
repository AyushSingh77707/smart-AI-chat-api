from fastapi import FastAPI
from groq import Groq
from app.core.config import settings

app = FastAPI(title="SmartChat API")

client = Groq(api_key=settings.GROQ_API_KEY)

@app.get("/")
def root():
    return {"message": "SmartChat API is running!"}

@app.get("/test-ai")
def test_ai():
    response = client.chat.completions.create(
        model=settings.GROQ_MODEL,
        messages=[
            {"role":"system","content":"reply in hindi"},
            {"role": "user", "content": "greet me in one line"}
        ]
    )
    ai_reply=response.choices[0].message.content
    return {"ai_reply": ai_reply}