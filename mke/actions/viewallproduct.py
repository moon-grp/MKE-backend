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


viewallEndPoint = Blueprint("viewallEndPoint", __name__)


@viewallEndPoint.route("/viewproducts", methods=["GET"])
def view():
    products = collection.find()
    resp = json_util.dumps(products, indent=4)

    return resp
