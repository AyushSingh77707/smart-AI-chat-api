from pydantic import BaseModel 

class ChatRequest(BaseModel):
    session_id:int
    message:str

class ChatResponse(BaseModel):
    session_id:int
    user_message:str
    ai_response:str