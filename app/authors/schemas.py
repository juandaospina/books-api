from marshmallow import fields, validate

from app.db import ma


class AuthorSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    about_author = fields.String(allow_none=True)
    born_date = fields.Integer()
    created_at = fields.DateTime(dump_only=True)
    email = fields.String(validate=validate.Email(error="Invalid email address"))
    first_name = fields.String()
    last_name = fields.String()
    nacionality = fields.String()
    updated_at = fields.DateTime(dump_only=True)

class EmptySchema(ma.Schema):
    pass