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
import requests
import json


# mongo db connection
Connection = os.getenv("MONGO_SRI")
paystack = os.getenv("pAPI_KEY")
client = MongoClient(Connection)
db = client["frames_db"]
collection = db["orders"]


payEndPointU = Blueprint("payEndPointU", __name__)


@payEndPointU.route("/payproduct", methods=["POST"])
def view():

    data = request.json
    referenceCode = data["referenceCode"]
    customerName = data["customerName"]
    customerEmail = data["customerEmail"]
    customerPhone = data["customerPhone"]
    customerAddress = data["customerAddress"]

    verifyPayments = requests.get(f"https://api.paystack.co/transaction/verify/{referenceCode}",  headers={
        'Authorization': f'Bearer {paystack}'})

    print(verifyPayments.content)
   # data = json.loads(verifyPayments.content)

    # transDate = data["data"]["transaction_date"]

    return "Transaction successful..", 200
