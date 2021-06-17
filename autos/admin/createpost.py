from flask import Blueprint, jsonify, request, Flask
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient

import cloudinary as cloud
from cloudinary import uploader as uploadit
import os
from slugify import slugify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import ssl


# cloudinary config
cloud.config(cloud_name=os.getenv("CLOUD_NAME"),
             api_key=os.getenv("API_KEY"),
             api_secret=os.getenv("API_SECRET"))


# mongo db connection
Connection = os.getenv("MONGO_SRI")
client = MongoClient(Connection, ssl_cert_reqs=ssl.CERT_NONE)
db = client["autos_db"]
collection = db["cars"]
collection2 = db["userfacing"]


autosAdminCEndPoint = Blueprint("autosAdminCEndPoint", __name__)


@autosAdminCEndPoint.route("/addcar", methods=["POST"])
@jwt_required
def uploadFrames():

    data = request.json

    #name = data["name"]
    #collection.insert_one({"name": name})
    carName = request.form.get("carName")
    carPrice = request.form.get("carPrice")
    #available = request.form.get("available")
    description = request.form.get("description")
    commission = request.form.get("commission")
    slug = slugify(carName)

    # working on image
    car_img = request.files["car_img"]

    uploadToCloud = uploadit.upload(car_img, )
    getImageUrl = uploadToCloud["url"]

    priceToFloat = float(carPrice)
    comToFloat = float(commission)

    collection.insert_one({
        "carname": carName,
        "carprice": priceToFloat,
        "available": True,
        "description": description,
        "commission": comToFloat,
        "mediaUrl": getImageUrl,
        "slug": slug
    })

    return "post created...", 200
