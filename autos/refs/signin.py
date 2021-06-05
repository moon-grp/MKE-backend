from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask import Blueprint, jsonify, request, Flask
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient

import bcrypt
import datetime
import validators
from bson import json_util
from bson.json_util import dumps
import json
from dotenv import load_dotenv
import os
load_dotenv()
import ssl


# mongo db connection
Connection = os.getenv("MONGO_SRI")
client = MongoClient(Connection, ssl_cert_reqs=ssl.CERT_NONE)
db = client["autos_db"]
collection = db["affil"]

# register blueprint
signInEndPoint = Blueprint("signInEndPoint", __name__)


@signInEndPoint.route("/signin", methods=["POST"])
def acc():
    try:
        data = request.json
        email = data["email"]
        password = data["password"]

        if not email:
            return "email is missing", 400
        if not password:
            return "password is missing", 400

        if validators.email(email) != True:
            return "Boba says email is not valid", 400

        checkEmail = collection.find_one({"email": email})

        if checkEmail != None:
            encPassword = checkEmail["password"]

            if bcrypt.checkpw(password.encode("utf-8"), encPassword):

                access_token = create_access_token(identity={"email": email})

                res = jsonify({
                    "message": "login succesful..",
                    "token": access_token
                })

                return res, 200
            else:
                res = "invalid password."
                return res, 400

        else:
            res = "account does not exist.."
            return res, 404

    except Exception as x:
        print(x)
