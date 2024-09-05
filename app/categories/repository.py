import typing as t

from .models import Category


def get_categories() -> t.List[Category]:
    """This function returns a list of categories in the database

    :return: A list of categories objects
    """
    categories = Category.get_all()
    return categories