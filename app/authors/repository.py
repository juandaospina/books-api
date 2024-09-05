import typing as t
from datetime import datetime

from .models import Author
from app.exceptions import ObjectNotFound


def get_all_authors() -> t.List[Author]:
    """Retrieves all author from the database.

    :return: List of authors.
    """
    return Author.get_all()


def get_author_by_id(id: int) -> t.Optional[Author]:
    """Returns an author by id.

    :param id: The id of the author
    :raise ObjectNotFound: if the author does not exist
    :return: An author object.
    """
    author = Author.get_by_id(id)
    if author is None:
        raise ObjectNotFound()
    return author


def create_author(
        first_name, 
        last_name, 
        email, 
        nacionality, 
        about_author, 
        born_date
    ) -> Author:
    """Create a new author in the database.

    :param first_name: The first name of the author
    :param last_name: The last name of the author
    :param email: The email address of the author
    :param nacionality: The nacionality of the author
    :param **kwargs (dict): Additional properties
    :return: The new author object
    """
    author = Author(first_name, last_name, email, 
                      nacionality, about_author, born_date)
    return Author.create_object(author)


def update_author(author_id: int, **kwargs) -> Author:
    """Updates the information about the author of the database.

    :param author_id: ID of the author to be updated
    :param **kwargs: Additional properties to be passed to the update 
    :raise ObjectNotFound: if the author to be updated does not exist
    :return: The information of author updated
    """
    author = get_author_by_id(author_id)
    kwargs["updated_at"] = datetime.now()
    author.update(kwargs)
    return author


def delete_author(author_id: int) -> None:
    """Delete the author from the repository

    :param author_id: ID of the author to be deleted
    :raise ObjectNotFound: if the author to be deleted does not exist
    :return: None
    """
    author = get_author_by_id(author_id)
    author.delete()