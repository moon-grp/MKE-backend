from flask import Blueprint, jsonify, request, Flask
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient 
from bson.objectid import ObjectId

import cloudinary as cloud
from cloudinary import uploader as uploadit
import os
from slugify import slugify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


# cloudinary config
cloud.config(cloud_name=os.getenv("CLOUD_NAME"),
             api_key=os.getenv("API_KEY"),
             api_secret=os.getenv("API_SECRET"))


# mongo db connection
Connection = os.getenv("MONGO_SRI")
client = MongoClient(Connection)
db = client["frames_db"]
collection = db["frames"]


editEndPoint = Blueprint("editEndPoint", __name__)


@editEndPoint.route("/editproduct/<id>", methods=["POST"])
@jwt_required
def updateFrame(id):

    productName = request.form.get("productName")
    framePrice = request.form.get("framePrice")
    available = request.form.get("available")
    description = request.form.get("description")
    slashPrice = request.form.get("slashPrice")
    slug = slugify(productName)

    # working on image
    frame_img = request.files["frame_img"]
    if productName and framePrice and available and description and slashPrice and frame_img:

        uploadToCloud = uploadit.upload(frame_img, )
        getImageUrl = uploadToCloud["url"]

        priceToFloat = float(framePrice)
        slashToFloat = float(slashPrice)
        #availableToBol = bool(available)

        collection.update_one({"_id": ObjectId(id)},
                              {
            "$set": {
                "productname": productName,
                "frameprice": priceToFloat,
                "available": available,
                "imgUrl": getImageUrl,
                "slashprice": slashToFloat,
                "description": description,
                "slug": slug

            }
        })

        return "product updated..", 200

    else:
        return "enter all required fields..", 400
