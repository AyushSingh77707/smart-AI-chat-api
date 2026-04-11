from pydantic import BaseModel
from typing import List
from datetime import datetime

class SessionCreate(BaseModel):
    title:str="New Chat"

class SessionResponse(BaseModel):
    id:int
    title:str
    created_at:datetime

    class Config:
        from_attributes=True

class MessageResponse(BaseModel):
    id:int
    role:str
    content:str
    created_at:datetime

    class Config:
        from_attributes=True

class SessionWithMessage(BaseModel):
    id:int
    title:str
    created_at:datetime
    messages:List[MessageResponse]

    class Config:
        from_attributes=True

