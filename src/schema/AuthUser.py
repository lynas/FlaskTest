from marshmallow import Schema, fields, validate


class AuthUser(Schema):
    _id = fields.String(required=False)
    username = fields.String(required=True)
    password = fields.String(required=True)
