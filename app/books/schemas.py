from datetime import datetime

from marshmallow import fields, validate, ValidationError

from app.authors.schemas import AuthorSchema
from app.db import ma

class IsbnValidator(validate.Validator):
    max_numbers = 13

    def __init__(self, message=None):
        self.message = message or 'La validación personalizada ha fallado'

    def __call__(self, value):
        if not self.validate(value):
            raise ValidationError(self.message)

    def validate(self, value):
        return len(str(value)) <= self.max_numbers


class BooksSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    isbn = fields.Integer(validate=IsbnValidator(), allow_none=True)
    isbn13 = fields.Integer(validate=IsbnValidator(), allow_none=True) 
    title = fields.String(validate=validate.Length(min=1, max=100))
    description = fields.String(
        validate=validate.Length(min=1, max=255), allow_none=True)
    published_year = fields.Integer(
        validate=validate.Range(min=1900, max=datetime.now().year), allow_none=True)
    language = fields.String()
    number_of_pages = fields.Integer()
    edition_number = fields.Integer(allow_none=True)
    author_id = fields.Integer(required=True) 
    format_id = fields.Integer(required=True)


class BookResponseSchema(BooksSchema):
    author = fields.Nested(AuthorSchema, dump_only=True)
    format = fields.String(attribute="format.format", dump_only=True)

class EmptySchema(ma.Schema):
    pass
