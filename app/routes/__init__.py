from flask import Flask, Blueprint


def init_app(app: Flask):
    bp_api = Blueprint("api", __name__, url_prefix="/api")

    app.register_blueprint(bp_api)
