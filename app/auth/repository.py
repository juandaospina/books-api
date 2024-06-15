from .models import User
from app.errors_handling import ObjectNotFound


def get_user(username: int) -> User:
    user = User.query.filter(User.username ==  username).first()
    if user is None:
        raise ObjectNotFound()
    return user