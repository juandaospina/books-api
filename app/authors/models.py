from sqlalchemy import Column, String, Integer, DateTime, func

from app.db import db


class Authors(db.Model):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False, unique=True)
    nacionality = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())