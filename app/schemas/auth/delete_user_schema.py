from marshmallow import Schema, fields


class DeleteUserSchema(Schema):
    userId = fields.Integer(required=True)
