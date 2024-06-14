from flask import Blueprint
from flask_apispec import views, doc, marshal_with
from flask_restful import Api, Resource

from app.docs import docs
from .schemas import CategorySchema
from . import repository


category_bp = Blueprint("category", __name__, url_prefix="/v1")
api = Api(category_bp)

@doc(tags=["Categories"], responses={
    200: {"description": "Respuesta exitosa"}})
class CategoryResource(views.MethodResource, Resource):
    @doc(description="Get all categories")
    @marshal_with(CategorySchema(many=True))
    def get(self):
        data = repository.get_categories()
        return data, 200


# Add resource
api.add_resource(CategoryResource, "/category")

# Register resource for docs
docs.register(CategoryResource, blueprint=category_bp.name)