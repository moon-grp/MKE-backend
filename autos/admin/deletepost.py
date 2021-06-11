from flask import Blueprint, jsonify, request, Flask
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import ssl

# mongo db connection
Connection = os.getenv("MONGO_SRI")
client = MongoClient(Connection, ssl_cert_reqs=ssl.CERT_NONE)
db = client["autos_db"]
collection = db["cars"]


deleteEndPointC = Blueprint("deleteEndPointC", __name__)


@deleteEndPointC.route("/deletepost/<id>", methods=["DELETE"])
@jwt_required
def deliT(id):
    collection.delete_one({"_id": ObjectId(id)})

    return "post deleted..", 200
