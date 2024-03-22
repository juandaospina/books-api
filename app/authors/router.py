from flask import Blueprint
from flask_restful import Api, Resource
from flask_apispec import views, doc, marshal_with, use_kwargs

from . import repository, schemas
from .models import Authors 
from app.docs import docs


authors_bp = Blueprint('authors', __name__)
api = Api(authors_bp)


@doc(tags=["Authors"])
class Authors(views.MethodResource, Resource):
    @doc(description="This method retrieves all authors.")
    @marshal_with(schemas.AuthorSchema(many=True))
    def get(self):
        data = repository.get_all_authors()
        return data, 200
    

    @doc(description="This method enable the creation of a new author.")
    @marshal_with(schemas.AuthorSchema, code=200)
    @use_kwargs(schemas.AuthorSchema(exclude=["created_at"]), location="json")
    def post(self, **kwargs):
        data = repository.create_author(**kwargs)
        return data, 200
    
    
@doc(tags=["Authors"])
class Author(views.MethodResource, Resource):
    @doc(description="This method retrieves an author by id.")
    @marshal_with(schemas.AuthorSchema(), code=200)
    def get(self, author_id):
        data = repository.get_author_by_id(author_id)
        return data, 200
    

    @doc(description="This method upgrade an author.")
    @use_kwargs(schemas.AuthorSchema(exclude=["created_at"]), location="json")
    def put(self, author_id, **kwargs):
        _author = repository.update_author(author_id, **kwargs)
        data = schemas.AuthorSchema().dump(_author)
        return data, 200
    

    @doc(description="Method for delete an author by id.")
    @marshal_with(schemas.EmptySchema, code=204, description="If author is deleted successfully")
    def delete(self, author_id):
        repository.delete_author(author_id)
        return None, 204


# Add resources
api.add_resource(Authors, "/authors")
api.add_resource(Author, "/author/<int:author_id>")

# Register resources for docs
docs.register(Authors, blueprint=authors_bp.name)
docs.register(Author, blueprint=authors_bp.name)