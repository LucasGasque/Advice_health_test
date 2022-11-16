from flask import Blueprint

from app.controllers.owners import get_all_owners

bp_owners = Blueprint("car_owners", __name__, url_prefix="/owners")

bp_owners.get("")(get_all_owners)
