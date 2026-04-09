from fastapi import APIRouter,HTTPException,Depends
from app.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserCreate,UserLogin,UserResponse,Token
from sqlalchemy.orm import Session
from app.core.security import hash_password,verify_password,create_access_token

router=APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register",response_model=UserResponse)
def register(info:UserCreate,db:Session=Depends(get_db)):
    existing_email=db.query(User).filter(User.email==info.email).first()
    if existing_email:
        raise HTTPException(status_code=409,detail="Email already exists!")
    existing_username=db.query(User).filter(User.username==info.username).first()
    if existing_username:
        raise HTTPException(status_code=409,detail="Email already exists!")
    hashed=hash_password(info.password)
    new_user=User(
        username=info.username,
        email=info.email,
        password=hashed
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(info:UserLogin,db:Session=Depends(get_db)):

    existing_user=db.query(User).filter(User.email==info.email).first()

    if not existing_user or not verify_password(info.password,existing_user.password):
        raise HTTPException(status_code=401,detail="invalid credentials!")
    
    access_token=create_access_token(data={"sub":existing_user.username})
    return{
        "access_token":access_token,
        "token_type":"bearer"
    }

@router.get("/me",response_model=UserResponse)
def get_me(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return current_user
    


    
    