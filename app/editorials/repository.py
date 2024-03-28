import typing as t

from .models import Editorials 

def get_all_editorials() -> t.List[Editorials]:
    """
    Retrieve all the editorials for a repository

    Returns:
        List[Editorials]: A list of Editorials
    """
    return Editorials.get_all()