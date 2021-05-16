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
db = client["frames_db"]
collection = db["frames"]


viewallEndPoint = Blueprint("viewallEndPoint", __name__)


@viewallEndPoint.route("/viewproducts", methods=["GET"])
@jwt_required
def view():
    
    products = collection.find()
    resp = json_util.dumps(products, indent=4)
    
    '''
    offset = 0
    #offset = int(request.args["offset"])
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
    return resp


#work on getting upset fixes using conditional statement