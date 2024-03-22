import typing as t

from .models import Authors
from app.exceptions import ObjectNotFound


def get_all_authors() -> t.List[Authors]:
    """
    Retrieves all author from the database

    Returns:
        List[Authors]: List of authors
    """
    return Authors.get_all()

def get_author_by_id(id: int) -> t.Optional[Authors]:
    """
    Retrieve an author by id

    Parameters:
        id (int): ID of the author

    Raises:
        ObjectNotFound: if the author is not found
    
    Returns:
        Dict[Authors] or None if the author is not found
    """
    _author = Authors.get_by_id(id)
    if _author is None:
        raise ObjectNotFound()
    return _author

def create_author(first_name, last_name, age, email, nacionality) -> Authors:
    """
    Create a new author in the repository

    Parameters:
        first_name (str): The first name of the author
        last_name (str): The last name of the author
        age (int): The age of the author
        email (str): The email address of the author
        nacionality (str): The nacionality of the author

    Returns:
        Dict[Authors]: The new author object
    """
    _author = Authors(first_name, last_name, age, email, nacionality)
    return Authors.create_object(_author)

def update_author(author_id: int, **kwargs) -> Authors:
    """
    Updates the information about the author of the repository

    Parameters:
        author_id (int): ID of the author to be updated
        kwargs (dict): Additional properties to be passed to the update 

    Raises:
        ObjectNotFound: if the author to be updated does not exist

    Returns:
        Dict[Authors]: The information of author updated
    """
    _author = get_author_by_id(author_id)
    _author.update(kwargs)
    return _author

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
    _author = get_author_by_id(author_id)
    _author.delete()