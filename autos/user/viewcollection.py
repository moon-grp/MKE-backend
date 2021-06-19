from flask import Blueprint, jsonify, request, Flask
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from bson.json_util import dumps
from bson import json_util
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import ssl

# mongo db connection
Connection = os.getenv("MONGO_SRI")
client = MongoClient(Connection)
db = client["autos_db"]
collection = db["cars"]


userViewallEndPointC = Blueprint("userViewallEndPointC", __name__)


@userViewallEndPointC.route("/ucars", methods=["GET"])
def view():

    products = collection.find({}, {"carname":1, "carprice":1, "available":1, "mediaUrl":1})
    resp = json_util.dumps(products, indent=4)
   

    
    return resp, 200


# work on getting upset fixes using conditional statement
