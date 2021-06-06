import ssl
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

from validators.email import email
load_dotenv()


# mongo db connection
Connection = os.getenv("MONGO_SRI")
client = MongoClient(Connection, ssl_cert_reqs=ssl.CERT_NONE)
db = client["autos_db"]
collection = db["affil"]

# register blueprint
createProfileEndPoint = Blueprint("createProfileEndPoint", __name__)


@createProfileEndPoint.route("/createprofile", methods=["POST"])
@jwt_required
def acc():
    try:
        data = request.json
        firstName = data["firstName"]
        lastName = data["lastName"]
        phoneNumber = data["phoneNumber"]
        accNumber = data["accNumber"]
        bankName = data["bankName"]

        if not firstName:
            return "firstname is missing", 400
        if not lastName:
            return "lastname is missing", 400
        if not phoneNumber:
            return "phonenumber is missing", 400
        if not accNumber:
            return "accountnumber is missing", 400
        if not bankName:
            return "bank name is missing", 400

        getEmail = get_jwt_identity()

        email = getEmail["email"]

        checkEmail = collection.find_one({"email": email})

        if checkEmail != None:

            collection.update_one({"email": email},
                                  {
                "$set": {

                    "user profile":  {
                        "firstname": firstName,
                        "lastname": lastName,
                        "accountNumber": accNumber,
                        "phone": phoneNumber,
                        "bankName": bankName
                    }
                }
            })

            res = "profile updated..."
            return res, 200

        else:
            res = "account does not exist.."
            return res, 404

    except Exception as x:
        print(x)
