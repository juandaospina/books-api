from sqlalchemy import Column, String, ForeignKey, Integer, BigInteger
from sqlalchemy.orm import relationship 

from app.db import db, BaseModelMixin

class Books(db.Model, BaseModelMixin):
    __tablename__ = 'books' 

    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(BigInteger, unique=True, nullable=True)
    isbn13 = Column(BigInteger, unique=True, nullable=True)
    title = Column(String(65), nullable=False)
    description = Column(String, nullable=True)
    published_year = Column(Integer, nullable=True)
    language = Column(String(20), nullable=False)
    number_of_pages = Column(Integer, nullable=False)
    edition_number = Column(Integer, nullable=True)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"))
    format_id = Column(Integer, ForeignKey("books_format.id", ondelete="CASCADE"))
    editorial_id = Column(Integer, ForeignKey("editorials.id"))
    author = relationship("Authors")
    format = relationship("BooksFormat", back_populates="book_format")
    editorial = relationship("Editorials", back_populates="book_editorial")

    def __init__(
            self, 
            title: str, 
            description: str, 
            published_year: int, 
            language: str,  
            number_of_pages: int, 
            edition_number: int, 
            author_id: int,
            isbn: int,
            isbn13: int,
            format_id: int, 
            editorial_id: int,
        ):
        self.title = title
        self.description = description
        self.published_year = published_year
        self.language = language
        self.number_of_pages = number_of_pages
        self.edition_number = edition_number
        self.author_id = author_id
        self.isbn = isbn
        self.isbn13 = isbn13
        self.format_id = format_id
        self.editorial_id = editorial_id


class BooksFormat(db.Model):
    __tablename__ = 'books_format'

    id = Column(Integer, primary_key=True, index=True)
    format = Column(String(45))
    book_format = relationship(Books, back_populates="format")