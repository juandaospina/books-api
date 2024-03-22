from sqlalchemy import Column, String, Integer, DateTime, func

from app.db import db, BaseModelMixin


class Authors(db.Model, BaseModelMixin):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False, unique=True)
    nacionality = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    def __init__(self, first_name, last_name, age, email, nacionality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.nacionality = nacionality