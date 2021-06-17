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
client = MongoClient(Connection, ssl_cert_reqs=ssl.CERT_NONE)
db = client["autos_db"]
collection = db["cars"]


userViewCarDetailsEndPointC = Blueprint("userViewCarDetailsEndPointC", __name__)


@userViewCarDetailsEndPointC.route("/uviewcar/<id>", methods=["GET"])
def view(id):

        product = collection.find_one({"_id": ObjectId(id)})

        res = jsonify({
            "carname": product["carname"],
            "description": product["description"],
            "carprice": product["carprice"],
            "mediaurl": product["mediaUrl"],
            
            
        })

        return res, 200


    


# work on getting upset fixes using conditional statement
