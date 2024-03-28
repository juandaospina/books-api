from sqlalchemy import Column, DateTime, String, Integer, func

from app.db import db, BaseModelMixin

class Editorials(db.Model, BaseModelMixin):
    __tablename__ = 'editorials'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    about = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())