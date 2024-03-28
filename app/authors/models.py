import typing as t

from sqlalchemy import Column, String, Integer, DateTime, func

from app.db import db, BaseModelMixin


class Authors(db.Model, BaseModelMixin):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    about_author = Column(String(255), nullable=True) 
    born_date = Column(Integer, nullable=True) 
    created_at = Column(DateTime, server_default=func.now())
    email = Column(String, nullable=False, unique=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    nacionality = Column(String, nullable=False)
    updated_at = Column(DateTime, server_default=func.now()) 

    def __init__(
            self, 
            first_name: str, 
            last_name: str, 
            email: str, 
            nacionality: t.Optional[str], 
            about_author: t.Optional[str], 
            born_date: t.Optional[int], 
        ):
        self.about_author = about_author
        self.born_date = born_date
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.nacionality = nacionality
