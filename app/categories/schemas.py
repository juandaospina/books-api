from marshmallow import fields, validate

from app.db import ma


class CategorySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(validate=validate.Length(min=1, max=100), 
                         allow_none=False)
    description = fields.String(validate=validate.Length(min=1, max=100), 
                                allow_none=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)