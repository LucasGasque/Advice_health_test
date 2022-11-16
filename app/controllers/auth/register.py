from http import HTTPStatus
from flask import request
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session

from app.models.auth import Auth
from app.schemas.auth.register_user_schema import RegisterUserSchema
from app.schemas.auth.register_car_owner_schema import CarOwnerSchema
from app.configs.database import db


def register_user():
    try:
        data = request.get_json()
        new_user_auth_found = None

        name = data.pop("name", None)
        sale_opportunity = data.pop("sale_opportunity", True)

        new_user_auth_table = RegisterUserSchema().load(data)

        session: Session = db.session
        session.add(new_user_auth_table)

        new_user_auth_found = Auth.query.filter_by(
            email=new_user_auth_table.email
        ).first()
        auth_id = new_user_auth_found.id

        new_car_owner = CarOwnerSchema().load(
            {
                "name": name,
                "sale_opportunity": sale_opportunity,
                "id": auth_id,
            }
        )

        session.add(new_car_owner)
        session.commit()

        return "", HTTPStatus.CREATED

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"Error": "E-mail already registered in database"}, HTTPStatus.CONFLICT
