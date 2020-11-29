from flask import Blueprint

loginEndPoint = Blueprint("loginEndPoint", __name__)


@loginEndPoint.route("/signin", methods=["POST"])
def login():
    return "e dy work"


