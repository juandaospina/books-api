from sqlalchemy import Column, String, ForeignKey, Integer, DateTime

from app.db import db

class Books(db.Model):
    __tablename__ = 'books' 
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(65), nullable=False)
    description = Column(String, nullable=True)
    published_at = Column(DateTime, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"))
