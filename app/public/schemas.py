from marshmallow import fields

from app.db import ma


class InfoSchema(ma.Schema):
    app_name = fields.String()
    version = fields.String()
    docs_url = fields.String()
    description = fields.String()