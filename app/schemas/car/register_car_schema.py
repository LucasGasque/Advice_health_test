from marshmallow import Schema, fields, post_load, validate

from app.models.cars import Car


class CarSchema(Schema):
    name = fields.String(required=True)
    color = fields.String(
        required=True, validate=validate.OneOf(["yellow", "blue", "gray"])
    )
    model = fields.String(
        required=True, validate=validate.OneOf(["hatch", "sedan", "convertible"])
    )
    owner_id = fields.Integer()

    @post_load
    def create_car(self, data, **kwargs):
        data["car_owner_id"] = data.pop("owner_id")

        return Car(**data)
