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
testEndPoint = Blueprint("testEndPoint", __name__)


@testEndPoint.route("/test/<ref>", methods=["GET"])
def acc(ref):
    if not ref:
        return "no ref", 200
    else:
        return "ref", 200