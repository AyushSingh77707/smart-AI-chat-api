from groq import Groq
from app.core.config import settings

client=Groq(api_key=settings.GROQ_API_KEY)

#helper function to generate auto title
def generate_session_title(user_message:str)->str:
    response=client.chat.completions.create(
        model=settings.GROQ_MODEL,
        messages=[
            {
                "role":"system","content":"You are a title generator.Generate a very short title (max 5 words) for a chat session based on user first message,return only the title nothing else"
            },
            {
                "role":"user","content":user_message
            }
        ]
    )
    return response.choices[0].message.content.strip()

generate_session_title("what is purpose of not wasting time")
