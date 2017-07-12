from marshmallow import Schema, fields, validate


class AppUser(Schema):
    firstName = fields.String(required=True)
    lastName = fields.String(required=True)
    age = fields.Integer(
        required=True,
        error_messages={'required': 'Age is required.'}
    )
