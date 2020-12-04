from flask import Blueprint, jsonify, request, Flask
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from bson.json_util import dumps
from bson import json_util


# mongo db connection
Connection = os.getenv("MONGO_SRI")
client = MongoClient(Connection)
db = client["frames_db"]
collection = db["frames"]


viewEndPoint = Blueprint("viewEndPoint", __name__)


@viewEndPoint.route("/viewproduct/<id>", methods=["GET"])
def view(id):
    product = collection.find_one({"_id":ObjectId(id)})
    resp = json_util.dumps(product, indent=4)

    return resp
