from marshmallow import Schema, fields, validate


class AppUser(Schema):
    _id = fields.String(required=False)
    firstName = fields.String(required=True)
    lastName = fields.String(required=True)
    age = fields.Integer(
        required=False,
        error_messages={'required': 'Age is required.'}
    )
