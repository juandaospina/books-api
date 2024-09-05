import typing as t

from .models import Editorial 

def get_all_editorials() -> t.List[Editorial]:
    """
    Retrieve all the editorials for a repository

    Returns:
        List[Editorial]: A list of Editorial
    """
    return Editorial.get_all()