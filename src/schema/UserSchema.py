from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(
        required=True,
        error_messages={'required': 'Age is required.'}
    )
    city = fields.String(
        required=True,
        error_messages={'required': {'message': 'City required', 'code': 400}}
    )
    email = fields.Str(required=True,
                       validate=validate.Email(error='Not a valid email address'))
