from flask import Blueprint
from flask_restful import Api, Resource
from flask_apispec import views, doc, marshal_with, use_kwargs

from . import repository 
from .schemas import BooksSchema, BookResponseSchema, EmptySchema
from app.docs import docs


books_bp = Blueprint('books', __name__, url_prefix="/v1")
api = Api(books_bp)
    

@doc(tags=['Books'], responses={422: {"description": "Entidad no procesable"}})
class BooksResource(views.MethodResource, Resource):
    @doc(description="Get all books from repository")
    @marshal_with(BookResponseSchema(many=True, 
                                     exclude=["author_id", "format_id", "editorial_id"]), 
                                     code=200)
    def get(self):
        data = repository.get_all_books()
        return data, 200

    @doc(description="Create a new book in the repository", code=200)
    @marshal_with(BookResponseSchema(exclude=["author_id", "format_id", "editorial_id"]))
    @use_kwargs(BooksSchema, location="json")
    def post(self, **kwargs):
        # errors = BooksSchema().validate(data=kwargs)
        data = repository.create_book(**kwargs)
        return data, 200
    

@doc(tags=['Books'], responses={
    404: {"description": "Objecto no encontrado"}, 
    422: {"description": "Entidad no procesable"}}
)
class BookResource(views.MethodResource, Resource):
    @doc(description="Get a book by id")
    @marshal_with(BookResponseSchema(exclude=["author_id", "format_id", "editorial_id"]), 
                  code=200)
    def get(self, book_id: int):
        data = repository.get_book_by_id(book_id)
        return data, 200

    @doc(description="Update a book")
    @marshal_with(BookResponseSchema(exclude=["author_id", "format_id", "editorial_id"]), 
                  code=200)
    @use_kwargs(BooksSchema, location="json")
    def put(self, book_id: int, **kwargs):
        # errors = BooksSchema().validate(kwargs)
        data = repository.update_book(book_id, **kwargs)
        return data, 200

    @doc(description="Delete a book")
    @marshal_with(EmptySchema, code=204)
    def delete(self, book_id: int):
        repository.delete_book(book_id)
        return None, 204


# Add resources
api.add_resource(BooksResource, "/books")
api.add_resource(BookResource, "/book/<int:book_id>")

# Register resources for docs
docs.register(BooksResource, blueprint=books_bp.name)
docs.register(BookResource, blueprint=books_bp.name)