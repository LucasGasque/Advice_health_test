from flask import Blueprint

from app.controllers.cars import register_car

bp_cars = Blueprint("cars", __name__, url_prefix="/cars")

bp_cars.post("")(register_car)
