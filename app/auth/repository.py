from .models import User
from app.errors_handling import ObjectNotFound


def get_user(username: int) -> User:
    """Returns a User object with the given username.

    :param username: The username to get the user from database.
    :raise ObjectNotFound: If the username is not found.
    :return: A User object.
    """
    user = User.query.filter(User.username ==  username).first()
    if user is None:
        raise ObjectNotFound()
    return user