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
collection2 = db["affil"]


viewCarDetailsEndPointC = Blueprint("viewCarDetailsEndPointC", __name__)


@viewCarDetailsEndPointC.route("/viewcar/<id>", methods=["GET"])
@jwt_required
def view(id):

    getEmail = get_jwt_identity()

    email = getEmail["email"]

    checkEmail = collection2.find_one({"email": email})

    if checkEmail != None:
        userName = checkEmail["username"]
        product = collection.find_one({"_id": ObjectId(id)})
        querylink = f"http://localhost:3000/autos/affiliates/garage/{ObjectId(id)}?ref={userName}"
        res = jsonify({
            "carname": product["carname"],
            "description": product["description"],
            "carprice": product["carprice"],
            "commission": product["commission"],
            "mediaurl": product["mediaUrl"],
            "available": product["available"],
            "reflink": querylink
        })

        return res, 200
    else:
        return "invalid token...", 400

    '''
    offset = 0
    # offset = int(request.args["offset"])
    startingId = collection.find().sort("_id", pymongo.ASCENDING)
    lastId = startingId[5]["_id"]
    numbers = collection.find({
        "_id": {
            "$gte": lastId
        }
    }).sort("_id", pymongo.ASCENDING).limit(5)

    nextUrl = offset + 5
    prevUrl = offset - 5

    resp = json_util.dumps({
        "result": numbers,
        "pre_url": prevUrl,
        "next_url": nextUrl
    }, indent=4)
    '''


# work on getting upset fixes using conditional statement
