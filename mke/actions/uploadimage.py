from flask import Blueprint, jsonify, request, Flask
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient

import cloudinary as cloud
from cloudinary import uploader as uploadit
import os
from slugify import slugify
from werkzeug.datastructures import ImmutableDict


# cloudinary config
cloud.config(cloud_name=os.getenv("CLOUD_NAME"),
             api_key=os.getenv("API_KEY"),
             api_secret=os.getenv("API_SECRET"))


# mongo db connection
Connection = os.getenv("MONGO_SRI")
client = MongoClient(Connection)
db = client["frames_db"]
collection = db["frames"]


uploadEndPoint = Blueprint("uploadEndPoint", __name__)


@uploadEndPoint.route("/addframe", methods=["POST"])
def uploadFrames():

    data = request.json
    d = dict(request.form)
    dd = request.form.get("name")

    #name = data["name"]
    #collection.insert_one({"name": name})
    productName = request.form.get("productName")
    framePrice = request.form.get("framePrice")
    available = request.form.get("available")
    description = request.form.get("description")
    slashPrice = request.form.get("slashPrice")
    slug = slugify(productName)

    # working on image
    frame_img = request.files["frame_img"]
    uploadToCloud = uploadit.upload(frame_img, )
    getImageUrl = uploadToCloud["url"]

    priceToFloat = float(framePrice)
    slashToFloat = float(slashPrice)
    availableToBol = bool(available)

    collection.insert_one({
        "productname": productName,
        "frameprice": priceToFloat,
        "available": availableToBol,
        "imgUrl": getImageUrl,
        "slashprice": slashToFloat,
        "slug": slug,
        "description": description
    })

    return "product uploaded...", 200
