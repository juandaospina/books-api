import typing as t

from .models import Editorial 

def get_all_editorials() -> t.List[Editorial]:
    """Retrieve all the editorials for a repository

    :return: A list of Editorial objects
    """
    return Editorial.get_all()