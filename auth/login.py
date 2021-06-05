from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask import Blueprint, jsonify, request, Flask
from flask_pymongo import PyMongo

import bcrypt
import datetime
import validators
from bson import json_util
from bson.json_util import dumps
import json
from dotenv import load_dotenv
import os
load_dotenv()

# register blueprint
loginEndPoint = Blueprint("loginEndPoint", __name__)


@loginEndPoint.route("/signin", methods=["POST"])
def login():
    data = request.json
    email = os.getenv("EMAIL")
    password = data["password"]

    o_pass = os.getenv("PASSCODE")
    hashed = bcrypt.hashpw(o_pass.encode("utf-8"), bcrypt.gensalt(12))
    if password:
        if bcrypt.checkpw(password.encode("utf-8"), hashed):

            access_token = create_access_token(identity={"email": email})

            res = jsonify({
                "message": "Welcome, kay..",
                "token": access_token
            })

            return res, 200
        else:
            return "wrong password", 400
    else:
        return "Enter password!!", 400
