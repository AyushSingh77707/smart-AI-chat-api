from fastapi import APIRouter,HTTPException,Depends
from app.core.dependencies import get_current_user
from app.database import get_db
from app.schemas.session import SessionCreate,SessionResponse,SessionWithMessage
from app.models.session import Session
from app.models.message import Message
from typing import List

router=APIRouter(prefix="/session",tags=["Sessions"])

@router.post("/create",response_model=SessionResponse)
def sess_create(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    new_session=Session(user_id=current_user.id,
                        # title=info.title,
                        title="New Chat")
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

@router.get("/",response_model=List[SessionResponse])
def view_all(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    data=db.query(Session).filter(Session.user_id==current_user.id).all()
    return data

@router.get("/{session_id}",response_model=SessionResponse)
def view_id(session_id:int,
            db:Session=Depends(get_db),
            current_user=Depends(get_current_user)):
    
    data=db.query(Session).filter(Session.id==session_id,Session.user_id==current_user.id).first()
    if not data:
        raise HTTPException(status_code=404,detail="Session not found!")
    return data

@router.delete("/{session_id}")
def del_user(session_id:int,
             db:Session=Depends(get_db),
             current_user=Depends(get_current_user)):
    data=db.query(Session).filter(Session.id==session_id,Session.user_id==current_user.id).first()
    if not data:
        raise HTTPException(status_code=404,detail="Session not Found!")
    db.delete(data)
    db.commit()
    return {"message":"Session deleted successfully!"}
    


    
