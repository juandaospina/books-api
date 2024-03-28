from marshmallow import fields

from app.db import ma

class EditorialsSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    about = fields.String(allow_none=True)
    created_at = fields.DateTime(dump_only=True)