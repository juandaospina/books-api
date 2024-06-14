import typing as t

from .models import Category


def get_categories() -> t.List[Category]:
    """
    This function returns a list of categories in the database

    returns: 
        List[Category]
    """
    categories = Category.get_all()
    return categories