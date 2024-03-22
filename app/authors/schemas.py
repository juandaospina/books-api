from marshmallow import fields, validate

from app.db import ma


class AuthorSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String()
    last_name = fields.String()
    age = fields.Integer()
    email = fields.String(validate=validate.Email(error="Invalid email address"))
    nacionality = fields.String()
    created_at = fields.DateTime()

class EmptySchema(ma.Schema):
    pass