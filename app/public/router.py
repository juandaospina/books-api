from flask import Blueprint
from flask_restful import Api, Resource
from flask_apispec import views, doc, marshal_with

from app.docs import docs
from .schemas import InfoSchema


public_bp = Blueprint("public", __name__)
api = Api(public_bp)


@doc(tags=["Public"])
class PublicResource(views.MethodResource, Resource):
    @doc(description="Return all the editorials")
    @marshal_with(InfoSchema, code=200)
    def get(self):
        return {
            "app_name": "Books API",
            "version": "1.0.0",
            "docs_url": '/docs-ui',
            "description": "API for searching books and information about their authors," 
                " categories and editorials - (Flask - PostgreSQL)",
        }, 200


# Add resourceS
api.add_resource(PublicResource, "/")

# Register resources for docs
docs.register(PublicResource, blueprint=public_bp.name)