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
import smtplib
from flask_cors import CORS, cross_origin

# mongo db connection
Connection = os.getenv("MONGO_SRI")
client = MongoClient(Connection, ssl_cert_reqs=ssl.CERT_NONE)
db = client["frames_db"]
collection = db["orders"]


emailAddress = os.getenv("BASE_EMAIL")
emailPassword = os.getenv("BASE_P")



pOrderEndPointU = Blueprint("pOrderEndPointU", __name__)


@pOrderEndPointU.route("/processorder/<id>", methods=["POST"])
# @jwt_required
@cross_origin()
def view(id):
    data = request.json
    orderEmail = data["orderEmail"]


    collection.update_one({"_id": ObjectId(id)},
                          {
        "$set": {


            "delivered": True

        }
    })

    mail(orderEmail)

    resp = jsonify("Customer notified of order processing!")

    return resp, 200




def mail(cEmail):
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(emailAddress, emailPassword)

        subject = "Order Processing"
        body = f"Hi, your order is processing. you should recieve it in 2-3 days."

        msg = f'subject:  {subject}\n\n{body}'

        #smtp.sendmail(emailAddress, "gogechi8@gmail.com", msg)
        smtp.sendmail(emailAddress, cEmail, msg)
