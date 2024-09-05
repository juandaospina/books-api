import typing as t
from datetime import datetime

from .models import Author
from app.exceptions import ObjectNotFound


def get_all_authors() -> t.List[Author]:
    """
    Retrieves all author from the database

    Returns:
        List[Author]: List of Author
    """
    return Author.get_all()


def get_author_by_id(id: int) -> t.Optional[Author]:
    """
    Retrieve an author by id

    Parameters:
        id (int): ID of the author

    Raises:
        ObjectNotFound: if the author is not found
    
    Returns:
        Dict[Author] or None if the author is not found
    """
    author = Author.get_by_id(id)
    if author is None:
        raise ObjectNotFound()
    return author


def create_author(first_name, last_name, email, 
                  nacionality, about_author, born_date) -> Author:
    """
    Create a new author in the repository

    Parameters:
        first_name (str): The first name of the author
        last_name (str): The last name of the author
        email (str): The email address of the author
        nacionality (str): The nacionality of the author
        **kwargs (dict): Additional properties

    Returns:
        Dict[Author]: The new author object
    """
    author = Author(first_name, last_name, email, 
                      nacionality, about_author, born_date)
    return Author.create_object(author)


def update_author(author_id: int, **kwargs) -> Author:
    """
    Updates the information about the author of the repository

    Parameters:
        author_id (int): ID of the author to be updated
        **kwargs (dict): Additional properties to be passed to the update 

    Raises:
        ObjectNotFound: if the author to be updated does not exist

    Returns:
        Dict[Author]: The information of author updated
    """
    author = get_author_by_id(author_id)
    kwargs["updated_at"] = datetime.now()
    author.update(kwargs)
    return author


def delete_author(author_id: int) -> None:
    """
    Delete the author from the repository

    Parameters:
        author_id (int): ID of the author to be deleted

    Raises:
        ObjectNotFound: if the author to be deleted does not exist

    Returns: 
        None
    """
    author = get_author_by_id(author_id)
    author.delete()