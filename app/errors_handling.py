from flask import Flask, jsonify

from .exceptions import ObjectNotFound


def register_errors(app: Flask):
    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found(exc: ObjectNotFound):
        return exc.to_dict(), 404

    @app.errorhandler(422)
    def handle_unprocessable_entity(exc: Exception):
        return jsonify({
            "message": "Entidad no procesable", 
            "status_code": 422
        }), 422