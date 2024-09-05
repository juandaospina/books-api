from flask import Blueprint
from flask_restful import Api, Resource
from flask_apispec import views, doc, marshal_with

from app.docs import docs
from . import repository, schemas


editorials_bp = Blueprint("editorials", __name__, url_prefix="/api/v1")
api = Api(editorials_bp)


@doc(tags=["Editorials"])
class EditorialResource(views.MethodResource, Resource):
    @doc(description="Return all the editorials")
    @marshal_with(schemas.EditorialSchema(many=True), code=200)
    def get(self):
        data = repository.get_all_editorials()
        return data, 200


# Add resourceS
api.add_resource(EditorialResource, "/editorials")

# Register resources for docs
docs.register(EditorialResource, blueprint=editorials_bp.name)