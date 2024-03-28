import typing as t

from .models import Books
from app.exceptions import ObjectNotFound

def get_book_by_id(book_id: int) -> t.Optional[Books]:
    """
    Retrieve a book by id

    Parameters:
        book_id (int): Id of the book

    Raises:
        ObjectNotFound: if the book is not found

    Returns:
        A dict of book or None if the book is not found
    """
    _book = Books.get_by_id(book_id)
    if _book is None:
        raise ObjectNotFound()
    return _book

def get_all_books() -> t.List[Books]:
    """
    This function returns all the books in the database

    Returns:
        List[Books]
    """
    return Books.get_all()

def create_book(
        title: str, 
        description: str, 
        published_year: str, 
        language: str,  
        number_of_pages: int, 
        edition_number: int, 
        author_id: int,
        isbn: int, 
        isbn13: int,
        format_id: int, 
        editorial_id: int, 
    ) -> Books:
    """
    Create a new book in the repository

    Parameters:
        title (str): Title of the book 
        description (str): Description of the book 
        published_year (str): Publisehed year of the book 
        language (str): Language of publish book  
        number_of_pages (int): Number of pages the book 
        edition_number (int): Number of edition 
        author_id (int): Author id that write book
        isbn (int): International Standard Book Number 
        isbn13 (int): International Standard Book Number
        format_id (int): Format of publish book
        editorial_id (int): Editorial that publish book
    
    Returns:
        Book: The created book
    """
    _book = Books(
        title, 
        description, 
        published_year, 
        language, 
        number_of_pages, 
        edition_number, 
        author_id, 
        isbn, 
        isbn13,
        format_id, 
        editorial_id
    )
    _book = _book.create_object()
    return _book

def update_book(book_id: int, **kwargs) -> t.Optional[Books]:
    """
    Updates the information about the book of the repository

    Parameters:
        book_id (int): ID of the book to be updated
        title (str): Title of the book 
        language (str): Language of publish book  
        number_of_pages (int): Number of pages the book 
        **kwargs (dict): Additional properties to be passed to the update 

    Raises:
        ObjectNotFound: if the book to be updated does not exist

    Returns:
        Dict[Book]: A dict with the updated book information
    """
    _book = get_book_by_id(book_id)
    _book.update(kwargs)
    return _book

def delete_book(book_id) -> None:
    """
    Delete the book from the repository

    Parameters:
        book_id (int): Id of the book to be deleted

    Raises:
        ObjectNotFound: if the book to be deleted does not exist

    Returns: 
        None
    """
    _book = get_book_by_id(book_id)
    _book.delete()
