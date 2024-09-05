import typing as t

from .models import Book
from app.exceptions import ObjectNotFound
from app.categories.models import Category


def get_book_by_id(book_id: int) -> t.Optional[Book]:
    """Retrieve a book by id
    
    :param book_id: Id of the book
    :raise ObjectNotFound: if the book is not found
    :return: A dict of book or None if the book is not found
    """
    book = Book.get_by_id(book_id)
    if book is None:
        raise ObjectNotFound()
    return book


def get_all_books() -> t.List[Book]:
    """This function returns all the books in the database

    :return: A list of Book objects
    """
    return Book.get_all()


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
        categories: list[dict[str, int | str]] | None 
    ) -> Book:
    """Create a new book in the repository

    :param title: Title of the book 
    :param description: Description of the book 
    :param published_year: Publisehed year of the book 
    :param language: Language of publish book  
    :param number_of_pages: Number of pages the book 
    :param edition_number: Number of edition 
    :param author_id: Author id that write book
    :param isbn: International Standard Book Number 
    :param isbn13: International Standard Book Number
    :param format_id: Format of publish book
    :param editorial_id: Editorial that publish book
    :param categories: Book categories
    :return: The created book object
    """
    book = Book(
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
    for category in categories: 
        _category = Category.query.get(category["id"])
        if _category:
            book.categories.append(_category)
    book.create_object()
    return book


def update_book(book_id: int, **kwargs) -> t.Optional[Book]:
    """Updates the information about the book of the database

    :param book_id: ID of the book to be updated
    :param title: Title of the book 
    :param language: Language of publish book  
    :param number_of_pages: Number of pages the book 
    :para(dict): Additional properties to be passed to the update 
    :raise ObjectNotFound: if the book to be updated does not exist
    :return: A dict with the updated book object
    """
    book = get_book_by_id(book_id)
    book.update(kwargs)
    return book


def delete_book(book_id) -> None:
    """Delete the book from the repository

    :param book_id: Id of the book to be deleted
    :raise ObjectNotFound: if the book to be deleted does not exist
    :return: None
    """
    book = get_book_by_id(book_id)
    book.delete()
