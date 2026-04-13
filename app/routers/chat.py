from fastapi import APIRouter,HTTPException,Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user
from app.schemas.chat import ChatRequest,ChatResponse
from groq import Groq
from app.models.message import Message
from app.models.session import Session as ChatSession
from app.core.config import settings
from app.routers.title import generate_session_title

router=APIRouter(prefix="/chat",tags=["Chat"])
client=Groq(api_key=settings.GROQ_API_KEY)

@router.post("/",response_model=ChatResponse)
def send_mssg(info:ChatRequest,db:Session=Depends(get_db),current_user=Depends(get_current_user)):

    #session check
    data=db.query(ChatSession).filter(ChatSession.id==info.session_id,ChatSession.user_id==current_user.id).first()
    if not data:
        raise HTTPException(status_code=404,detail="Session Not Found!")
    
    #load history
    history=db.query(Message).filter(Message.session_id==data.id).order_by(Message.created_at.asc()).all()
    
    #auto title generate
    if len(history)==0:
        data.title=generate_session_title(info.message)
        db.commit()
        db.refresh(data)
    #giving history and user message to groq in ai format

    message_for_groq=[
        {"role":"system","content":"you are a helpful assistant.you must always reply in english always only , regardless of what language user writes in. Never switch to any other language"}
    ]
    

    for i in history:
        message_for_groq.append(
            {"role":i.role,"content":i.content}
        )

    message_for_groq.append({
        "role":"user","content":info.message
    })

    response=client.chat.completions.create(
        model=settings.GROQ_MODEL,
        messages=message_for_groq
    )

    ai_reply=response.choices[0].message.content
    
    #saving user and ai chats in database
    
    user_message=Message(
        session_id=data.id,
        role="user",
        content=info.message
    )
    db.add(user_message)

    ai_message=Message(
        session_id=data.id,
        role="assistant",
        content=ai_reply
    )
    db.add(ai_message)

    db.commit()

    return ChatResponse(
        session_id=data.id,
        user_message=info.message,
        ai_response=ai_reply
    )



