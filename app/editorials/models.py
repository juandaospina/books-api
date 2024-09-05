from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.orm import relationship 

from app.db import db, BaseModelMixin

class Editorial(db.Model, BaseModelMixin):
    __tablename__ = 'editorials'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    about = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    book_editorial = relationship("Book", back_populates="editorial")