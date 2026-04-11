from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Session(Base):
    __tablename__="sessions"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    title=Column(String,nullable=False,default="New Chat")
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    user=relationship("User",back_populates="sessions")
    messages=relationship("Message",back_populates="session",cascade="all , delete")



