from flask import Flask

from .exceptions import ObjectNotFound


def register_errors(app: Flask):
    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found(exc: ObjectNotFound):
        return exc.to_dict()