from flask import Flask, Blueprint

from app.routes.auth import bp_auth
from app.routes.car_owners import bp_owners
from app.routes.cars import bp_cars


def init_app(app: Flask):
    bp_api = Blueprint("api", __name__, url_prefix="/api")

    bp_api.register_blueprint(bp_auth)
    bp_api.register_blueprint(bp_owners)
    bp_api.register_blueprint(bp_cars)

    app.register_blueprint(bp_api)
