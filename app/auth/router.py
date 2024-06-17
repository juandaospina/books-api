from flask import Blueprint
from flask_apispec import views, doc, use_kwargs
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token

from app.errors_handling import Unauthorized
from app.docs import docs
from .schema import UserSchema
from . import repository


jwt_bp = Blueprint("jwt", __name__, url_prefix="/v1")
api = Api(jwt_bp)


@doc(tags=["Authorization"], responses={
    401: {"description": "Usuario no autorizado"},
    404: {"description": "Objecto no encontrado"}})
class TokenResource(views.MethodResource, Resource):
    @doc(description="Get authorization token")
    @use_kwargs(UserSchema, location="json")
    def post(self, **kwargs):
        username = kwargs.get("username")
        user = repository.get_user(username)
        if user.password != kwargs.get("password"):
            raise Unauthorized()
        token = create_access_token(identity=user.username)
        return {"access_token": token}, 200
    

api.add_resource(TokenResource, "/token")
docs.register(TokenResource, blueprint=jwt_bp.name)