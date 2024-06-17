from marshmallow import fields, validate

from app.db import ma


class UserSchema(ma.Schema):
    username = fields.String(validate=validate.Length(min=3))
    password = fields.String(validate=validate.Length(min=6))