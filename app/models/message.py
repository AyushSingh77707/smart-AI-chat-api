from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Message(Base):
    __tablename__="messages"
    id=Column(Integer,primary_key=True,index=True)
    session_id=Column(Integer,ForeignKey("sessions.id"),nullable=False)
    role=Column(String,nullable=False)
    content=Column(Text,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    session=relationship("Session",back_populates="messages")