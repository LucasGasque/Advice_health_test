from marshmallow import Schema, fields, post_load

from app.models.car_owners import CarOwner


class CarOwnerSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    sale_opportunity = fields.Boolean(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        name = data.get("name")
        data["name"] = name.title()
        return CarOwner(**data)
