from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required

from app.models.car_owners import CarOwner


def get_all_owners():
    try:
        owners = CarOwner.query.all()

        return jsonify(owners), HTTPStatus.OK
    except Exception as e:
        return {"Error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
