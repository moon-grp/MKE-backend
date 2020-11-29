from flask import Blueprint, jsonify, request, Flask
from flask_pymongo import PyMongo

import bcrypt
import datetime
import validators
from bson import json_util
from bson.json_util import dumps
import json

loginEndPoint = Blueprint("loginEndPoint", __name__)


@loginEndPoint.route("/signin", methods=["POST"])
def login():
    data = request.json
    email = "abankab@gmail.com"
    password = data["password"]

    o_pass = "mrMKEkay"
    hashed = bcrypt.hashpw(o_pass.encode("utf-8"), bcrypt.gensalt(12))
    if password:
        if bcrypt.checkpw(password.encode("utf-8"), hashed):

            access_token = create_access_token(identity={"email": email})

            res = jsonify({
            "message": "Welcome, mr kay..",
            "token": access_token
            })

            return res, 200
        else:
            return "wrong password", 400
    else:
        return "Enter password!!", 400
