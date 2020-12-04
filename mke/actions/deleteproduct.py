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


# mongo db connection
Connection = os.getenv("MONGO_SRI")
client = MongoClient(Connection)
db = client["frames_db"]
collection = db["frames"]


deleteEndPoint = Blueprint("deleteEndPoint", __name__)


@deleteEndPoint.route("/deleteproduct/<id>", methods=["DELETE"])
@jwt_required
def deliT(id):
    collection.delete_one({"_id": ObjectId(id)})

    return "product deleted..", 200
