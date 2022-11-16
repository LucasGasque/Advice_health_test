from http import HTTPStatus
from flask import jsonify, request, current_app

from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound
from flask_jwt_extended import jwt_required

from app.exceptions import CarLimitReached
from app.models.car_owners import CarOwner
from app.schemas.car.register_car_schema import CarSchema


@jwt_required()
def register_car():
    try:
        data = request.get_json()

        owner_id = data.get("owner_id")

        owner = CarOwner.query.filter_by(id=owner_id).one()

        setattr(owner, "sale_opportunity", False)

        current_app.db.session.add(owner)
        current_app.db.session.commit()

        if len(owner.cars) >= 3:
            raise CarLimitReached

        car = CarSchema().load(data)

        current_app.db.session.add(car)
        current_app.db.session.commit()

        return jsonify(car), HTTPStatus.CREATED

    except ValidationError as err:
        return jsonify({"Error": err.messages}), HTTPStatus.BAD_REQUEST

    except NoResultFound:
        return jsonify({"Error": "Owner not found"}), HTTPStatus.NOT_FOUND

    except CarLimitReached:
        return {"Error": "Car limit reached"}, HTTPStatus.BAD_REQUEST

    except Exception as e:
        return {"Error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
